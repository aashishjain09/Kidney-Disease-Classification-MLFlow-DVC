from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_training import Training
from cnnClassifier import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        training=Training(ConfigurationManager().get_training_config())
        training.get_base_model()
        training.traing_valid_generator()
        training.train()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx================x")
    except Exception as e:
        logger.exception(e)
        raise e