# Logging 

from logging import *

LOG_FORMAT = '{lineno} *** {name} *** {asctime} *** {message}'
basicConfig(filename='logfile.log', level=DEBUG, filemode='w', style='{' , format=LOG_FORMAT)

logger = getLogger('Guru')

logger.debug("This is Debug")
logger.info("This is Info")
logger.warning("This is Warning")
error("This is Error")
critical("This is Critical")