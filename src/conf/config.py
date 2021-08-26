import os
import logging


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
INPUT_ARTIFACTS_DIR = os.path.join(BASE_DIR, "src", "artifacts")
MODEL_FILE_NAME = os.path.join(INPUT_ARTIFACTS_DIR, "model.pkl")
ENCODER_FILE_NAME = os.path.join(INPUT_ARTIFACTS_DIR, "encoder.pkl")
LOG_DIR = os.path.join(BASE_DIR, "log")
LOG_FILE_NAME = "app.log"
logging.basicConfig(filename=os.path.join(LOG_DIR, LOG_FILE_NAME), level=logging.DEBUG)
host = "0.0.0.0"
port = 5000
