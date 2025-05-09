from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation_mlflow import Evaluation
from cnnClassifier import logger

STAGE_NAME = "Model Evaluiation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        training=Evaluation(ConfigurationManager().get_training_config())
        training.get_base_model()
        training.traing_valid_generator()
        training.train()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx================x")
    except Exception as e:
        logger.exception(e)
        raise e