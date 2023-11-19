#in order to test our logger file we use log.py 
from flask import Flask
from src.logger import logging

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    logging.info("We are testing our logger file")

    return "Welcome"

if __name__ == "__main__":
    app.run(debug= True)