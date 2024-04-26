# Streamlit_Application
## SQL Data Retrieval Streamlit App
# Overview
This application utilizes a Gemini model to interpret natural language queries and convert them into SQL queries. It then executes these queries against a SQLite database called loan_db which is the one I submited initialy for my dataset and displays the results.

# Installation
To run this application, you'll need to install the required dependencies. You can do this by running:
pip install -r requirements.txt
The dependencies are streamlit, google-generativeai, and python-dotenv.

# Setup
Ensure you have the .env file with your GOOGLE_API_KEY configured.
Place the loan_db.csv file in your desired directory and update the paths in sql.py accordingly.
Running the App
To start the app, navigate to the app's directory and run:
streamlit run app.py
The app will be hosted locally and can be accessed through a web browser.

# Usage
Enter your natural language query in the input box and click "Ask the question". The Gemini model will generate the SQL query, which will be executed against the loan_db database.

