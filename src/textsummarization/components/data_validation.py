import os
from textsummarization.logging import logger
from textsummarization.config.congifuration import DataValidationConfig

class DataValidation:
    def __init__(self,config: DataValidationConfig):
        self.config= config

    
    def validate_all_file_exist(self) -> bool:

        try:
            validation_status=None
            
            all_file=os.listdir(os.path.join('artifacts','data_ingestion','samsum_dataset'))

            for file in all_file:
                if file not in self.config.ALL_REQUIRED_FILE:
                    validation_status=False

                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f'Validation_status: {validation_status}')
                
                else:

                    validation_status=True

                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f'Validation_status: {validation_status}')
                
            return validation_status
        except Exception as e:
            raise e