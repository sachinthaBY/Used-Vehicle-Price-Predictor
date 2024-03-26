import pickle
from sklearn.ensemble import RandomForestRegressor

model = pickle.load(open('model.pkl', 'rb'))
print(model.predict([[1,11,2016,1,1,1000,25000]]))
