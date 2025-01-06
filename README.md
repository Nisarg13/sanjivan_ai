# **Titanic Dataset Q&A Chatbot**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sanjivanai.streamlit.app/)

This project provides an interactive Q&A chatbot for exploring and analyzing the Titanic dataset. Users can input natural language queries, and the app dynamically generates Python code to process the dataset and visualize results in real-time.

---

## **Features**
- **Natural Language Interface**: Ask questions about the Titanic dataset in plain English.
- **Dynamic Python Code Generation**: Utilizes OpenAI GPT-3.5-Turbo to generate Python code for data analysis.
- **Real-time Execution**: Displays data processing results or visualizations instantly.
- **Interactive Design**: Built with Streamlit for a seamless user experience.
- **Secure and Robust**: Code sanitization ensures safe execution of generated scripts.

---

## **Quick Links**
- **GitHub Repository**: [Nisarg13/sanjivan_ai](https://github.com/Nisarg13/sanjivan_ai)
- **Streamlit App**: [sanjivanai.streamlit.app](https://sanjivanai.streamlit.app/)

---

## **Requirements**
- Python 3.8 or higher
- Required Python libraries:
  - `streamlit`
  - `langchain`
  - `openai`
  - `pandas`
  - `matplotlib`
  - `python-dotenv`

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/Nisarg13/sanjivan_ai.git
cd sanjivan_ai
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Add Your OpenAI API Key**
- Create a `.env` file in the project root directory:
  ```plaintext
  OPENAI_API_KEY=your_openai_api_key
  ```
- Replace `your_openai_api_key` with your actual OpenAI API key.

### **5. Add the Titanic Dataset**
- Save the Titanic dataset as `tested.csv` in the root directory of the project.

### **6. Run the Streamlit App**
```bash
streamlit run app.py
```

### **7. Open the App**
- Open your browser and navigate to the local URL provided by Streamlit (e.g., `http://localhost:8501`).
- Alternatively, access the hosted app here: [https://sanjivanai.streamlit.app](https://sanjivanai.streamlit.app).

---

## **Usage**
1. **Ask Questions**: Type queries like:
   - "What is the average age of passengers?"
   - "Plot the survival rate by gender."
   - "Show the total number of passengers by embarkation port."
2. **View Results**:
   - Data processing outputs appear as tables.
   - Visualizations (e.g., plots) are displayed dynamically.

---

## **Project Workflow**

### **Dataset Handling**
- The Titanic dataset (`tested.csv`) is preprocessed:
  - Invalid or missing values in key columns (e.g., `Age`, `Embarked`, `Fare`) are handled gracefully.
  - Converts `Age` to numeric, filling errors with defaults.

### **Natural Language to Python Code**
- User queries are passed to OpenAI GPT-3.5-Turbo through LangChain.
- A structured prompt helps generate relevant Python code for:
  - Data filtering and aggregation.
  - Visualization using Matplotlib.

### **Execution and Results**
- Generated code is sanitized to ensure security.
- The sanitized code is executed on the dataset.
- Results (tables or plots) are displayed interactively.

---

## **Limitations**
- Relies on a well-structured Titanic dataset in `tested.csv`.
- The accuracy of generated Python code depends on the prompt and GPT model's response.
- Multi-turn conversations or complex queries are not yet supported.

---

## **Future Enhancements**
- Enable support for multi-turn conversations.
- Expand compatibility with additional datasets.
- Add advanced query debugging and logging features.

---

## **Contributing**
We welcome contributions! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## **Contact**
- **Email**: nisargganatra13@gmail.com
- **GitHub**: [Nisarg13](https://github.com/Nisarg13)

---

## **License**
This project is licensed under the [MIT License](LICENSE).

---

**Enjoy exploring the Titanic dataset with your personalized chatbot!**
