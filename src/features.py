from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class ExtractDateComponents(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return pd.DataFrame({"day_of_year": X["date"].apply(lambda y: y.dayofyear),
                             "day_of_week": X["date"].apply(lambda y: y.dayofweek),
                             "week_of_year": X["date"].apply(lambda y: y.isocalendar().week),
                             "month_of_year": X["date"].apply(lambda y: y.month),
                             "year": X["date"].apply(lambda y: y.year)
                             },
                            index=X.index)
