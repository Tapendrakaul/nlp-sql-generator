import os
import streamlit as st
from langchain.chains import create_sql_query_chain
from langchain_google_genai import GoogleGenerativeAI
from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError
from langchain_community.utilities import SQLDatabase
from dotenv import load_dotenv

class QuestionAnsweringApp:
    def __init__(self):
        load_dotenv()
        self.db_user = "root"
        self.db_password = "Test@1234"
        self.db_host = "localhost"
        self.db_name = "retail_sales_db"
        self.engine = self._create_engine()
        self.db = SQLDatabase(self.engine, sample_rows_in_table_info=3)
        self.llm = GoogleGenerativeAI(
            model="gemini-pro",
            google_api_key=os.getenv("GOOGLE_GEMINI_API_KEY")
        )
        self.chain = create_sql_query_chain(self.llm, self.db)
    
    def _create_engine(self):
        """Create and return the SQLAlchemy engine."""
        return create_engine(
            f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}"
        )
    
    def execute_query(self, question):
        try:
            # Generate SQL query from question
            response = self.chain.invoke({"question": question})

            # Execute the query
            result = self.db.run(response)
            
            return response, result
        except ProgrammingError as e:
            st.error(f"An error occurred: {e}")
            return None, None
    
    def render_app(self):
        """Render the Streamlit application."""
        st.title("Question Answering App")
        question = st.text_input("Enter your question:")

        if st.button("Execute"):
            if question:
                cleaned_query, query_result = self.execute_query(question)
                
                if cleaned_query and query_result is not None:
                    st.write("Generated SQL Query:")
                    st.code(cleaned_query, language="sql")
                    st.write("Query Result:")
                    st.write(query_result)
                else:
                    st.write("No result returned due to an error.")
            else:
                st.write("Please enter a question.")


if __name__ == "__main__":
    app = QuestionAnsweringApp()
    app.render_app()
