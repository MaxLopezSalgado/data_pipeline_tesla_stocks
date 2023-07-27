import gspread
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from datetime import datetime
import json

# Access the Google service account credentials from secrets
google_client_email = st.secrets["google_auth"]["client_email"]
google_private_key = json.loads(st.secrets["google_auth"]["private_key"])

# Define the get_data() function to fetch the values from your Google Spreadsheet.

def get_data():
    # Authenticate with Google Sheets API
    gc = gspread.service_account(google_client_email=google_client_email,
                                 google_private_key=google_private_key)

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

    # Convert the 'date' column to a datetime format
    df['date'] = pd.to_datetime(df['date'], format='%Y/%m/%d')

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

    # Set the y-axis ticker to display at regular intervals (e.g., every $10)
    ax.yaxis.set_major_locator(ticker.MultipleLocator(base=10))

    # Format the x-axis labels to display only the month name
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b'))

    # Set the interval for displaying x-axis labels (e.g., every 1 month)
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))

    # Rotate the x-axis labels for better readability
    plt.xticks(rotation=45)

    # Pass the figure (fig) to st.pyplot()
    st.pyplot(fig)

if __name__ == '__main__':
    main()
