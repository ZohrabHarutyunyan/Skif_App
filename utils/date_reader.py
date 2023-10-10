import json

def data_reader():
    f = open("../config.json")
    data = json.load(f)
    f.close()
    return data