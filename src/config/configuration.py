#This file uses the constants defined in constants/__init__.py to create concrete file paths used in the data pipeline.
from src.constants import *
import os, sys

import os

# ROOT_DIR is set to the value of ROOT_DIR_KEY from the constants.
ROOT_DIR = ROOT_DIR_KEY


#DATASET_PATH combines ROOT_DIR, DATA_DIR, and DATA_DIR_KEY to form the full path to the dataset.
DATASET_PATH = os.path.join(ROOT_DIR,DATA_DIR,DATA_DIR_KEY)

# Data ingestion config
#CURRENT_TIME_STAMP in their paths, which means each run of the pipeline will generate data in a unique, timestamped directory.
RAW_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_INGESTION_KEY,CURRENT_TIME_STAMP,
                             DATA_INGESTION_RAW_DATA_DIR,RAW_DATA_DIR_KEY)

TRAIN_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_INGESTION_KEY,CURRENT_TIME_STAMP,
                               DATA_INGESTION_INGESTED_DATA_DIR_KEY,TRAIN_DATA_DIR_KEY)

TEST_FILE_PATH = os.path.join(ROOT_DIR,ARTIFACT_DIR_KEY,DATA_INGESTION_KEY,CURRENT_TIME_STAMP,
                              DATA_INGESTION_INGESTED_DATA_DIR_KEY,TEST_DATA_DIR_KEY)

