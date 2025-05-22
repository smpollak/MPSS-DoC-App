import requests
import pandas as pd
import json
from io import StringIO

def fetch_oecd_data(metric):
    url = f"https://sdmx.oecd.org/public/rest/data/{metric}/all?startPeriod=2000&endPeriod=2025&dimensionAtObservation=AllDimensions&format=csvfilewithlabels"
    response = requests.get(url)
    print(response.status_code)
    # digesting the csv text into a pandas df
    df = pd.read_csv(StringIO(response.text)) #stringio makes it "appear" like a csv to pandas
    df = df[['TIME_PERIOD', 'Reference area', 'REF_AREA', 'Measure','OBS_VALUE']] # selecting columns to keep
    return df

TUD_code = 'OECD.ELS.SAE,DSD_TUD_CBC@DF_TUD,'
CTP_code = 'OECD.CTP.TPS,DSD_TAX_CIT@DF_CIT,1.0/.A..ST..S13+S1311+S13M..'


print(fetch_oecd_data(CTP_code))