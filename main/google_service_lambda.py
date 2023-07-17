import gspread

def save_data(event, context):
    gc = gspread.service_account(filename="./service_account.json")

    wks = gc.open("<NAME_OF_YOUR_GOOGLE_SPREADSHEET>").sheet1

    wks.append_row([event["responsePayload"]["date"],
                    event["responsePayload"]["close"]])