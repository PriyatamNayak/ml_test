import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from src.conf.config import (
    host,
    port)
from src.app.app import app


# Run the Flask server
if __name__ == '__main__':
    app.run(host=host, port=port)


