import os
from datetime import datetime
Root_dir = os.getcwd()
Config_dir = "config"
Config_File_Name = "config.yaml"

CONFIG_FILE_PATH= os.path.join(Root_dir,Config_dir,Config_File_Name)
CURRENT_TIME_STAMP = F"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"



## Traning pipeline related variable 
Traning_PIPELINE_CONFIG_KEY = "training_pipeline_config"
Traning_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"


### Data Ingestion related varieble 

DATA_INGESTION_CONFIG_KEY = "data_ingestion_config" 
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY ="raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"