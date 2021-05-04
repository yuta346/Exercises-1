
#Completed
def remove_ages(pdict,x,y):
    result = {}
    if not pdict:
        return {}
    for name, val in pdict.items():
        if val>=x and val<=y:
            result[name] = val
    return result


pdict = {"Nell": 26, "Sue": 30, "Billy": 4}
print(remove_ages(pdict, 10, 30)) #== {"Nell": 26, "Sue": 30}
