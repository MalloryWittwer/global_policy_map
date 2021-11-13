import gspread
from oauth2client.service_account import ServiceAccountCredentials
import csv

def fetch_data():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("Climate Law Scrapers Tracking Sheet").sheet1
    list_of_hashes = sheet.get_all_records()

    with open('data/data_gcl.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Country', 'Assigned to', 'Status'])
        for h in list_of_hashes:
            if not h['Country']:
                break
            country = h['Country']
            volunteer = h['Assigned to']
            status = h['Status']
            writer.writerow([country, volunteer, status])
    print('Fetched data as CSV from Google Sheets!')

if __name__ == '__main__':
    fetch_data()