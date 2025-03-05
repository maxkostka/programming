import json
import logging

DEFAULT_CONFIG_PATH = "./config.json"
DEFAULT_LOG_FILE = "./meisenkasten.log"

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
rootLogger = logging.getLogger()

fileHandler = logging.FileHandler(DEFAULT_LOG_FILE)
fileHandler.setFormatter(logFormatter)
rootLogger.addHandler(fileHandler)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)

class Meisenkasten():
  def __init__(self, config_path = None):
    if not config_path:
      self._config_path = DEFAULT_CONFIG_PATH
    read_config()

def _read_config(self):
  with open(self._config_path, "r") as config_file:
    self._config = json.read(config_file)

def main():
  logging.debug("main")

if __name__ == "__main__":
    logging.debug("call main")
    main()
  
