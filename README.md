# 🎓 Defensa Metodológica de Investigación Científica (Puntos 6.4 al 6.7)
### Universidad Privada Domingo Savio (UPDS) — Sede Santa Cruz
**Docente Evaluador:** Lic. Marcial Villarroel Siles  
**Enfoque:** Metodología de la Investigación Científica Aplicada  

---

## 🌐 Enlace en Vivo (GitHub Pages)
Una vez activado GitHub Pages en el repositorio, la presentación estará disponible en:
👉 **[https://josempb13.github.io/presentacion_tec_inv/](https://josempb13.github.io/presentacion_tec_inv/)**

---

## 📱 Modo Control Remoto Móvil con Notas Privadas
La aplicación incluye un sistema de doble vista diseñado para exposiciones formales con proyector:
1. **En la Pantalla / Proyector (Laptop):**  
   Muestra únicamente las diapositivas en alta resolución, sin notas ni elementos distractores para el tribunal evaluador.
2. **En el Celular del Expositor:**  
   Al escanear el código QR (o acceder con `?remote=1`):
   - **Botones táctiles grandes:** `[◀ ANTERIOR]` y `[SIGUIENTE ▶]` para pasar diapositivas a distancia.
   - **Cronómetro individual de 3:00 minutos:** Con alertas de tiempo por orador.
   - **Notas Privadas Completas:** Objetivo pedagógico, guion verbal de exposición y frase de pase formal al siguiente compañero.
   - **Sincronización en tiempo real:** Funciona mediante WebSockets seguros (MQTT Relay) sin requerir instalación de ninguna app.

---

## 👥 Estructura de Expositores y Temario

| N° | Expositor | Subtema | Diapositivas |
| :---: | :--- | :--- | :---: |
| **—** | **Equipo de Investigación** | Apertura Formal y Carátula Protocolar | Diapositiva 1 |
| **1** | **Deivy Melgar Perez** | 6.4 Tabulación de Datos: Concepto, Finalidad y Rol Metodológico | Diapositiva 2 |
| **2** | **María Teresa Paco Flores** | 6.4 Codificación Técnica, Libro de Códigos y Matriz $(N \times K)$<br>6.4 Tratamiento del Missing Data y Tabulación Cruzada $(2 \times 2)$ | Diapositivas 3 y 4 |
| **3** | **José Maria Peredo Barba** | 6.5 Sistematización y Distribución de Frecuencias Canónica<br>6.5 Agrupación en Intervalos de Clase y Marca de Clase | Diapositivas 5 y 6 |
| **4** | **Mishel Alcázar Valdez** | 6.5 Criterios de Selección Gráfica según Nivel de Medida<br>6.5 Diagrama de Caja y Bigotes (Boxplot) y Detección de Outliers | Diapositivas 7 y 8 |
| **5** | **Carlos Alberto Choque Serrano** | 6.6 Análisis Cuantitativo de Datos: Fases Secuenciales<br>6.6 Modelos Estadísticos Clásicos: Correlación ($r$) y Regresión Lineal | Diapositivas 9 y 10 |
| **6** | **Dapne Scarlet Salvatierra Nina** | 6.6 Minería de Datos y el Proceso KDD (*Knowledge Discovery*)<br>6.6 Selección de Modelos Predictivos y Advertencia Causal | Diapositivas 11 y 12 |
| **7** | **Yord Gember Rojas Rocha** | 6.7 Procesamiento en IBM SPSS Statistics: Vista de Datos y Variables<br>6.7 Interpretación de Salida SPSS y Lectura Rigurosa del $p$-valor | Diapositivas 13 y 14 |
| **8** | **Rodrigo Arauz Mercado** | 6.7 Análisis Cualitativo en ATLAS.ti: Unidad Hermenéutica<br>6.7 Redes Semánticas y Triangulación Metodológica Cualitativa | Diapositivas 15 y 16 |
| **—** | **Rodrigo Arauz Mercado y Equipo** | Síntesis Metodológica Comparativa y Glosario Académico | Diapositiva 17 |
| **—** | **Tribunal Evaluador** | Ronda de Preguntas y Defensa Oral Colegiada | Diapositiva 18 |

---

## ⌨️ Atajos de Teclado (Laptop)
- **`Flecha Derecha` / `Espacio`:** Siguiente diapositiva.
- **`Flecha Izquierda`:** Diapositiva anterior.
- **`M`:** Abrir ventana de **Control Remoto Móvil y Código QR**.
- **`N`:** Ver **Notas del Presentador** en pantalla.
- **`O`:** Vista general de **Miniaturas** para navegación rápida.
- **`G`:** Abrir **Glosario Metodológico**.
- **`A`:** Consultar **Guía de Estilo APA 7**.
- **`F11`:** Pantalla completa del navegador.
- **`Esc`:** Cerrar cualquier ventana emergente o modal.

---

## 🛠️ Arquitectura Técnica
- **Archivo único autocontenido:** [index.html](file:///c:/Users/josem/Desktop/Nueva%20carpeta/index.html) sin dependencias pesadas de frameworks externos.
- **Estilos:** CSS3 nativo con diseño oscuro académico (*Slate Dark* `#0f172a`), tipografía escalable e interfaces adaptativas.
- **Matemáticas y Tipografía:** Notación matemática limpia con subíndices, superíndices y caracteres científicos sin requerir librerías externas de renderizado.
- **Interacciones:** Simuladores interactivos en tiempo real (cálculo de intervalos de Sturges, matriz de correlación Pearson, visualizador hermenéutico ATLAS.ti, y selector de escalas de medición).
