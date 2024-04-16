import pickle

f=open('embeddings.pickle','rb')
print(f)
data=pickle.load(f)
print(len(data["embeddings"]))
print(data["names"])
f.close()

