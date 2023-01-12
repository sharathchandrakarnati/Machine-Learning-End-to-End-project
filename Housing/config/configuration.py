
from Housing.entity.config_entity import dataIngentionConfig,dataValidationConfig,DatatransformationConfig,ModelTraningConfig, ModelEvaluationConfig,ModelpushingConfig,TraningPipelineConfig
from Housing.util.util import read_yaml_file 
from Housing.logger import logging
from Housing.constant import *
from Housing.exception import HousingException 
import os,sys


import  os 
Root_DIR = os.getcwd() # to get current working directory 



class Configuration:
    
    def __init__(self, config_file_path:str = CONFIG_FILE_PATH, 
                 current_time_stamp:str = CURRENT_TIME_STAMP) -> None:
        self.config_info = read_yaml_file(file_path = config_file_path)
        self.traning_pipline_config = self.get_traning_pipline_config()
        self.time_stamp = current_time_stamp
        
    def get_data_ingestion_config(self) -> dataIngentionConfig:
        pass
    def get_data_validation_config(self) -> dataValidationConfig:
        pass
    def get_data_transformation_config(self) ->DatatransformationConfig :
        pass
    def get_model_traning_config(self) -> ModelTraningConfig :
        pass
    def get_model_evaluation_config(self)-> ModelEvaluationConfig :
        pass 
    def get_model_pusher_config(self) -> ModelpushingConfig :
        pass
    def get_traning_pipline_config(self) ->TraningPipelineConfig :
        try :
            traning_pipeline_config = self.config_info[Traning_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(Root_DIR, traning_pipeline_config[TRAINING_PIPELINE_NAME_KEY],traning_pipeline_config[Traning_PIPELINE_ARTIFACT_DIR_KEY])
            traning_pipeline_config  = TraningPipelineConfig(artifact_dir= artifact_dir)
            logging.info(f"Traning pipeline config:{traning_pipeline_config}")
            return traning_pipeline_config 
            

             
        except Exception as e:
          raise HousingException(e,sys) from e
             
  
    
    
    