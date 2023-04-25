#%%
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# generate a synthetic dataset
X, y = make_classification(n_samples=10000, 
                           n_features=20, 
                           n_informative=18, 
                           n_redundant=2, 
                           random_state=42)

print(X.shape)
print(y.shape)

#%%

# define the model
model = RandomForestClassifier(n_estimators=500, n_jobs=-1)
model

# %%

# fit the model (time it)
start = time.perf_counter()
model.fit(X, y)
end = time.perf_counter()
print(f"Time to fit: {end - start:.2f} seconds")
# %%
