import json

def parsing(files_name):
    with open (files_name, "r") as json_file:
        dict = json.load(json_file)
    json_file.close()
    time=dict.get('timeline')
    dict={}
    for i in range (len(time)):
        dict["time_for_frag" + str(i+1)] = time [i]
    print(dict)
    

parsing(r"C:\Users\stud\PycharmProjects\pythonProject\combined_output.json")



