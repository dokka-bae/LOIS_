import file_reader
def parsing(iteration : int = 0):
    data = {
        'values': [],
        'functions': []
    }
    row = file_reader.read_file(f".\\tests\\{iteration+1}")
    for item in row['values']:
        key = item[:item.index('(')]
        item = item[item.index('{'):]
        item = item.replace("{", "").replace("}", "")
        if len(item) == 0:
            values = {}
        else:
            item = item.split('), (')
            item = [x.replace('(','').replace(')','') for x in item]
            values = {key:value for element in item for key,value in [element.split(', ')] }
        dict_values = {
            key:values
        }
        data['values'].append(dict_values)
    for item in row['functions']:
        key = item[:item.index('(')]
        item = item[item.index('= (')+3:][:-1]
        key = [x[:x.index('(')] for x in item.split(' ~> ')]
        data['functions'].append(key)
    return data


