# Question Answering App

This is a Streamlit-based application that generates and executes SQL queries based on user questions. It uses Google Generative AI to generate SQL queries and SQLAlchemy to execute them on a MySQL database.

## Features

- Generate SQL queries from natural language questions.
- Execute the generated SQL queries on a MySQL database.
- Display the generated SQL query and the query results.

## Requirements

- Python 3.11
- Streamlit
- SQLAlchemy
- LangChain
- LangChain Google Generative AI
- Python Dotenv
- MySQL

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/Tapendrakaul/nlp-sql-generator.git
    cd nlp-sql-generator
    ```

2. Create and activate a virtual environment:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your Google API key:

    ```env
    GOOGLE_GEMINI_API_KEY=your_google_api_key
    ```

## Usage

1. Start the Streamlit application:

    ```sh
    streamlit run main.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Enter your question in the text input field and click the "Execute" button.

4. The generated SQL query and the query results will be displayed.

## Project Structure

- `main.py`: The main application file.
- `requirements.txt`: The list of required Python packages.
- `venv/`: The virtual environment directory.

## License

This project is licensed under the MIT License.