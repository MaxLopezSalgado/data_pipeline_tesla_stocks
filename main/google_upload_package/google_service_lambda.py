import gspread

def save_data():
    gc = gspread.service_account(filename="./service-account.json")

    wks = gc.open("data_pipeline_tesla_stocks").sheet1

    wks.append_row([event["responsePayload"]["date"],
                    event["responsePayload"]["close"]])