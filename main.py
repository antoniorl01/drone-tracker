import logging
import sys
import droneapp.controllers.server
import config

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

if __name__ == '__main__':
    droneapp.controllers.server.run()