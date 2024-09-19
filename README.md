***Text-to-SQL GENAI Model***
This project demonstrates a Text-to-SQL Generative AI application that allows users to input human-readable text prompts and generates corresponding SQL queries. The application also retrieves relevant data from an SQLite3 database based on the generated SQL query.

The core functionality is powered by Google Generative AI (GenAI) for natural language understanding and query generation, SQLite3 for database operations, and Streamlit for the front-end web interface.

***Features***
Human-readable to SQL query generation: Convert natural language inputs into SQL queries.
Database integration: Run the generated SQL queries against an SQLite3 database and retrieve the relevant data.
Streamlit UI: A simple, interactive web application for user input and displaying results.
Google Generative AI: Utilizes Google’s advanced AI models for accurate query generation.

***Prerequisites***
Before running the project, ensure you have the following installed on your machine:
Python 3.7+
SQLite3
Streamlit
Google Generative AI SDK/Tools (via API or relevant Google AI model)


***Usage***
Text Input: Enter a human-readable query in the input box. For example:

"Show me all employees who joined after 2020."
"What are the total sales in June?"
SQL Generation: The model converts the prompt into a SQL query.

Data Retrieval: The generated SQL is executed on the SQLite3 database, and the results are displayed in the app.
