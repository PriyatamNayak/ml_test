import pickle
import numpy as np
from src.conf.config import MODEL_FILE_NAME, ENCODER_FILE_NAME, logging


class Predict:
    """
    class for classification based on inputs
    """
    def __init__(self, model_pickle_path=MODEL_FILE_NAME, encoder_pickle_path=ENCODER_FILE_NAME):
        self.model = pickle.load(open(model_pickle_path, 'rb'))
        self.encoder = pickle.load(open(encoder_pickle_path, 'rb'))

    def classify(self, *args):
        """

        :param
           args: list type
           description: It will content the value of different independent features
        :return:
        """

        arr = np.array(args)  # Convert to numpy array
        arr = arr.astype(np.float64)  # Change the data type to float
        query = arr.reshape(1, -1)   # Reshape the array
        prediction = self.model.predict(query)[0]  # Retrieve from dictionary
        result = self.encoder.inverse_transform([prediction])[0]
        logging.info(f"The prediction for the input{args} is {result}")
        return result  # Return the prediction

