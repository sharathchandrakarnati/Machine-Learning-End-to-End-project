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