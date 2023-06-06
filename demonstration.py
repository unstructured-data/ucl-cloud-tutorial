#%%
import time
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

#%%

# set path to data

path_to_data = "../"

# read document-term matrix
dt = pd.read_csv(path_to_data + "dt.csv")

# rename first column (contains the cik code)
dt.rename(columns={"Unnamed: 0": "cik"}, inplace=True)

# extract the cik codes and remove from dataframe
cik = dt[["cik"]]
dt.drop(columns=["cik"], inplace=True)

dt

#%%

# save columns as vocabulary
vocab = dt.columns

# transform the document-term matrix into a numpy array
dt = dt.values
dt.shape

#%%

# read the covariates data for the cik codes
df_cov = pd.read_csv(path_to_data + "cik_covariates.csv")
df_cov

#%%

# merge the naics2 sector with the ciks codes
naics2 = pd.merge(cik, df_cov[["cik", "naics2"]], on="cik", how="left")
labels = naics2["naics2"].values
print(labels.shape)
#%%

# define the model
model = RandomForestClassifier(n_estimators=20, n_jobs=-1)
model

#%%

# fit the model (time it)
start = time.perf_counter()
model.fit(dt, labels)
end = time.perf_counter()
print(f"Time to fit: {end - start:.2f} seconds")

#%%

# get the feature importances
importances = model.feature_importances_
# sort the feature importances
indices = importances.argsort()[::-1]
# get the top 10 features
top10 = indices[:10]
# get the top 10 feature names
top10_features = [vocab[i] for i in top10]
top10_features

#%%

# generate in-sample predictions
start = time.perf_counter()
preds = model.predict(dt)
end = time.perf_counter()
print(f"Time to predict: {end - start:.2f} seconds")

#%%

# calculate the accuracy
acc = (preds == labels).mean()
print(f"Accuracy: {acc:.2f}")

#%%

# save the model with pickle
import pickle
model_name = "model.pkl"
with open(model_name, "wb") as f:
    pickle.dump(model, f)

# save the feature importances as csv with the name of the feature and its importance
importances = pd.DataFrame({"feature": vocab, "importance": model.feature_importances_})
importances.to_csv("importances.csv", index=False)

# %%
