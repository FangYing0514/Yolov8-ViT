import os
import numpy as np
import json

def json2txt(path_json, path_txt):
    with open(path_json, 'r', encoding='gb18030') as json_file:
        json_data = json.load(json_file)
        with open(path_txt, 'w+') as txt_file:
            for shape in json_data['shapes']:
                xy = np.array(shape['points'])
                label = str(shape['label'])
                str_xy = ''
                for m, n in xy:
                    str_xy += str(m) + ',' + str(n) + ','
                str_xy += label
                txt_file.writelines(str_xy + "\n")

dir_json = 'ultralytics/bones/labels/'
dir_txt = 'ultralytics/bones/'
if not os.path.exists(dir_txt):
    os.makedirs(dir_txt)
list_json = os.listdir(dir_json)
for cnt, json_name in enumerate(list_json):
    print('cnt=%d, name=%s' % (cnt, json_name))
    path_json = os.path.join(dir_json, json_name)
    path_txt = os.path.join(dir_txt, json_name.replace('.json', '.txt'))
    json2txt(path_json, path_txt)
