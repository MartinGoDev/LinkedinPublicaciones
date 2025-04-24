import pandas as pd
from faker import Faker
import random
from ydata_profiling import ProfileReport

# Inicializar Faker
fake = Faker()

# Lista de posibles elementos/afinidades
elementos = ['Fuego', 'Agua', 'Tierra', 'Aire', 'Luz', 'Oscuridad', 'Hielo', 'Rayos']

# Lista de posibles roles
roles = ['Protagonista', 'Antagonista', 'Secundario', 'Mentor', 'Rival']

# Generar datos
num_personajes = 100
datos = []

for _ in range(num_personajes):
    personaje = {
        'nombre': fake.name(),
        'edad': random.randint(15, 50),
        'elemento': random.choice(elementos),
        'rol': random.choice(roles),
        'poder_base': random.randint(1, 100),
        'poder_maximo': random.randint(100, 1000),
        'experiencia': random.randint(1, 1000),
        'altura_cm': random.randint(150, 200),
        'peso_kg': random.randint(45, 100)
    }
    datos.append(personaje)

# Crear DataFrame
df = pd.DataFrame(datos)

# Calcular poder total (poder_base + poder_maximo)
df['poder_total'] = df['poder_base'] + df['poder_maximo']

# Generar reporte de perfil
profile = ProfileReport(df, title="Reporte de Personajes de Anime")
profile.to_file("reporte_anime.html")

# Guardar el dataset
df.to_csv('personajes_anime.csv', index=False)

print("Dataset creado y reporte generado exitosamente!")






