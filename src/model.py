import glob
import cloudpickle
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from features import ExtractDateComponents


def load_model() -> Pipeline:
    """
     Load the trained sklearn Pipeline object.

    :return: sklearn Pipeline
    """

    ml_pipeline = cloudpickle.load(open("data/ml_pipeline.joblib", 'rb'))
    return ml_pipeline


def predict_sales(date: str, pipeline: Pipeline) -> dict:
    """
    Predict the sales for the single date given.

    :param date: String Date must have the format ddmmyyyy otherwise and exception.
    :param pipeline: sklearn Pipeline
    :return: dict with key sales: value prediction if successful otherwise messaye
    """

    try:
        prediction = pipeline.predict(pd.DataFrame({"date": pd.to_datetime(date, format="%d%m%Y")},
                                                   index=[0]))[0]
        return {'sales': prediction}
    except ValueError:
        return {'message': 'Invalid date format. Must be ddmmyyyy.'}


def train_model():
    """
    ML pipeline training function added for completes.
    Currently there are no endpoints for training new models or selecting different models for
    prediction, but they can be added.

    :return:
    """

    # parse saved data
    data = pd.read_csv("/usr/data/data_trc.csv")
    data["date"] = pd.to_datetime(data["date"])
    data = data.groupby("date").agg({"sales": "sum"})
    data = data.sort_values("date")
    data = data.reset_index()

    # model input column
    X = data[["date"]]
    # model forecast target column
    y = data["sales"]

    # sklearn pipeline defined by one feature generation step and Random Forest Regressor stepl
    ml_pipeline = Pipeline([("extract_date", ExtractDateComponents()),
                            ("model", RandomForestRegressor())])

    # for consistency, and to improve fit performance, only the last 400 days are used for training
    ml_pipeline.fit(X.iloc[-400:],
                    y=y.iloc[-400:])

    # prevent model overwrite
    num_models = len(glob.glob('/usr/data/ml_pipeline_*'))
    # save
    cloudpickle.dump(ml_pipeline, open(f'/usr/data/ml_pipeline_{num_models}.joblib', 'wb'))
