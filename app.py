import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Predicción de Servicios Policiales", page_icon="🚔", layout="wide")

st.title("🚔 Dashboard de Predicción - Inspección de Policía")

@st.cache_resource
def load_or_train_model():
    model_path = 'modelo_regresion.pkl'
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        st.warning("⚠️ Modelo no encontrado. Entrenando el modelo automáticamente desde el dataset...")
        try:
            # Entrenamiento automático como fallback
            from sklearn.model_selection import train_test_split
            from sklearn.preprocessing import OneHotEncoder
            from sklearn.compose import ColumnTransformer
            from sklearn.pipeline import Pipeline
            from sklearn.linear_model import LinearRegression
            
            df = pd.read_csv('SERVICIOS_ATENDIDOS_POR_LA_INSPECCION_DE_POLICIA_20260508.csv')
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
            
            # Guardar el modelo recién entrenado
            with open(model_path, 'wb') as file:
                pickle.dump(pipeline, file)
                
            st.success("✅ Modelo entrenado y guardado exitosamente.")
            return pipeline
        except Exception as e:
            st.error(f"Error al entrenar el modelo: {e}")
            return None

model = load_or_train_model()

if model is None:
    st.error("❌ No se pudo cargar ni entrenar el modelo.")
else:
    st.sidebar.header("Parámetros de Predicción")
    
    # Valores de ejemplo basados en los datos
    anio = st.sidebar.selectbox("Selecciona el Año", ["2020", "2021", "2022", "2023", "2024"])
    mes = st.sidebar.selectbox("Selecciona el Mes", [
        "Enero a Diciembre", "Enero a Marzo", "Abril a Junio", "Julio a Septiembre", "Octubre"
    ])
    tipo_servicio = st.sidebar.selectbox("Selecciona el Tipo de Servicio", [
        "Despachos comisorios Recibidos", "Querellas recibidas", "Actas de amonestación",
        "Audiencias de conciliación", "Notificación personal", "Medidas de protección",
        "Citaciones", "Denuncias o quejas", "Visitas oculares", "Constancia perdida de documento",
        "Autos y resoluciones comparendos", "Audiencia por comparendos"
    ])
    
    if st.sidebar.button("Predecir Cantidad"):
        # Crear dataframe para la predicción
        input_data = pd.DataFrame({
            'AÑO': [anio],
            'MES': [mes],
            'TIPO DE SERVICIO': [tipo_servicio]
        })
        
        prediccion = model.predict(input_data)
        
        # Evitar valores negativos
        valor_estimado = max(0, int(round(prediccion[0], 0)))
        
        st.success(f"La cantidad estimada de '{tipo_servicio}' para el periodo seleccionado es: **{valor_estimado}**")
        
        st.info("💡 Este valor es una estimación basada en datos históricos mediante Regresión Lineal.")

st.markdown("---")
st.markdown("### 📊 Datos Históricos")
try:
    df = pd.read_csv('SERVICIOS_ATENDIDOS_POR_LA_INSPECCION_DE_POLICIA_20260508.csv')
    st.dataframe(df.head(50))
except:
    st.warning("No se pudo cargar el dataset original.")
