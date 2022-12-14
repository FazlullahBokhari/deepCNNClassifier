# deep Classifier project

## workflow

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config.
6. Update the components
7. Update the pipeline
8. Test run pipeline stage
9. run tox for testing your package
10. Update the dvc.yaml
11. run "dvc repro" for running all the stages in pipeline

![](https://github.com/FazlullahBokhari/deepCNNClassifier/blob/main/docs/images/Data%20Ingestion%402x%20(1).png) 
  
Step 1: Set the environment variable | Get it from daghub -> remote tab -> mlflow tab  
MLFLOW_TRACKING_URI=https://dagshub.com/fazlullahb/deepCNNClassifier.mlflow \
MLFLOW_TRACKING_USERNAME=fazlullahb \
MLFLOW_TRACKING_PASSWORD=<> \
python script.py

Step 2: install mlflow 

Step 3: Set remote URI

Ste 4: Use context manager of mlflow to start run and then log metrics, params and model
$ mlflow server \ 
> --backend-store-uri sqlite:///mlflow.db \ 
> --default-artifact-root ./artifacts \ 
> --host 0.0.0.0 -p  

