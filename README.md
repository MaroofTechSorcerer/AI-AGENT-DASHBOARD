# AI Agent Dashboard

## Project Description
The AI Agent Dashboard is an intelligent tool designed to assist users in extracting valuable insights from data. Users can upload CSV files or connect to Google Sheets to retrieve specific information from a selected column using natural language prompts. The dashboard supports various operations such as calculating the minimum, maximum, average, sum, and count of numeric values.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
3. [Environment Setup](#environment-setup)
4. [Usage Guide](#usage-guide)
    - [Uploading a CSV File](#uploading-a-csv-file)
    - [Connecting to Google Sheets](#connecting-to-google-sheets)
5. [Example Queries](#example-queries)
6. [Sample Dataset](#sample-dataset)
7. [Optional Features](#optional-features)
8. [Loom Video](#loom-video)

## Prerequisites
- Python 3.6 or higher
- Pip (Python package installer)

## Installation
1. **Clone the repository**:
   ```sh
   git clone https://github.com/your-username/AI_AGENT_DASHBOARD.git
   cd AI_AGENT_DASHBOARD
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```sh
   python -m venv myenv
   source myenv/bin/activate  # On Windows: myenv\Scripts\activate
   ```

3. **Install the required libraries**:
   ```sh
   pip install -r requirements.txt
   ```

## Environment Setup
1. **Set up environment variables**:
   - Create a `.env` file in the project directory with the following content:
     ```sh
     GOOGLE_APPLICATION_CREDENTIALS=credentials.json
     ```

2. **Obtain Google Sheets API credentials**:
   - Follow the instructions [here](https://developers.google.com/sheets/api/quickstart/python) to create a project and enable the Google Sheets API.
   - Download the `credentials.json` file and place it in the project directory.

## Usage Guide

### Uploading a CSV File
1. **Upload a CSV File**:
    - Click on "Upload CSV" and select your CSV file.
    - Preview the data and select the column containing numeric values.
    - Enter a custom prompt (e.g., "Get me the minimum value of column X").
    - Click "Extract Information" to see the results.
    - Download the extracted information using the "Download Extracted Information" button.

### Connecting to Google Sheets
1. **Enter Google Sheets Details**:
    - Enter your Google Sheets ID and the data range (e.g., `Sheet1!A1:D10`).
    - Click "Load Google Sheet" to load the data.
    - Preview the data and select the column containing numeric values.
    - Enter a custom prompt (e.g., "Get me the minimum value of column X").
    - Click "Extract Information from Google Sheet" to see the results.
    - Download the extracted information using the "Download Extracted Information" button.

## Example Queries

- "What is the minimum value of the column?"
- "Show me the maximum value in this column."
- "Calculate the average of the column values."
- "What is the total sum of the values in this column?"
- "How many entries are there in this column?"

## Sample Dataset

Here is an example of how your CSV file should look:

| ID | Name  | Age | Salary  |
|----|-------|-----|---------|
| 1  | John  | 28  | 50000   |
| 2  | Jane  | 32  | 60000   |
| 3  | Doe   | 45  | 55000   |
| 4  | Smith | 23  | 45000   |

Use this sample dataset to test the functionalities of the dashboard.

## Optional Features

- **Enhanced Error Handling**: Provides detailed error messages to help troubleshoot issues.
- **Additional Queries Supported**: Supports more advanced queries by extending the `extract_info` function.

## Loom Video
https://www.loom.com/share/419eafe2f26a4af59b2bf347880aa4c9?sid=b9a98e22-1446-408c-9f64-f8e1110ed47d

```
