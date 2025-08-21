import logging

logger_file = logging.getLogger(__name__)
file_handler = logging.FileHandler('logs.log')
logger_file.addHandler(file_handler)
print(logger_file.handlers)
logger_file.warning('Warning message')