import logging
from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
import logging
import sys,os 
from housing.config.configuration import Configuration
def main():
    try:
        data_validation_config = Configuration.get_data_validation_config()
        print(data_validation_config)
    except Exception as e:
            logging.error(f"{e}")
            print(e)
   



if __name__ =="__main__":
    main()