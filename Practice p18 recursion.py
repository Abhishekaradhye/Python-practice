
def openabc(res):
    if res <=0:
        return res
    else:
        output = openabc(res - 1)
        return output
    
print(openabc(0))
print(openabc(-9))