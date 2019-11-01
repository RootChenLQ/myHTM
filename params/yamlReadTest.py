# -*- coding:utf-8 -*-
import yaml
import os
from nupic.frameworks.opf.model_factory import ModelFactory
'''
_EXAMPLE_DIR = os.path.dirname(os.path.abspath(__file__))  #abspath()为绝对路径   dirname 获取当前文件所在文件夹的路径
_INPUT_FILE_PATH = os.path.join(_EXAMPLE_DIR, os.pardir, "data", "gymdata.csv")  #os.path.join（） #联合两个至以上的位置信息 os.pardir 父目录
_PARAMS_PATH = os.path.join(_EXAMPLE_DIR, os.pardir, "params", "model.yaml")
'''
_EXAMPLE_DIR = os.path.dirname(os.path.abspath(__file__))
_PARAMS_PATH = os.path.join(_EXAMPLE_DIR, "model.yaml")
with open(_PARAMS_PATH, "r") as f:
  modelParams = yaml.safe_load(f)

model = ModelFactory.create(modelParams)
# This tells the model the field to predict.
model.enableInference({'predictedField': 'consumption'})
