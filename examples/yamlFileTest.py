# -*- coding:utf-8 -*-
import yaml
import os
from nupic.frameworks.opf.model_factory import ModelFactory
'''
_EXAMPLE_DIR = os.path.dirname(os.path.abspath(__file__))  #abspath()为绝对路径   dirname 获取当前文件所在文件夹的路径
_INPUT_FILE_PATH = os.path.join(_EXAMPLE_DIR, os.pardir, "data", "gymdata.csv")  #os.path.join（） #联合两个至以上的位置信息 os.pardir 父目录
_PARAMS_PATH = os.path.join(_EXAMPLE_DIR, os.pardir, "params", "model.yaml")
'''
if __name__=="__main__":
    _EXAMPLE_DIR = os.path.dirname(os.path.abspath(__file__))
    _PARAMS_PATH = os.path.join(_EXAMPLE_DIR, os.pardir,"params","model.yaml")
    #yaml 文件的读取
    with open(_PARAMS_PATH, "r") as f:
    modelParams = yaml.safe_load(f)
    # yaml文件保存模型的全部参数,以字典的形式
    print modelParams['modelParams']

    #yaml 文件的写入:将自己创建的字典写入到yaml中
    #列表中的所有成员都开始于相同的缩进级别, 并且使用一个 "- " 作为开头(一个横杠和一个空格):
    test_dic = {
        'encoder':{
            'encoderparams':{
                'version': 1
            }
        },
        'SP': {
            'Shape': 2048,
            'synapses':[ [1,2],[3,4]],
            'permanance':[[0.1,0.3],[0.6,0.9]],
            'permanance_thres': 0.5,
            'boost':[[0.1,0.3],[0.4,0.4]]
        },
        'TM': {
            'Shape':[2048,10],
            'synapses': [[[0.1,0.2,0.3],[0.2,0.3,0.6]]],
            
        }
    }

    OUTPUT_PATH = os.path.join(_EXAMPLE_DIR,"test.yaml")
    with open(OUTPUT_PATH,"w") as f:
        yaml.dump(test_dic,f)



    #写已有的文件到目录中名字为时间和output.yaml
    #比如修改para中的参数，存储到文件中
