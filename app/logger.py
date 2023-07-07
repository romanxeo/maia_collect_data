import logging

Logger = logging.getLogger(__name__)
Logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logger.info')

formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
file_handler.setFormatter(formatter)
Logger.addHandler(file_handler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)
Logger.addHandler(consoleHandler)