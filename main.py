from textsummarization.pipeline.data_ingestion_pipeline import DataingestionTrainingPipeline
from textsummarization.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from textsummarization.logging import logger



STAGE_NAME='Data Ingestion Stage'

try:
    logger.info(f'>>>>>  stage {STAGE_NAME} started <<<<<<<')
    data_ingestion=DataingestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME='Data Validation Stage'
try:
    logger.info(f'>>>>>  stage {STAGE_NAME} started <<<<<<<')
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f'>>>>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x')
    
except Exception as e:
    logger.exception(e)
    raise e
