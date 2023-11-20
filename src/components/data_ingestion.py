from src.constants import *
from src.config.configuration import *
import os,sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException

#It holds paths for raw, train, and test data. 
@dataclass
class DataIngestionconfig:
    train_data_path:str=TRAIN_FILE_PATH
    test_data_path:str=TEST_FILE_PATH
    raw_data_path:str= RAW_FILE_PATH

#The DataIngestion class initializes an instance of DataIngestionConfig, which contains the file paths needed for the data ingestion process.
class DataIngestion:
    def __init__(self):
        self.data_ingestion_config=DataIngestionconfig()

    #The initiate_data_ingestion method initiates the data ingestion process, logs the start of the process, and continues with data operations.
    def initiate_data_ingestion(self):
        # Start of data ingestion process
        logging.info("="*50)
        logging.info("Initiate Data Ingestion config")
        logging.info("="*50)

        try:
            # Reading data from the dataset path
            df=pd.read_csv(DATASET_PATH)
            #df=pd.read_csv(os.path.join("D:\DATASET\delivery_dataset\finalTrain.csv"))
            logging.info(f"Download data {DATASET_PATH}")

            logging.info('Dataset read as pandas Dataframe')

            # raw data folder created (if it doesot exist) and Saving the raw data
            os.makedirs(os.path.dirname(self.data_ingestion_config.raw_data_path),exist_ok=True)  
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False)   

            # Splitting data into train and test sets
            logging.info("train test split")
            train_set,test_Set = train_test_split(df,test_size=0.20,random_state=42)

            # train data folder created and saving the train data
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)
            train_set.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)

            logging.info(f"train data path, {TRAIN_FILE_PATH}")

            # test data folder created and Saving the test data
            os.makedirs(os.path.dirname(self.data_ingestion_config.test_data_path),exist_ok=True)
            test_Set.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)

            logging.info(f"test data path, {TEST_FILE_PATH}")

            # Completing the data ingestion process
            logging.info("data ingestion complete")

            # Returning the file paths of the train and test data
            return(
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )

        # Handling exceptions during data ingestion
        except Exception as e:
            logging.info('Exception occured at Data Ingestion stage')
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.iniitiate_data_ingestion()
