import inspect
import logging
import os
class LogGen:

    @staticmethod
    def log_gen():
        project_root = os.path.dirname(os.path.abspath(__file__))
        logs_folder = os.path.join(project_root, "Logs")
        logs_file_path = os.path.join(logs_folder, "salesforce.log")
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler(logs_file_path)
        formatter = logging.Formatter(" %(asctime)s : %(levelname)s : %(name)s : %(message)s ", datefmt='%m/%d/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger




