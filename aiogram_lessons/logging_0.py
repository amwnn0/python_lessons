import logging
import sys

logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s]  #%(levelname)-8s %(filename)s:'
                                                '%(lineno)d - %(name)s - %(message)s')

# logging.info('Info message')
# logging.debug('Debug message')
# logging.warning('Warning message')
# logging.error('Error message')
# logging.critical('Critical message')

logger = logging.getLogger(__name__)
print(logger)

# logger.debug('Debug message')
# logger.warning('Warning message')
# logger.error('Error message')
# logger.critical('Critical message')

format1 = '#%(levelname)-8s [%(asctime)s] - %(filename)s:'\
           '%(lineno)d - %(name)s - %(message)s'
format2 = '[{asctime}] #{levelname:8} {filename}:'\
           '{lineno} - {name} - {message}'

formatter1 = logging.Formatter(fmt=format1)
formatter2 = logging.Formatter(fmt=format2, style='{')

print(logger.handlers)

stderr_handler = logging.StreamHandler()
stdout_handler = logging.StreamHandler(stream=sys.stdout)
logger.addHandler(stderr_handler)
logger.addHandler(stdout_handler)

print(logger.handlers)

logger.warning('Warning message')