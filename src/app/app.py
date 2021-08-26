from flask import (
    Flask,
    jsonify,
    request,
    Response,
)
from http import HTTPStatus
from src.training.train import Train
from src.prediction.predict import Predict
from src.conf.config import (
    logging,
    host,
    port)

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify("The API server is up and running")


# Route 'create' accepts POST request
@app.route('/create', methods=['POST'])
def create_model():
    try:
        if request.method == 'POST':
            input_file = request.files.get('csv_file', None)
            target = request.args.get('target', None)
            if input_file is None:
                return jsonify("""ERROR: Please check 'csv_file' form parameter should contains values or use double 
                quotes like:  "csv_file=@iris.csv"  instead of single quote  """)
            if target is None:
                return jsonify("Please provide the target")

            Train().run(input_file, target)
            return Response('', status=HTTPStatus.OK, mimetype='application/json')
    except Exception as err:
        logging.error(f"Error: {err}")
        return Response(f"{err}", status=HTTPStatus.UNPROCESSABLE_ENTITY, mimetype='application/json')


# Route 'predict' accepts POST request
@app.route('/predict', methods=['POST'])
def classify():
    try:
        if request.method == 'POST':
            input_params = request.form.get('input_line', None)
            if input_params is None:
                return jsonify("""ERROR: Please check 'input_line' form parameter should contains values or use double 
                quotes like:  "input_line=5.1,3.5,1.4,0.2"  instead of single quote""")
            try:
                load_model_obj = Predict()
            except Exception as err:
                logging.error(f"Error: {err}")
                return Response("Not Found", status=HTTPStatus.NOT_FOUND, mimetype='application/json')
            result = load_model_obj.classify(input_params.split(","))
            return Response(result, status=HTTPStatus.OK, mimetype='application/json')
    except Exception as err:
        logging.error(f"Error: {err}")
        return Response(f"{err}", status=HTTPStatus.UNPROCESSABLE_ENTITY, mimetype='application/json')


# Run the Flask server
if __name__ == '__main__':
    app.run(host=host, port=port)
