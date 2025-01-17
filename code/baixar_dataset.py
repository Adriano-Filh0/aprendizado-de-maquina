from roboflow import Roboflow
rf = Roboflow(api_key="F55eWRWpi2MQsShuOrnO")
project = rf.workspace("fire-extinguisher-detect-ddy5c").project("fire-extinguisher-detect")
version = project.version(1)
dataset = version.download("yolov11")
                
