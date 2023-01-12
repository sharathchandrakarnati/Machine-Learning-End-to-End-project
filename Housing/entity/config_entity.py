from collections import namedtuple
   
   
   

dataIngentionConfig = namedtuple("dataIngentionConfig",["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])  
dataValidationConfig = namedtuple("DataValidationConfig",['schema_file_path'])
DatatransformationConfig = namedtuple("Data_transformationConfig",["add_bedroom_per_room","transformed_traindir","transformed_test_dir","preprocessed_object_file_path"])
ModelTraningConfig = namedtuple("MModelTraningConfig",["trained_model_file_path","base_accuracy"])
ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",['model_evaluation_file_path',"time_stamp"]) 
ModelpushingConfig = namedtuple("ModelpushingConfig",['export_dir_path'])
TraningPipelineConfig = namedtuple("TraningPipelineConfig",["artifact_dir"])
