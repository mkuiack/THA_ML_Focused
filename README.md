# ML Demand Sensing Problem

This is a flask application which forecasts total sales for a given date.




### Requirements:
- Docker

### Usage:

clone this repository cd to the root 
#### 1. Build docker container

```
$ docker build -t forecast_app . 
```
#### 2. Run
```
$ docker run -p 8000:8000  forecast_app
```

This starts a Flask app running in a docker continer exposing port 8000. 

Sales forecasts can be returned by posting GET requests to 
```
localhost:8000/api/predict?date=05102020
```
returns a response with a json body: 
```
{
"sales": 407.64664
}
```

If the date is not in the correct format, it must be ddmmyyyy
then a message is returned:
```
{
'message': 'Invalid date format. Must be ddmmyyyy.'
}
```


#### Structure 

```
|-- data
    |-- data_trc.csv
    |-- ml_pipeline.joblib
    |-- ml_pipeline.pkl
|-- documents
    |-- ML\ THA.pdf
    |-- Mark_kuiack_presentation.pptx
    |-- data_exploration.ipynb
|-- env
|-- requirements.txt
|-- src
    |-- __init__.py
    |-- app.py
    |-- features.py
    |-- model.py
```