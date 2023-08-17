## Automated Data Pipelines Project

### Project Overview

In this project, I built a data pipeline to gather and analyze stock price data for Tesla from a free Stock API. The pipeline will include steps to retrieve data, store it in a Google Spreadsheet, and create an interactive data visualization using Streamlit. This hands-on project will cover aspects of data retrieval, processing, storage, and presentation.

### Steps to Completion

1. **API Data Retrieval:** Obtain access to the Stock API, request an API Token, and use Python's `urllib3` library to fetch current stock price data for Tesla.

2. **Google Spreadsheet Integration:** Set up a Google Spreadsheet with columns for date and price. Utilize the `gspread` library to write the retrieved data into the spreadsheet.

3. **Data Visualization with Streamlit:** Create an interactive data visualization using Streamlit. Develop a line chart to display the stock price data over time, allowing users to explore trends and patterns.

4. **Automated Data Pipeline:** Implement a serverless data pipeline using AWS Lambda functions and EventBridge. Schedule regular updates to fetch data from the API and update the Google Spreadsheet.

5. **Deploy Streamlit App:** Deploy the Streamlit app to an online platform (Heroku or Streamlit Cloud) to make the data visualization accessible to a wider audience.

### Prerequisites

- Python programming knowledge.
- Familiarity with API interactions using libraries like `urllib3`.
- Basic understanding of Google Spreadsheets and `gspread` library.
- Experience with creating data visualizations using Streamlit.
- Exposure to AWS Lambda functions and EventBridge for building data pipelines.
- Optional: Experience with deploying applications on platforms like Heroku or Streamlit Cloud.

By completing this project, I gained valuable experience in data pipeline development, data retrieval, storage, and visualization. The project also enhanced my understanding of cloud services and serverless computing.
