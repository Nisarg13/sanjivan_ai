# Titanic Dataset Q&A Streamlit Application

## Overview
The **Titanic Dataset Q&A** app is a Streamlit-based interactive application that allows users to query the Titanic dataset using natural language. Leveraging LlamaIndex and OpenAI's GPT-based language models, the app provides both data-driven responses and visualizations to user queries.

---

## Features
- **Natural Language Queries**: Ask questions about the Titanic dataset in plain English.
- **Interactive Visualizations**: Generate plots and charts for insights, such as age distribution, fare distribution, survival counts, and passenger class breakdowns.
- **Safe Code Execution**: Ensures safe execution of generated Python code with built-in sanitization mechanisms.
- **Streamlined UI**: Intuitive user interface with real-time query processing and dynamic responses.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/titanic-qna-app.git
   cd titanic-qna-app
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your OpenAI API key to a `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. Ensure the Titanic dataset (`tested.csv`) is placed in the root directory.

---

## Usage

1. Run the application:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your web browser at `http://localhost:8501`.

3. Interact with the app:
   - Enter a natural language query (e.g., "What is the age distribution of passengers?").
   - View the textual response and/or data visualizations.

---

## Example Queries
- "Show the distribution of passenger ages."
- "What is the average fare paid by passengers?"
- "Visualize the survival count."
- "Break down the passengers by class."

---

## Technical Details

### Key Libraries and Tools
- **Streamlit**: Framework for building the web application.
- **Pandas**: Data analysis and manipulation library.
- **Matplotlib**: Visualization library for generating plots.
- **LlamaIndex**: For integrating language models into the data querying pipeline.
- **OpenAI GPT-3.5**: Language model for natural language understanding and response generation.

### Functionality Highlights
- **Query Pipeline**: Custom pipeline built with `QueryPipeline` from LlamaIndex to:
  - Parse user queries into Python expressions.
  - Execute expressions on the Titanic dataset.
  - Synthesize user-friendly responses.
- **Code Sanitization**: Ensures safe execution by removing imports and dunder methods from generated code.
- **Dynamic Visualizations**: Generates appropriate plots based on user queries with Matplotlib.

---

## Dataset Information
The Titanic dataset (`tested.csv`) contains information about passengers, including:
- `PassengerId`: Unique ID for each passenger.
- `Survived`: Survival status (0 = No, 1 = Yes).
- `Pclass`: Passenger class (1 = 1st, 2 = 2nd, 3 = 3rd).
- `Name`: Passenger's name.
- `Sex`: Gender of the passenger.
- `Age`: Age of the passenger.
- `Fare`: Fare paid by the passenger.
- `Embarked`: Port of embarkation.

Ensure the dataset is properly preprocessed before use.

---

## Troubleshooting

- **Dataset Issues**:
  - Ensure the `tested.csv` file is in the root directory and formatted correctly.
  - Check for encoding errors if the dataset fails to load.
- **API Key Errors**:
  - Verify the `.env` file contains the correct OpenAI API key.
- **App Crashes**:
  - Review the Streamlit logs for detailed error messages.
  - Check compatibility of Python version and installed packages.

---

## Contribution

We welcome contributions to enhance the functionality of the app. Please:
1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Submit a pull request with detailed explanations.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements
- **OpenAI** for providing the GPT-3.5 language model.
- **Streamlit** for the web application framework.
- **LlamaIndex** for enabling integration with language models.

---

Enjoy exploring the Titanic dataset with this intuitive Q&A app!

