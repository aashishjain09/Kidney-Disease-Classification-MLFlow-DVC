# Kidney-Disease-Classification-MLflow-DVC


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/aashishjain09/Kidney-Disease-Classification-MLFlow-DVC
```
### STEP 01- Create a virtual environment after opening the repository

```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)

- [MLflow tutorial](https://youtu.be/qdcHHrsXA48?si=bD5vDS60akNphkem)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI= \
MLFLOW_TRACKING_USERNAME= \
MLFLOW_TRACKING_PASSWORD= \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=

export MLFLOW_TRACKING_USERNAME=

export MLFLOW_TRACKING_PASSWORD=

```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag