def new_str(str):
    if len(str)>=2 and str[:2]=="is":
        return str
    return "is" + str
print(new_str("Array"))
print(new_str("isloaded"))
