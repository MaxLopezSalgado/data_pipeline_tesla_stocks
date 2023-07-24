import gspread
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json
import os

# Define the get_data() function to fetch the values from your Google Spreadsheet.

# def get_data():
#     # Authenticate with Google Sheets API
#     gc = gspread.service_account(filename='./service-account.json')

#     # Open the spreadsheet
#     spreadsheet = gc.open('data_pipeline_tesla_stocks')

#     # Select the worksheet
#     worksheet = spreadsheet.sheet1

#     # Get all values from the worksheet as a list of lists
#     data = worksheet.get_all_values()

#     # Create a pandas DataFrame from the data
#     df = pd.DataFrame(data[1:], columns=data[0])

#     return df


# Define the get_data() function to fetch the values from your Google Spreadsheet.


def get_data():
    # Get the JSON content from the environment variable
    json_str = os.environ.get("GOOGLE_SERVICE_ACCOUNT")

    # Load the JSON content as a dictionary
    service_account_info = json.loads(json_str)

    # Authenticate with Google Sheets API using the loaded service account info
    gc = gspread.service_account_from_dict(service_account_info)

    # Open the spreadsheet
    spreadsheet = gc.open('data_pipeline_tesla_stocks')

    # Select the worksheet
    worksheet = spreadsheet.sheet1

    # Get all values from the worksheet as a list of lists
    data = worksheet.get_all_values()

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data[1:], columns=data[0])

    return df


# Create the Streamlit app and define the main code to display the line chart

def main():
    # Get data from the Google Spreadsheet
    df = get_data()

    # Set up Streamlit
    st.title('Data Visualization with Streamlit')
    st.write(df)  # Display the data as a table

    # Display the line chart
    st.subheader('Line Chart')
   
   # Create the figure and axes objects
    fig, ax = plt.subplots()

    # Plot the data using the axes object (ax)
    ax.plot(df['date'], df['close'])
    ax.set_xlabel('Date')
    ax.set_ylabel('Close Price')

    # Pass the figure (fig) to st.pyplot()
    st.pyplot(fig)

if __name__ == '__main__':
    main()