
from model import load_model, predict_sales
from flask import Flask, request, make_response
from sklearn.pipeline import Pipeline
from typing import Tuple

def create_app() -> Tuple[Flask, Pipeline] :

    # start app
    app = Flask(__name__)

    @app.route("/")
    def root():
        return {"message": "Sales prediction app started."}


    @app.route("/api/predict")
    def predict():

        date = request.args.get('date', None)
        result = predict_sales(date, pipeline)
        return make_response(result)

    # load the saved ML pipeline once an store in memory
    pipeline = load_model()

    return app, pipeline




if __name__ == "__main__":

    app, pipeline  = create_app()
    app.run(port=8000, host='0.0.0.0')
