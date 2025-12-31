import requests
import pandas as pd

def fetch_data():
    url = "https://api.spacexdata.com/v4/launches/past"
    response = requests.get(url).json()
    df = pd.json_normalize(response)
    df = df[df['rocket'] == '5e9d0d95eda69973a809d1ec'] # Filter Falcon 9
    df.to_csv('data/dataset_part_1.csv', index=False)
    print("Data saved to data/dataset_part_1.csv")

if __name__ == "__main__":
    fetch_data()