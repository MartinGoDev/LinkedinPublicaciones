# Generador de Dataset de Personajes de Anime

Este proyecto genera un dataset aleatorio de personajes de anime con diferentes características y niveles de poder, utilizando la librería Faker.

## 🎮 Características

- Genera 100 personajes con atributos aleatorios
- Incluye características como nombre, edad, elemento, rol, poder base, poder máximo, etc.
- Genera un reporte de análisis de datos usando ydata-profiling
- Guarda los datos en formato CSV

## 🛠️ Requisitos

```bash
pip install pandas faker ydata-profiling
```

## 📋 Uso

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecuta el script:
```bash
python main.py
```

3. Se generarán dos archivos:
   - `personajes_anime.csv`: Dataset con los personajes generados
   - `reporte_anime.html`: Reporte de análisis de datos

## 📊 Estructura del Dataset

El dataset incluye las siguientes columnas:
- nombre: Nombre del personaje
- edad: Edad del personaje (15-50 años)
- elemento: Afinidad elemental
- rol: Rol en la historia
- poder_base: Poder base del personaje (1-100)
- poder_maximo: Poder máximo alcanzable (100-1000)
- experiencia: Nivel de experiencia (1-1000)
- altura_cm: Altura en centímetros
- peso_kg: Peso en kilogramos
- poder_total: Suma de poder base y máximo

## 🎯 Propósito del Proyecto

Este proyecto demuestra:
- Generación de datos sintéticos con Faker
- Manipulación de datos con Pandas
- Análisis exploratorio de datos con ydata-profiling
- Creación de datasets para análisis y machine learning 