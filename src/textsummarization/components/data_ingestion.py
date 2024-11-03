import os
import urllib.request as request
import zipfile
from textsummarization.logging import logger
from textsummarization.utils.common import get_size
from textsummarization.entity import dataingestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: dataingestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f'{filename} download! with following info: \n{headers}')
        else:
            logger.info(f'File already exsists of size: {get_size(Path(self.config.local_data_file))}')

    def extract_zip_file(self):

        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file,'r') as file:
            file.extractall(unzip_path)