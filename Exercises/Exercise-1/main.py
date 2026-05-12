import requests
import os
import zipfile


download_urls = [
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2018_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q2.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q3.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2019_Q4.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2020_Q1.zip",
    "https://divvy-tripdata.s3.amazonaws.com/Divvy_Trips_2220_Q1.zip",
]

downloads_folder = "downloads"
extracted_folder = "extracted"

os.makedirs(downloads_folder,exist_ok=True)
os.makedirs(extracted_folder,exist_ok=True)


def main():
    for url in download_urls:
        #we extract file name from the url
        filename = url.split('/')[-1]
        print(filename)

        #zip path 
        zip_path = os.path.join(downloads_folder, filename)
        print(zip_path)

        reponse = requests.get(url)
        #print(reponse,zip_path)
        print(reponse.status_code)

        with open(zip_path,"wb") as f:
            f.write(reponse.content)

        print(f"Downloaded {zip_path}")

        print(f"Extracting {filename}")

        with zipfile.ZipFile(zip_path,'r') as zip_ref:
            zip_ref.extractall(extracted_folder)

        print(f"Extracted to {extracted_folder}")


if __name__ == "__main__":
    main()
