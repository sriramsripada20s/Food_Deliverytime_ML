#The constants/__init__.py file defines various constants and functions that are used throughout our project
import os, sys
from datetime import datetime

#whenevr pipeline is runned the timestamp is produced as output. (Generates a timestamp so that we know at which timestamp we have created which output)
def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}"

#Stores the timestamp when the pipeline is run.
CURRENT_TIME_STAMP = get_current_time_stamp()

#The current working directory of the project.
ROOT_DIR_KEY = os.getcwd()
#Paths related to the data directory
DATA_DIR = "Data"
#main data file
DATA_DIR_KEY = "finalTrain.csv"

#Base directory for storing artifacts.
ARTIFACT_DIR_KEY = "Artifact"

#Data Ingestion related variable
DATA_INGESTION_KEY = "data_ingestion"
DATA_INGESTION_RAW_DATA_DIR = "raw_data_dir"
DATA_INGESTION_INGESTED_DATA_DIR_KEY = "ingested_dir"
RAW_DATA_DIR_KEY = "raw.csv"
TRAIN_DATA_DIR_KEY = "train.csv"
TEST_DATA_DIR_KEY = "test.csv"
