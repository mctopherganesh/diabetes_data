import json
import datetime




def make_datestamp():
    
    return datetime.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')


def create_bs_obj(datestamp,new_obj):
    
    data = {datestamp : new_obj}

    return data

def loads_json_file():
    with open('data.json') as json_file:
        data = json.load(json_file)
        return data

def append_object(obj,json_file_obj):
    json_file_obj.append(obj)
    return json_file_obj


def write_to_file(appended_json):

    with open('data.json', 'w') as outfile:
        json.dump(json_file_obj, outfile)

def write_new_data(bs_score):
    
    json_file = loads_json_file()
    new_json_data = create_bs_obj(make_datestamp(), bs_score)
    json_file = append_object(new_json_data, json_file)
    write_to_file(json_file)
