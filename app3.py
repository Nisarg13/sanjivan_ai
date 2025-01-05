import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from llama_index.core.query_pipeline import QueryPipeline as QP, Link, InputComponent
from llama_index.experimental.query_engine.pandas import PandasInstructionParser
from llama_index.llms.openai import OpenAI
from llama_index.core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import io
import contextlib
import re

# Load environment variables
load_dotenv()

# Set Streamlit page configuration
st.set_page_config(page_title="Titanic Dataset Q&A", layout="wide")

# Function to extract Python code from LLM response
def extract_code(message):
    """
    Extracts Python code from a markdown-formatted code block in the message.
    """
    code_block = re.search(r'```python\s*([\s\S]*?)```', message)
    if code_block:
        return code_block.group(1).strip()
    return ""

# Function to sanitize generated code
def sanitize_code(code):
    """
    Sanitizes the extracted code by removing import statements and preventing dunder methods.
    """
    # Remove import statements
    code = re.sub(r'^\s*import\s+\w+.*$', '', code, flags=re.MULTILINE)
    code = re.sub(r'^\s*from\s+\w+\s+import\s+.*$', '', code, flags=re.MULTILINE)
    
    # Prevent usage of dunder methods
    if re.search(r'__\w+__', code):
        raise ValueError("Usage of private or dunder methods is not allowed.")
    
    return code

# Function to execute code and capture output
def execute_code(code, exec_env):
    """
    Executes sanitized code and captures its output.
    """
    captured_output = io.StringIO()
    try:
        with contextlib.redirect_stdout(captured_output):
            exec(code, exec_env)
    except Exception as e:
        return f"Error during execution: {e}"
    return captured_output.getvalue()

# Load Titanic dataset
@st.cache_data
def load_titanic_data():
    dataset_path = "tested.csv"  # Ensure this path is correct
    try:
        data = pd.read_csv(dataset_path, encoding="utf-8")
    except UnicodeDecodeError as e:
        st.error(f"Error reading the file: {e}")
        return pd.DataFrame()
    except FileNotFoundError:
        st.error(f"File not found: {dataset_path}")
        return pd.DataFrame()
    # Data Cleaning
    data['Age'] = pd.to_numeric(data['Age'], errors='coerce')
    data.fillna({"Age": -1, "Embarked": "unknown", "Fare": 0}, inplace=True)
    return data

# Streamlit UI
st.title("🛳️ Titanic Dataset Q&A")
st.write("Ask questions about the Titanic dataset using LlamaIndex and receive data-driven answers.")

# Load the dataset
data = load_titanic_data()
if data.empty:
    st.stop()  # Stop execution if data is not loaded

# Define allowed built-ins for safe execution
allowed_builtins = {
    "print": __builtins__["print"],
    "range": __builtins__["range"],
    "len": __builtins__["len"],
    "min": __builtins__["min"],
    "max": __builtins__["max"],
    "sum": __builtins__["sum"]
}

# Define Prompts and LLM
instruction_str = (
    "You have a pandas DataFrame named 'df'. "
    "You also have access to the following pre-imported modules: pandas as pd, matplotlib.pyplot as plt. "
    "Your task is to answer questions using Python expressions related to data analysis and visualization only. "
    "Do not include any import statements or use private methods (methods starting and ending with double underscores). "
    "Use only the pre-defined modules and functions available."
)

pandas_prompt_str = (
    "You are working with a pandas DataFrame in Python.\n"
    "The name of the DataFrame is `df`.\n"
    "This is the result of `print(df.head())`:\n"
    "{df_str}\n\n"
    "Instructions:\n"
    "{instruction_str}\n"
    "Query: {query_str}\n\n"
    "Expression:"
)

response_synthesis_prompt_str = (
    "Based on the input query and output results, generate a user-friendly response.\n\n"
    "Query: {query_str}\n"
    "Python Output: {pandas_output}\n\n"
    "Response:"
)

# Initialize Prompt Templates
pandas_prompt = PromptTemplate(pandas_prompt_str).partial_format(
    instruction_str=instruction_str,
    df_str=data.head(5).to_string()
)

