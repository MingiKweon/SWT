import pickle

mydat = ["kookmin",123,"재밌다"]

with open("my.dat","wb") as f:
    pickle.dump(mydat,f)

with open("my.dat","rb") as f:
    x = pickle.load(f)

    print(x)