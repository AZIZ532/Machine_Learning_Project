import logging
from housing.logger import logging
import logging
from housing.config.configuration import Configuration
def main():
    try:
<<<<<<< HEAD
        #pipeline = Pipeline()
        #pipeline.run_pipeline()
        data_validation = Configuration().get_data_transformation_config()
        print(data_validation)
=======
        data_validation_config = Configuration.get_data_validation_config()
        print(data_validation_config)
>>>>>>> 9d2e73f40d08fc29c5b03ed7510500b8250b4d9e
    except Exception as e:
            logging.error(f"{e}")
            print(e)
   



if __name__ =="__main__":
    main()