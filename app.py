from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os 
import sqlite3      
import google.generativeai as genai


#COnfig our api key

genai.configure(api_key = os.getenv("Google_Api_key"))



def get_gemini_response(question,prompt):
    # Create a client
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])

    return response.text


#Function to retrieve query from the sql data base 

def read_sql_query(sql,db):
    conn  = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()  
    conn.close()
    for row in rows:
        print(row)
    return rows


prompt = ["""
        You are an expert in converting English questions to SQL query! The SQL Database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, MARKS 
          \n\n For example, How many entries of records are present? \n \n also the sql code should not have ''' in beginning or end and sql word in output.

"""]


#Streamlit APP
st.set_page_config(page_title="I can Retrieve any SQL query")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input",key="input")


submit = st.button("Ask the Question")


if submit:
    response = get_gemini_response(question,prompt)
    print(response)

    data = read_sql_query(response,"student.db")
    st.subheader("The Response is ")

    for row in data:
        print(row)
        st.header(row)