from main import get_data
import gspread

def save_data():
    data = get_data()
    gc = gspread.service_account(filename="./service-account.json")

    wks = gc.open("data_pipeline_tesla_stocks").sheet1

    wks.append_row([data['date'],
                    data['close']])
save_data()