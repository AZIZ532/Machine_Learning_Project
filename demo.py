import logging
from housing.logger import logging
import logging
from housing.config.configuration import Configuration
def main():
    try:
        #pipeline = Pipeline()
        #pipeline.run_pipeline()
        data_validation = Configuration().get_data_transformation_config()
        print(data_validation)
    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__ =="__main__":
    main()