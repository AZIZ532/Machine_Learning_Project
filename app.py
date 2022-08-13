#from crypt import methods
import sys
from flask import Flask
from housing.exception import HousingException
from housing.logger import *
import logging
from housing.config.configuration import Configuration

app=Flask(__name__)

@app.route("/",methods = ['POST','GET'])
def index():
    try:
        raise Exception(" we are testing this custom exception")
    except Exception as e:
        raise HousingException(e,sys) from e
        logging.info(housing.error_message)    
        logging.info("we are testing logging module in logger file !")
    return "world"


if __name__=="__main__":
    app.run(debug= True)