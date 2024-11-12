import streamlit as st
import pandas as pd
from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import spacy

# Loading environment variables
load_dotenv()

# Google Sheets API setup
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def get_google_sheet(spreadsheet_id, range_name):
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])
    if not values:
        return pd.DataFrame()
    return pd.DataFrame(values[1:], columns=values[0])

def extract_info(df, column, prompt):
    try:
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(prompt)
        prompt = prompt.lower()
        if "minimum" in prompt or "lowest" in prompt:
            result = df[column].astype(float).min()
            return f"The minimum value in column '{column}' is {result}."
        elif "maximum" in prompt or "highest" in prompt:
            result = df[column].astype(float).max()
            return f"The maximum value in column '{column}' is {result}."
        elif "average" in prompt or "mean" in prompt:
            result = df[column].astype(float).mean()
            return f"The average value in column '{column}' is {result}."
        elif "sum" in prompt or "total" in prompt:
            result = df[column].astype(float).sum()
            return f"The sum of values in column '{column}' is {result}."
        elif "count" in prompt or "number of" in prompt:
            result = df[column].count()
            return f"The count of values in column '{column}' is {result}."
        elif "median" in prompt:
            result = df[column].astype(float).median()
            return f"The median value in column '{column}' is {result}."
        elif "standard deviation" in prompt or "std dev" in prompt:
            result = df[column].astype(float).std()
            return f"The standard deviation of values in column '{column}' is {result}."
        elif "variance" in prompt:
            result = df[column].astype(float).var()
            return f"The variance of values in column '{column}' is {result}."
        else:
            return "Query not supported. Please rephrase your query to include 'minimum', 'maximum', 'average', 'sum', 'count', 'median', 'standard deviation', or 'variance'."
    except Exception as e:
        return f"Error: {e}"

def main():
    st.title("AI Agent Dashboard")

    st.write("This dashboard allows you to upload CSV files or connect to Google Sheets, and extract information using natural language queries.")
    
    # File uploading section
    st.header("Upload CSV")
    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded Data Preview:")
        st.write(df.head())
        if not df.empty:
            columns = df.columns.tolist()
            selected_column = st.selectbox("Select the column with numeric values", columns)
            query = st.text_input("Enter your custom prompt (e.g., 'Get me the minimum value of column X'):")
            if st.button("Extract Information"):
                extracted_info = extract_info(df, selected_column, query)
                st.write({"Extracted Info": extracted_info})

    # Google Sheets connection section
    st.header("Connect to Google Sheets")
    spreadsheet_id = st.text_input("Enter Google Sheets ID")
    range_name = st.text_input("Enter data range (e.g., Sheet1!A1:D10)")

    if st.button("Load Google Sheet"):
        df = get_google_sheet(spreadsheet_id, range_name)
        if df.empty:
            st.error("No data found.")
        else:
            st.write("Google Sheet Data Preview:")
            st.write(df.head())
            columns = df.columns.tolist()
            selected_column = st.selectbox("Select the column with numeric values", columns)
            query = st.text_input("Enter your custom prompt (e.g., 'Get me the minimum value of column X'):")
            if st.button("Extract Information from Google Sheet"):
                extracted_info = extract_info(df, selected_column, query)
                st.write({"Extracted Info": extracted_info})

if __name__ == "__main__":
    main()
