import pandas as pd
import pickle as pkl

df = pd.read_csv("data/val_bf.csv")

df.dropna(inplace = True)

target = df["Survived"]
del(df["Survived"])
    
model_unpickle = open("data/model.pkl", 'rb')
model = pkl.load(model_unpickle)
model.close()

predictions = model.predict(df)
# Reassign target (if it was present) and predictions.
df["prediction"] = predictions
df["target"] = target

ok = 0
for i in df.iterrows():
    if (i[1]["target"] == i[1]["prediction"]):
        ok = ok + 1

print("accuracy is", ok / df.shape[0])
