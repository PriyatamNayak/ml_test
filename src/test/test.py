""" Tests """

# pylint: disable=redefined-outer-name
import os
import pytest
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
from src.prediction import predict
from src.training import train

test_dir = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture(scope="module")
def iris():
    """ Module fixture for the IrisDataset class """
    iris_data_file = os.path.join(test_dir, 'test_artifacts', 'iris.csv')
    return iris_data_file


@pytest.fixture(scope="module")
def model_obj():
    """ Module fixture for the IrisDataset class """
    model = predict.Predict(model_pickle_path=os.path.join(test_dir, 'test_artifacts', 'model.pkl'),
                            encoder_pickle_path=os.path.join(test_dir, 'test_artifacts', 'encoder.pkl'))
    return model


def test_prediction_with_positive_values(model_obj):
    """
    Used to test positive values with our trained model
    :return:
    """
    # 5.1,3.5,1.4,0.2,setosa
    # 5.6,3,4.5,1.5,versicolor

    y_preds = model_obj.classify(5.1, 3.5, 1.4, 0.2)
    y_test = "setosa"

    assert y_preds == y_test
    y_preds = model_obj.classify(5.6, 3, 4.5, 1.5)
    y_test = "versicolor"

    assert y_test == y_preds


def test_prediction_with_negative_values(model_obj):
    """
    Used to test negative values with our trained model
    :return:
    """
    X_test = [-2, -4, -6, -8]
    y_test = "setosa"
    y_preds = model_obj.classify(X_test)
    assert y_test == y_preds


def test_train_with_iris_data(iris):
    """
    Used to test positive values with our trained model
    :return:
    """

    result_test = train.Train().run(iris, "Species")
    result_actual = "Success"

    assert result_test == result_actual
