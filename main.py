from Network_Security.components.data_ingestion import DataIngestion
from Network_Security.components.data_validation import DataValidation
from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logging.logger import logging
from Network_Security.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataValidationConfig
import sys

if __name__=='__main__':
    try:
        trainingPipelineConfig=TrainingPipelineConfig()
        dataIngestionConfig=DataIngestionConfig(trainingPipelineConfig)
        data_ingestion=DataIngestion(dataIngestionConfig)
        logging.info("Initiate the data Ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion completed")  
        print(dataingestionartifact)  
        data_validation_config =DataValidationConfig(trainingPipelineConfig)
        data_validation = DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data Validation completed")  
        print(data_validation_artifact)

    

    except Exception as e:
           raise NetworkSecurityException(e,sys)