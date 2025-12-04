from Network_Security.components.data_ingestion import DataIngestion
from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logging.logger import logging
from Network_Security.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
import sys

if __name__=='__main__':
    try:
        trainingPipelineConfig=TrainingPipelineConfig()
        dataIngestionConfig=DataIngestionConfig(trainingPipelineConfig)
        data_ingestion=DataIngestion(dataIngestionConfig)
        logging.info("Initiate the data Ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)





    except Exception as e:
           raise NetworkSecurityException(e,sys)