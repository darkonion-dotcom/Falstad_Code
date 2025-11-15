import numpy as np

def solve_bridge_circuit(E, R1, R2, R3, R4, R5, R6):
    """
    Resuelve el circuito puente de la página 29 usando análisis nodal.
    
    Nodos:
    - V1 = E (Voltaje de la fuente)
    - V2 = Voltaje en el nodo de entrada del puente (después de R1)
    - V3 = Voltaje en el nodo entre R2, R3 y R6
    - V4 = Voltaje en el nodo entre R4, R5 y R6
    - Tierra = 0V (después de R3 y R5, y en el negativo de E)
    """
    
    # --- Configuración del Sistema de Ecuaciones (Matriz G * V = I) ---
    
    # Matriz G (Conductancia) - Basada en las ecuaciones KCL
    # G = [G11, G12, G13]
    #     [G21, G22, G23]
    #     [G31, G32, G33]
    
    G_matrix = np.array([
        [(1/R1 + 1/R2 + 1/R4), -1/R2, -1/R4],
        [-1/R2, (1/R2 + 1/R3 + 1/R6), -1/R6],
        [-1/R4, -1/R6, (1/R4 + 1/R5 + 1/R6)]
    ])
    
    # Vector I (Corriente) - Basado en las fuentes conocidas
    # I = [I1]
    #     [I2]
    #     [I3]
    
    I_vector = np.array([
        E/R1,
        0,
        0
    ])
    
    # --- Resolución del Sistema ---
    # Resuelve G * V = I para encontrar el vector de voltaje V = [V2, V3, V4]
    try:
        voltages = np.linalg.solve(G_matrix, I_vector)
        
        print("--- Resultados del Análisis Nodal ---")
        print(f"Voltaje en Nodo 2 (V2): {voltages[0]:.4f} V")
        print(f"Voltaje en Nodo 3 (V3): {voltages[1]:.4f} V")
        print(f"Voltaje en Nodo 4 (V4): {voltages[2]:.4f} V")
        print("-------------------------------------")
        
        return voltages
        
    except np.linalg.LinAlgError:
        print("Error: La matriz es singular, el circuito no se puede resolver.")
        return None

# --- EJEMPLO DE USO ---
# Como el diagrama no tiene valores, usaré valores de ejemplo:
# E  = 12 V
# R1 = 100 Ω
# R2 = 200 Ω
# R3 = 300 Ω
# R4 = 400 Ω
# R5 = 500 Ω
# R6 = 600 Ω

print("Simulando el circuito con valores de ejemplo:")
solve_bridge_circuit(E=12, R1=100, R2=200, R3=300, R4=400, R5=500, R6=600)