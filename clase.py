#Resultado será un Grafo de Calificaciones de Personas
#Cada Nodo es un promedio de Calificaciones
#Cada Persona tiene varias Calificaciones
#Cada Calificación está relacionada con un nodo al promediarse
# En lugar de Colegas sean Calificaciones Las Calificaciones sean de 60 a 100
# 6 personas con varias calificaciones (mas de 3 calificaciones) y al menos 3 promedios diferentes
# Si el promedio es menor que 70, el nodo es rojo

import json
import networkx as nx
import matplotlib.pyplot as plt

# Datos directamente como diccionario
personas = [
    {"name": "Javi", "calificaciones": [60,70,80,65]},
    {"name": "Adrian", "calificaciones": [65,60,70,55]},
    {"name": "Pablo", "calificaciones": [75,80,85,90]},
    {"name": "Fer", "calificaciones": [90,90,85,95]},
    {"name": "Ivan", "calificaciones": [85,90,95,100]},
    {"name": "Yayo", "calificaciones": [70,75,80,85]}
]

G = nx.Graph()

# Agregar nodos y calcular promedios
for p in personas:
    promedio = sum(p["calificaciones"]) / len(p["calificaciones"])
    G.add_node(p["name"], promedio=promedio)

# Conectar todas las personas entre sí
nombres = [p["name"] for p in personas]
for i in range(len(nombres)):
    for j in range(i+1, len(nombres)):
        G.add_edge(nombres[i], nombres[j])

# Configurar colores y etiquetas
colores = ['red' if G.nodes[n]['promedio'] < 70 else 'blue' for n in G.nodes()]
etiquetas = {n: f"{n}\n({G.nodes[n]['promedio']:.1f})" for n in G.nodes()}

# Dibujar el grafo
plt.figure(figsize=(8, 6))
nx.draw(G, labels=etiquetas, node_color=colores, 
        with_labels=True, node_size=2000, font_size=10)
plt.title("Grafo de Calificaciones")
plt.show()
