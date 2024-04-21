from dotenv import load_dotenv
load_dotenv() #load all env vars

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

#Configuring API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#function to load google gemini model and provide sql query as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text


#Function to retrieve query from sql database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

#Defining my prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The Sql database has the name loan_db and has the following columns -  loan_id, no_of_dependents, 
    education, self_employed, income_annum, loan_amount, loan_term, cibil_score, 
    residential_assets_value, commercial_assets_value, luxury_assets_value, bank_asset_value and loan_status
    \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM loan_db ;
    \nExample 2 - Tell me all the people who are graduates?, 
    the SQL command will be something like this SELECT * FROM loan_db where education="Graduate"; 
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

#Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App to Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")


#if submit is clicked 
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"loan_db.db")
    st.subheader("The response is")
    for row in data:
        print(row)
        st.header(row)

