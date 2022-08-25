
import sys
from flask import Flask
from housing.exception import HousingException
from housing.logger import logging
import logging
from housing.config.configuration import Configuration

app=Flask(__name__)

@app.route("/",methods = ['POST','GET'])
def index():
    try:
        data_validation_config = Configuration.get_data_validation_config()
        print(data_validation_config)
    except Exception as e:
            logging.error(f"{e}")
            print(e)
   


if __name__=="__main__":
    app.run(debug= True)