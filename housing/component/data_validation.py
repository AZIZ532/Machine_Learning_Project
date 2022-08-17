from housing.logger import logging
from housing.entity.config_entity import DataValidationConfig
from housing.exception import HousingException
from housing.entity.config_entity import DataIngestionConfig
import os,sys


class DataValidation:
    
    def __init__(self,data_validation_config = DataValidationConfig,
                 data_ingestion_artifact = DataIngestionConfig) -> None:
        try:
            logging.info(f"{'>>'*20}Data Validation log started.{'<<'*20} ")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            
        except Exception as e:
            raise HousingException(e,sys) from e
        
    
    def is_train_test_exists(self) -> bool:
        try:
            logging.info(f"Checking if train and test data exists")
            is_train_file_exist = False
            is_test_file_exist = False
            
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
            
            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)
            
            is_available = is_train_file_exist and is_test_file_exist
            
            logging.info(f"Train and test data exists : {is_available}")
            
            if not is_available:
                training_file = self.data_ingestion_artifact.train_file_path
                testing_file  = self.data_ingestion_artifact.test_file_path
                message = f"Train and test data not available. [{training_file}] and [{testing_file}]"
                raise Exception (message)
            return is_available
        
        except Exception as e:
            raise HousingException(e,sys) from e 
        
    def validate_data(self) -> bool:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
        
        
        
    def initiate_data_validation(self):
        try:
            self.is_train_test_exists()
            self.validate_data()
                
        except Exception as e:
            raise HousingException(e,sys) from e