import traceback
import os
from sklearn.externals import joblib


def get(model, model_name, dir_path):
    try:
        pathFile = os.path.join(dir_path, model_name + '.pkl')
        # If the file already exists, load the model
        if os.path.isfile(pathFile):
            model = joblib.load(pathFile)
    except Exception as e:
        traceback.print_tb(e.__traceback__)
    return model


def create(model, model_name, dir_path):
    try:
        joblib.dump(model, os.path.join(dir_path, model_name + '.pkl'))
    except Exception as e:
        traceback.print_tb(e.__traceback__)
