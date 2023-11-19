import logging
import os, sys
from datetime import datetime

#combining the current working directory (os.getcwd()) with the directory name "logs" to create a path where log files might be stored.
LOG_DIR = "logs"
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

#creates a directory named "logs" in the current working directory 
# and if it already exists, it won't throw an error due to the exist_ok=True parameter.
os.makedirs(LOG_DIR, exist_ok=True)

# .log log_2023_
#generates a log filename that includes the current date and time information.
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
fie_name = f"log_{CURRENT_TIME_STAMP}.log"

# output log_2023_-7_3_3_4_5.log

## Create the full path for the log file by joining the directory and filename
log_file_path = os.path.join(LOG_DIR,fie_name )

## Configure the logging module
logging.basicConfig(filename = log_file_path,
                    filemode = "w",
                    format ='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO )


#Explanation of logging.basicConfig() arguments:

#filename: Specifies the file where log messages will be written.
#filemode: Defines the file opening mode ("w" for write mode in this case, which truncates the file if it already exists).
#format: Specifies the format of log messages using placeholders like %(asctime)s for timestamp, %(name)s for logger name, %(levelname)s for log level, etc.
#level: Sets the logging level. In this case, it's set to logging.INFO, which means it will capture log messages at the INFO level or above.

#This file does:
#1.Defines Log Directory Path:
#2.Generates Log File Name:
#3.Sets up Logging Configuration: