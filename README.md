# AI Agent Dashboard

## Project Description
This project is an AI-powered dashboard that allows users to upload CSV files or connect to Google Sheets to retrieve specific information from a chosen column using custom prompts. It provides functionalities such as calculating minimum, maximum, average, sum, and count of numeric values in the selected column.

## Setup Instructions

### Prerequisites
1. Python 3.6 or higher
2. Pip (Python package installer)

### Installation Steps
1. **Clone the repository** (if not already):
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

4. **Set up environment variables**:
   - Create a `.env` file in the project directory with the following content:
     ```
     GOOGLE_APPLICATION_CREDENTIALS=credentials.json
     ```

## Usage Guide

### Uploading a CSV File
1. Click on "Upload CSV" and select your file.
2. Preview the data and select the column containing numeric values.
3. Enter a custom prompt (e.g., "Get me the minimum value of column X").
4. Click "Extract Information" to see the results.

### Connecting to Google Sheets
1. Enter your Google Sheets ID and the data range (e.g., `Sheet1!A1:D10`).
2. Click "Load Google Sheet" to load the data.
3. Preview the data and select the column containing numeric values.
4. Enter a custom prompt (e.g., "Get me the minimum value of column X").
5. Click "Extract Information from Google Sheet" to see the results.

## API Keys and Environment Variables

- **Google Sheets API**: Place your `credentials.json` in the project directory and ensure the path is correctly set in the `.env` file.

## Optional Features

- **Enhanced Error Handling**: Detailed error messages to help troubleshoot issues.
- **Additional Queries Supported**: Apart from basic statistics, more advanced queries can be supported by extending the `extract_info` function.

## Example Queries

- "What is the minimum value of the column?"
- "Show me the maximum value in this column."
- "Calculate the average of the column values."
- "What is the total sum of the values in this column?"
- "How many entries are there in this column?"

## Sample Dataset

Here is an example of how your CSV file should look like:

| ID | Name  | Age | Salary  |
|----|-------|-----|---------|
| 1  | John  | 28  | 50000   |
| 2  | Jane  | 32  | 60000   |
| 3  | Doe   | 45  | 55000   |
| 4  | Smith | 23  | 45000   |

Anyone can use this sample dataset to test the various functionalities of the dashboard.

### Steps to Create and Populate the README.md File:
1. **Open your project directory in a code editor (e.g., VSCode).**
2. **Create a new file named `README.md` in the root of your project directory.**
3. **Copy the above content.**
4. **Paste the copied content into the `README.md` file.**
5. **Save the `README.md` file.**

This will ensure that your project has a comprehensive and informative README.md file, which is crucial for documentation and understanding the project setup and usage.
```

Just follow these steps to create and populate the `README.md` file in your project directory. This will make your project well-documented and easy to understand for anyone who reviews it.
