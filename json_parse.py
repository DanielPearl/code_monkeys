d = {"key1":{"dict1","dict2"}, "key2":None, "key3":["list1",True]}

def json_to_string(d):
        print(d)
        new = d
        while len(new) > 0:
            for key in d:
                if type(d[key]) != dict and type(d[key]) != list:
                    return "{" + "{0}:{1}".format(key, d[key]) + "}"
                else:
                    del new[key]
                    return json_to_string(d)

print(json_to_string(d))
