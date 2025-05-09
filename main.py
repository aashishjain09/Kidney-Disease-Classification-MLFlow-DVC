from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e

##################################################################################################
STAGE_NAME = "Prepare Base Model Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e

##################################################################################################
STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e

##################################################################################################
STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e

# COMMANDS TO PUT IN CMD PROMPT OF THE FOLDER AFTER ADDING DVC AND MODEL
"""
    - FIRST DELETE ARTIFACTS if you are running for first time
    
    dvc init
    dvc repro
    
    - To see the pipeline graph
    
    dvc dag

    - After saving the evaluation into MLFlow (DAGS) and restarting a session | Session = new terminal + new evaluation

    export MLFLOW_TRACKING_URI = ""
    export MLFLOW_TRACKING_USERNAME = ""
    export MLFLOW_TRACKING_PASSWORD = ""

"""