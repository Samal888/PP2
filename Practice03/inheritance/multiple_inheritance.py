t = (1,2,6,4,9,6,"ab","bcr","aeo","gah",-6,-7)

vowels = "aoeui"

#l -- ["ab","aeo","gah"]

def hasvowel(x):
    for i in range(len(x)):
        if x[i] in vowels:
            return True
    return False

l = list(filter(lambda x: isinstance(x,str) and hasvowel(x), t))
print(l)