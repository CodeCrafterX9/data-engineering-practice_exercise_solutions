import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def main():
    # your code here
    URL = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    TARGET_TIMESTAMP = "2024-01-19 15:45"
    response = requests.get(URL)

    df=pd.read_html(response.text)[0]

    filename = df[df['Last modified']==TARGET_TIMESTAMP].iloc[0,0]

    file_url = URL + filename

    csv_reponse = requests.get(file_url)

    with open(filename,'wb') as f:
        f.write(csv_reponse.content)

    data = pd.read_csv(filename)
    max_bulb_temp = data['HourlyDryBulbTemperature'].max()

    output = data[data['HourlyDryBulbTemperature']==max_bulb_temp]
    print(output)

if __name__ == "__main__":
    main()
