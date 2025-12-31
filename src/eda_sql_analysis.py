import sqlite3
import pandas as pd

def run_queries():
    conn = sqlite3.connect('spacex_database.db')
    df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv")
    df.to_sql('SPACEXTBL', conn, if_exists='replace', index=False)
    
    # Example Task: Success counts
    query = "SELECT Mission_Outcome, COUNT(*) FROM SPACEXTBL GROUP BY Mission_Outcome"
    print(pd.read_sql(query, conn))
    conn.close()

if __name__ == "__main__":
    run_queries()