import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('datos_inspeccion.csv')
df['AÑO'] = df['AÑO'].astype(str).str.replace(',', '')

X = df[['AÑO', 'MES', 'TIPO DE SERVICIO']]
y = df['CANTIDAD']

categorical_features = ['AÑO', 'MES', 'TIPO DE SERVICIO']
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', categorical_transformer, categorical_features)
    ])

pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('regressor', LinearRegression())])

pipeline.fit(X, y)

with open('modelo_regresion.pkl', 'wb') as file:
    pickle.dump(pipeline, file)

print("Modelo exportado correctamente.")
