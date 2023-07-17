import gspread
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def get_data():
    # Authenticate with Google Sheets API
    gc = gspread.service_account(filename='./service-account.json')

    # Open the spreadsheet
    spreadsheet = gc.open('data_pipeline_tesla_stocks')

    # Select the worksheet
    worksheet = spreadsheet.sheet1

    # Get all values from the worksheet as a list of lists
    data = worksheet.get_all_values()

    # Create a pandas DataFrame from the data
    df = pd.DataFrame(data[1:], columns=data[0])

    return df

def main():
    # Get data from the Google Spreadsheet
    df = get_data()

    # Set up Streamlit
    st.title('Data Visualization with Streamlit')
    st.write(df)  # Display the data as a table

    # Display the line chart
    st.subheader('Line Chart')
    plt.plot(df['date'], df['close'])
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    st.pyplot()

if __name__ == '__main__':
    main()