response_synthesis_prompt = PromptTemplate(response_synthesis_prompt_str)

# Initialize LLM
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-3.5-turbo")

# Initialize Query Pipeline
qp = QP(
    modules={
        "input": InputComponent(),
        "pandas_prompt": pandas_prompt,
        "llm1": llm,
        "pandas_output_parser": PandasInstructionParser(df=data),
        "response_synthesis_prompt": response_synthesis_prompt,
        "llm2": llm,
    },
    verbose=True,  # Set to True for debugging
)

# Define the pipeline chain
qp.add_chain(["input", "pandas_prompt", "llm1", "pandas_output_parser"])

# Define Links between modules
qp.add_links([
    Link("input", "response_synthesis_prompt", dest_key="query_str"),
    Link("pandas_output_parser", "response_synthesis_prompt", dest_key="pandas_output"),
])

qp.add_link("response_synthesis_prompt", "llm2")

# Streamlit user input
user_query = st.text_input("💬 **Ask a question about the Titanic dataset:**", "")

# Function to detect if the query requests a plot
def is_plot_request(query):
    plot_keywords = ['plot', 'graph', 'chart', 'visualize', 'histogram', 'bar', 'scatter']
    return any(keyword in query.lower() for keyword in plot_keywords)

# Function to generate and display plots based on query
def generate_plot(query, df):
    # Simple keyword-based plot generation
    if 'age' in query.lower():
        st.write("### 📊 Age Distribution")
        fig, ax = plt.subplots()
        df['Age'].hist(ax=ax, bins=20, color='skyblue', edgecolor='black')
        ax.set_xlabel('Age')
        ax.set_ylabel('Frequency')
        ax.set_title('Age Distribution of Titanic Passengers')
        st.pyplot(fig)
    elif 'fare' in query.lower():
        st.write("### 📈 Fare Distribution")
        fig, ax = plt.subplots()
        df['Fare'].hist(ax=ax, bins=20, color='green', edgecolor='black')
        ax.set_xlabel('Fare')
        ax.set_ylabel('Frequency')
        ax.set_title('Fare Distribution of Titanic Passengers')
        st.pyplot(fig)
    elif 'survival' in query.lower():
        st.write("### 🪂 Survival Count")
        fig, ax = plt.subplots()
        survival_counts = df['Survived'].value_counts().sort_index()
        survival_counts.index = ['Did Not Survive', 'Survived']
        survival_counts.plot(kind='bar', ax=ax, color=['red', 'green'])
        ax.set_xlabel('Survival Status')
        ax.set_ylabel('Count')
        ax.set_title('Survival Count of Titanic Passengers')
        st.pyplot(fig)
    elif 'class' in query.lower():
        st.write("### 🏷️ Passenger Class Distribution")
        fig, ax = plt.subplots()
        class_counts = df['Pclass'].value_counts().sort_index()
        class_counts.index = ['1st Class', '2nd Class', '3rd Class']
        class_counts.plot(kind='bar', ax=ax, color=['gold', 'silver', 'brown'])
        ax.set_xlabel('Passenger Class')
        ax.set_ylabel('Count')
        ax.set_title('Passenger Class Distribution')
        st.pyplot(fig)
    else:
        st.warning("🔍 Sorry, I couldn't determine the type of plot you requested.")

# Handle user query
if user_query.strip():
    with st.spinner("🔄 Processing your query..."):
        try:
            # Run the query through the pipeline
            raw_response = qp.run(query_str=user_query)

            # Extract the final message from the response
            if isinstance(raw_response, str):
                final_msg = raw_response
            elif isinstance(raw_response, dict):
                final_msg = raw_response.get("response", str(raw_response))
            else:
                final_msg = str(raw_response)

            # Display the response
            st.write("### 📝 Response")
            st.write(final_msg)

            # Check if the user requested a plot
            if is_plot_request(user_query):
                generate_plot(user_query, data)

        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")
            st.stop()
