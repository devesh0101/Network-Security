import os
import sys
import json


# Load environment variables from .env file (mongo db url)
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(f"Mongo DB URL : {MONGO_DB_URL}")

# used for getting the certificate for secure connection
import certifi
CA = certifi.where()

import pandas as pd
import numpy as np
import pymongo

# Import custom exceptions and logger
from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logging.logger import logging

# Data extraction class used to extract data from MongoDB
class NetworkDataExtractor():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    # Class to get data from the csv file in Newtwork data folder and convert it to json format
    def get_data_as_json(self,file_path):
    
        try:
            # reading the csv file  
            df = pd.read_csv(file_path) 
            logging.info(f"CSV file {file_path} read successfully")
            # reset index of dataframe
            df.reset_index(drop=True, inplace=True) 

            # convert dataframe to json records
            json_records = list(json.loads(df.T.to_json()).values())
            logging.info(f"Converted dataframe to json records successfully")
            return json_records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    # Method to insert json records into MongoDB collection
    def insert_data_mongodb(self,database,collection,records):
      
        try:
            # Initialize the database, collection and records
            self.database = database
            self.collection = collection
            self.records = records

            # Create MongoDB client and insert records
            self.mong0_client = pymongo.MongoClient(MONGO_DB_URL)
            self.db = self.mong0_client[self.database]
            self.col = self.db[self.collection] 
            self.col.insert_many(self.records)
            
            return(len(self.records))
        
        except:
        
            raise NetworkSecurityException(e, sys)
        

if __name__ == "__main__":
    file_path = os.path.join("Network_Data/phisingData.csv")
    DATABASE = "NetworkSecurityDB"
    COLLECTION = "PhishingDataCollection"
    networkobj= NetworkDataExtractor()
    records=networkobj.get_data_as_json(file_path)
    print(f"Number of records obtained from csv file: {len(records)}")
    no_of_records = networkobj.insert_data_mongodb(DATABASE,COLLECTION,records)
    print(f"Number of records inserted to MongoDB: {no_of_records}")