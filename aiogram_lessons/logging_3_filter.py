import logging


#define custom filter
class ErrorLogFilter(logging.Filter):
    #redefine filter method
    def filter(self, record):
        return record.levelname == 'ERROR' and 'важно' in record.msg.lower()

#initialyze logger
logger = logging.getLogger(__name__)
#create stderr handler
stderr_handler = logging.StreamHandler()
#add filter to handler
stderr_handler.addFilter(ErrorLogFilter())
#add handler to logger
logger.addHandler(stderr_handler)

logger.warning('Важно! Это лог с предупреждением!')
logger.error('Важно! Это лог с ошибкой!')
logger.info('Важно! Это лог с уровня INFO!')
logger.error('Это лог с ошибкой!')

class EvenLogFilter(logging.Filter):
    def filter(self, record):
        return not record.i % 2

class CriticalLogFilter(logging.Filter):
    ...

class DebugWarningFilter(logging.Filter):
    ...

logger1 = logging.Logger(__name__)
stderr_handler1 = logging.StreamHandler()
logger1.addFilter(EvenLogFilter())
logger1.addHandler(stderr_handler1)


#с помощью параметра extra можно в словаре передавать дополнительные данные, которые будут доступны у экземпляра класса
# LogRecord в фильтре. Ключи из словаря становятся атрибутами объекта типа LogRecord, по которым доступны значения по
# этим ключам в словаре extra
for i in range(1,7):
    logger1.warning('Важно! Это лог с предупреждением! %d', i, extra={'i': i})