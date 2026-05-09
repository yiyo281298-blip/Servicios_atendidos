# 🚔 Servicios Atendidos por la Inspección de Policía - Predicción

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)

## 📖 Descripción del Proyecto
Este proyecto desarrolla un pipeline completo de Machine Learning siguiendo la metodología **CRISP-ML(Q)**. Se utiliza un conjunto de datos sobre los **Servicios Atendidos por la Inspección de Policía** con el objetivo de predecir la cantidad de servicios que se atenderán, basándose en la temporalidad (Año, Mes) y el tipo de servicio. El proyecto finaliza con un despliegue interactivo mediante **Streamlit** y una **Landing Page**.

---

## ⚙️ Metodología CRISP-ML (Ciclo de Vida)

Este proyecto fue desarrollado bajo las 7 fases principales de la metodología CRISP-ML:

### 1. Identificación del Problema (Business and Data Understanding)
*   **Problema:** La inspección de policía necesita prever el volumen de diferentes tipos de servicios (querellas, actas, conciliaciones, etc.) para optimizar la asignación de recursos y tiempos de respuesta.
*   **Objetivo:** Desarrollar un modelo predictivo capaz de estimar la `CANTIDAD` de servicios basados en variables históricas.

### 2. Recolección de Datos (Data Preparation - Extraction)
*   Se obtuvo el archivo original `SERVICIOS_ATENDIDOS_POR_LA_INSPECCION_DE_POLICIA_20260508.csv` que contiene registros desde 2020 hasta el tercer/cuarto trimestre de 2024.

### 3. Preparación de Datos (ETL y EDA)
*   **Limpieza (ETL):** Tratamiento de valores faltantes (si los hay), estandarización de columnas (AÑO, MES) y formateo de la variable objetivo (`CANTIDAD`).
*   **Análisis Exploratorio (EDA):** Visualización de la distribución de servicios a lo largo del tiempo y por tipo. *(Implementado en el cuaderno `01_ETL_EDA.ipynb`)*.

### 4. Ingeniería de Modelos (Model Engineering)
*   Transformación de variables categóricas mediante `OneHotEncoding` u `OrdinalEncoding`.
*   Selección del modelo: **Regresión Lineal**, al tratarse de la predicción de una variable continua / de conteo. *(Implementado en el cuaderno `02_Modelo_Regresion.ipynb`)*.

### 5. Evaluación del Modelo (Model Evaluation)
*   Evaluación mediante métricas de error (como MSE o MAE) y precisión ($R^2$) utilizando un conjunto de datos de prueba (`test_set`).

### 6. Despliegue (Model Deployment)
*   El modelo es exportado a un archivo `.pkl`.
*   Se crea la interfaz de usuario utilizando **Streamlit** en el archivo `app.py`.
*   Se diseña una **Landing Page** moderna (`index.html`) para la presentación del proyecto.

### 7. Mantenimiento y Actualización (Monitoring and Maintenance)
*   El sistema está diseñado para que, al incorporar nuevos registros en el dataset, se puedan re-entrenar los notebooks de manera sencilla, actualizar el archivo `.pkl` y reflejar el nuevo aprendizaje en la aplicación.

---

## 🚀 Estructura del Proyecto

```text
📁 Proyecto
├── 📄 README.md                        # Documentación del proyecto (este archivo)
├── 📄 requirements.txt                 # Dependencias del proyecto
├── 📄 SERVICIOS_ATENDIDOS_POR_LA_INSPECCION_DE_POLICIA_20260508.csv  # Dataset
├── 📓 01_ETL_EDA.ipynb                 # Cuaderno de Extracción y EDA
├── 📓 02_Modelo_Regresion.ipynb        # Cuaderno de Entrenamiento y Modelo
├── 📦 modelo_regresion.pkl             # Modelo entrenado listo para producción
├── 💻 app.py                           # Aplicación web en Streamlit
├── 🌐 index.html                       # Landing Page explicativa
└── 🎨 style.css                        # Estilos para la Landing Page
```

## 🛠️ Instrucciones de Ejecución

1. **Instalar Dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Ejecutar los Cuadernos (Opcional, para reentrenar el modelo):**
   Abre y ejecuta en orden `01_ETL_EDA.ipynb` y `02_Modelo_Regresion.ipynb` en tu entorno Jupyter.
3. **Lanzar la Aplicación Streamlit:**
   ```bash
   streamlit run app.py
   ```
4. **Ver la Landing Page:**
   Simplemente haz doble clic sobre el archivo `index.html` para abrirlo en tu navegador favorito.
