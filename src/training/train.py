# importing all modules
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from src.conf.config import MODEL_FILE_NAME, ENCODER_FILE_NAME, logging


class Train:
    def __init__(self):
        self.data = None
        # Encoding the target variables to integers
        self.numeric_conf = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']

    def data_reprocessing(self, data_file, target_column):


        X = None  # independent variable data(or features)
        y = None  # dependent variable or target variable data

        try:
            self.data = pd.read_csv(data_file)
        except Exception as e:
            print(f"ERROR: File reading is not successful: {e}")
        try:
            label_encoder = LabelEncoder()
            df = self.data.iloc[:, self.data.columns != target_column]
            X = df.select_dtypes(include=self.numeric_conf)
            output = open(ENCODER_FILE_NAME, 'wb')
            y = label_encoder.fit_transform(self.data[target_column])
            pickle.dump(label_encoder, output)
        except Exception as error:
            logging.error(f"Error: {error}")
        else:
            logging.info("Data Pre processing completed without any error")
        finally:
            logging.info("Data Pre-processing stage completed ")
        return X, y

    @staticmethod
    def fit(X, y, C=1.0, kernel='poly', degree=3):
        """
        # C SVM regularization parameter
        # SVC with polynomial (degree 3) kernel
        :param X:
        :param y:
        :param C:
        :param kernel:
        :param degree:
        :return:
        """

        model = SVC(kernel=kernel, degree=degree, C=C).fit(X, y)
        return model

    def save_model(self, model):
        """

        :param
           model: object
           description: it is final model after fit

        :return:
        """
        try:
            with open(MODEL_FILE_NAME, "wb") as output_model:
                pickle.dump(model, output_model)
            pickle.dump(self.model, MODEL_FILE_NAME)
        except Exception as error:
            logging.error(f"Error: {error}")
        else:
            logging.info("Model saved Successfully")

        finally:
            logging.info("Model saving stage completed ")

    def run(self, data_file, target_column):
        """
        Driver method to run all the method for training class
        :param
           data_file: csv file
        :param
            target_column: str
        :return:
             None
        """
        X, y = self.data_reprocessing(data_file, target_column)
        model = self.fit(X, y)
        self.save_model(model)
        return "Success"
