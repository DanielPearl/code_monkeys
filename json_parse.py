import json

d = [{"key":"value"},5,"string",["string",4]]

def json_to_string(d):
        # print(d)
        new = d
        while len(new) > 0:
            for key in d:
                print(key)
                print(type(d[key]))
                if type(d[key]) == dict:
                    return "{" + "{0}:{1}".format(key, d[key]) + "}"
                else:
                    del new[key]
                    return json_to_string(d)

def json_loads(d):
    jstring = json.dumps(d)
    return jstring

print(json_to_string(d))
print(d)
print(json_loads(d))
