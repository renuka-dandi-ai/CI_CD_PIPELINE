import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression

#load data
df=pd.read_csv(r"C:\Users\Renuka dandi\OneDrive\Documents\CI_CD_pipeline\data\data.csv")

x=df[["area","bedrooms"]]
y=df["price"]

#train model
model=LogisticRegression()
model.fit(x,y)

#save model
with open(r"C:\Users\Renuka dandi\OneDrive\Documents\CI_CD_pipeline\backend\models\model.pkl","wb") as f:
    pickle.dump(model,f)
