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
  
MLFLOW_TRACKING_URI=https://dagshub.com/fazlullahb/deepCNNClassifier.mlflow \
MLFLOW_TRACKING_USERNAME=fazlullahb \
MLFLOW_TRACKING_PASSWORD=12eadccb6e23e1fd35381edaf52d8dc7e2e1c48d \
python script.py

$ mlflow server \ 
> --backend-store-uri sqlite:///mlflow.db \ 
> --default-artifact-root ./artifacts \ 
> --host 0.0.0.0 -p 1234