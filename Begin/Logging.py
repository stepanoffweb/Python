import logging
#dir(logging) does not react
#help(logging)
#Create and config logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "C:\\Users\\User\\Python\\Lumberjack.log",
						level = logging.DEBUG, format = LOG_FORMAT)#  filemode = 'w'
#Create a logger without name to evoid some issues, "root logger"
logger = logging.getLogger()

logger.info("Our first message")
logger.info("It's just some inormation message")
logger.debug('Try, Villy, try it!')
logger.warning('I can\'t do it, sorry.')
logger.error('Did you just try to divide by zero?')
logger.critical('You have crushed the entire Internet, congratulations!')
print(logger.level)# It must be lower  for all greater levels can be displayed