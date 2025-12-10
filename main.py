from Network_Security.components.data_ingestion import DataIngestion
from Network_Security.components.data_validation import DataValidation
from Network_Security.components.data_transformation import DataTransformation
from Network_Security.exception.exception import NetworkSecurityException
from Network_Security.logging.logger import logging
from Network_Security.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig,DataValidationConfig,DataTransformationConfig
import sys


from Network_Security.components.model_trainer import ModelTrainer
from Network_Security.entity.config_entity import ModelTrainerConfig

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
        logging.info("Initiate the data Transformation")
        data_tranformation_config = DataTransformationConfig(trainingPipelineConfig)
        data_transformation = DataTransformation(data_validation_artifact,data_tranformation_config) 
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation completed")  
        print(data_transformation_artifact)

        logging.info("Model Training sstared")
        model_trainer_config=ModelTrainerConfig(trainingPipelineConfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logging.info("Model Training artifact created")

    

    except Exception as e:
           raise NetworkSecurityException(e,sys)