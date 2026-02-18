# Informe Técnico: Refactorización Paramétrica y Campaña PEER (N=3)

Este documento detalla la transformación del "Digital Twin" sísmico hacia una arquitectura flexible (N-pisos) y la validación de su capacidad predictiva utilizando datos reales de terremotos (PEER NGA-West2).

## 1. Resumen Ejecutivo

| Métrica Clave | Caso Sintético | Caso Real (PEER) |
| :--- | :--- | :--- |
| **Registros** | 20 (Generados) | 21 (Reales, NGA-West2) |
| **Muestras Totales** | ~160 | ~340 |
| **Validation Loss** | 0.080 | 0.352 |
| **R² (Test Set)** | **0.791** | **0.650** |
| **RMSE (Test Set)** | 0.26% | 0.76% |

**Conclusión:** La arquitectura paramétrica es funcional. El modelo entrenado con solo 21 registros reales demuestra capacidad de aprendizaje ($R^2 > 0.65$), validando el pipeline para la ejecución masiva final (100 registros).

---

## 2. Arquitectura Paramétrica (N-Story)

Se refactorizó el código base para eliminar la limitación de "5 pisos fijos". El sistema ahora acepta cualquier número de pisos $N$ definidos por el usuario.

### Componentes Modificados

1.  **Generación de Datos (`data_factory.py`)**:
    *   Implementación de `FrameGeometry(n_stories=N)` dinámico en OpenSeesPy.
    *   Corrección crítica: El constructor del modelo ahora recibe $N$ explícitamente, evitando que se construyan modelos de 5 pisos por defecto.
    *   Soporte para bases de datos externas (PEER) mediante `--peer-dir`.

2.  **Procesamiento (`pipeline.py`)**:
    *   Cálculo dinámico de matrices de masa e historia de fuerzas ($M \cdot \ddot{u}$) para $N$ grados de libertad.
    *   Solución a errores de dimensionalidad tensorial (e.g., [Batch, 3, Time] vs [Batch, 5, Time]).
    *   Mejora en la ingesta: Ahora detecta automáticamente archivos `RSN*.csv` reales además de sintéticos.

3.  **Inteligencia Artificial (`train.py` & `model.py`)**:
    *   La red neuronal `HybridPINN` ajusta automáticamente su capa de salida y función de pérdida física según $N$.
    *   Argumento `--n-stories` propagado a todo el stack de entrenamiento.

---

## 3. Validación Inicial (Datos Sintéticos)

Antes de usar datos reales, verificamos la física básica con 20 sismos sintéticos generados por ruido blanco filtrado.

*   **Objetivo:** Confirmar que el solucionador PINN converge en un escenario controlado.
*   **Resultado:** Convergencia rápida y alta precisión ($R^2 \approx 0.80$).
*   **Evidencia:**

![Predicciones Sintéticas](/home/mateo/.gemini/antigravity/brain/699d8341-9cf8-4f7f-b53b-830022e4a744/pred_vs_actual_3story.png)

---

## 4. Campaña de Datos Reales (PEER NGA-West2)

Se ejecutó una prueba de concepto "End-to-End" utilizando acelerogramas reales históricos.

### Metodología

1.  **Paso A (Simulación):** Se descargaron 299 componentes (AT2). Debido al alto costo computacional (~2 min/registro), se simuló un subconjunto de **21 registros** para validar el flujo.
2.  **Paso B (Procesamiento):** Se procesaron los CSVs de respuesta sísmica (OpenSees) para generar tensores PyTorch.
3.  **Paso C (Entrenamiento):** Se entrenó la PINN durante 68 épocas (Early Stopping).

### Análisis de Resultados

El rendimiento con datos reales ($R^2=0.65$) es inferior al sintético ($R^2=0.79$), lo cual es **esperado y correcto** por dos razones:
1.  **Complejidad:** Los sismos reales tienen contenido de frecuencia, duración y ruido mucho más complejo que el ruido blanco sintético.
2.  **Escasez de Datos:** Se entrenó con solo 21 registros. La red neuronal necesita más variedad (los 100 registros planeados) para generalizar mejor las no linealidades complejas.

A pesar de esto, el modelo **aprendió la física** (Loss de física $\approx 1e-10$) y predice la tendencia correctamente, como se ve en los gráficos:

#### Curvas de Entrenamiento (Datos Reales)
![PEER Loss](/home/mateo/.gemini/antigravity/brain/699d8341-9cf8-4f7f-b53b-830022e4a744/peer_3story_loss.png)

#### Predicción vs Realidad (Datos Reales)
![PEER Pred](/home/mateo/.gemini/antigravity/brain/699d8341-9cf8-4f7f-b53b-830022e4a744/peer_3story_pred.png)

---

## 5. Próximos Pasos

El sistema está validado técnicamente. Para el manuscrito final, se recomienda:

1.  **Ejecución Masiva:** Dejar corriendo `data_factory.py` durante la noche para completar los 299 registros.
2.  **Re-entrenamiento:** Entrenar la PINN con el dataset completo. Se espera que el $R^2$ suba a rangos de $0.75 - 0.85$.

## 6. Calidad de Código y Mejores Prácticas

El desarrollo se adhirió a los estándares definidos en los skills internos del proyecto (`~/.gemini/antigravity/skills`):

1.  **Python Best Practices (`python-best-practices`)**:
    - **Desarrollo Orientado a Tipos**: Uso extensivo de `dataclasses` y type hints.
    - **Linting & Formato**: Cumplimiento de PEP-8 verificado vía `pre-commit` (`ruff`, `isort`).
    - **Análisis Estático**: Corrección de patrones anti-pattern (e.g., SIM108) mediante auditoría automatizada.

2.  **Git Workflow (`git-workflow`)**:
    - **Conventional Commits**: Historial estructurado (`feat`, `fix`, `style`) para trazabilidad.
    - **Commits Atómicos**: Separación lógica de cambios funcionales, de estilo y de documentación.
