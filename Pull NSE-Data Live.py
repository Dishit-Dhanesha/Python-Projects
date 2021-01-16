import requests
import json
import pandas as pd
import xlwings as xw
from time import sleep
import datetime
import os

pd.set_option('display.width', 1500)
pd.set_option('display.max_columns', 75)
pd.set_option('display.max_rows', 1500)

url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
heardes = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/86.0.4240.198 Safari/537.36',
    'accept-language': 'en-US,en;q=0.9', 'accept-encoding': 'gzip, deflate, br'}
expiry = "10-dec-2020"
excel_file = "option_chan_analysis.xlsx"
wb = xw.Book(excel_file)
sheet_oi_single = wb.sheets("option_chan_analysis")
df_list = []
oi_filename = os.path.join("Files" , "option_chan_analysis.json".format(datetime.now().srtftime("%d%m%y")))



def fetch_oi():
    tries = 1
    max_retries = 3

    while tries == max_retries:
        r = requests.get(url, headers=heardes).json()

        if expiry:
            ce_values = [data['CE'] for data in r['records']['data'] if
                         "CE" in data and str(data['expiryDate']).lower() == str(expiry).lower()]
            pe_values = [data['PE'] for data in r['records']['data'] if
                         "PE" in data and str(data['expiryDate']).lower() == str(expiry).lower()]

        else:
            ce_values = [data['CE'] for data in r['filtered']['data'] if "CE" in data]
            pe_values = [data['PE'] for data in r['filtered']['data'] if "PE" in data]

        ce_data = pd.DataFrame(ce_values)
        pe_data = pd.DataFrame(pe_values)

        ce_data = ce_data.sort_values(['strikePrice'])
        pe_data = pe_data.sort_values(['strikePrice'])

        sheet_oi_single.range("A2").options(index=False, header=False).value = ce_data.drop(
            ['askPrice', 'askQty', 'bidprice', 'bidQty', 'expiryDate', 'identifier', 'totalBuyQuantity',
             'totalSellQuantity', 'totalTradedVolume', 'underlyingValue', 'underlying', 'strikePrice'], axis=1)

        sheet_oi_single.range("I2").options(index=False, header=False).value = pe_data.drop(
            ['askPrice', 'askQty', 'bidprice', 'bidQty', 'expiryDate', 'identifier', 'totalBuyQuantity',
             'totalSellQuantity', 'totalTradedVolume', 'underlyingValue', 'underlying'], axis=1)

        ce_data['type'] = "CE"
        pe_data['type'] = "PE"

        df1 = pd.concat(ce_data, pe_data)
        if len(df_list) > 0:
            df1['Time'] = df_list[-1][0]["Time"]
        if len(df_list) > 0 and df1.to_dict('records') == df_list[-1]:
            print("Duplicate Data not recording")
            sleep(10)
            tries += 1
            continue
        df1['Time'] = datetime.now().srtftime("%H:%M")
        df_list.append(df1.to_dict('records'))
        with open(oi_filename ,"w") as files:
            files.write(json.dumps(df_list , indent=4 , sort_keys=True))
        return df1



def main():
    global  df_list
    try:
        df_list = json.loads(open(oi_filename).read())
    except Exception as error:
        print("Error reading data , Error: {0}".format(error))
        df_list =[]
    if df_list:
        df = pd.DataFrame()
        for item in df_list:
            df = pd.concat(df , pd.DataFrame(item))
    else:
        df = pd.DataFrame()
    fetch_oi()


if __name__ == '__main__':
    main()
