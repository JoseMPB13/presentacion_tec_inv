# -*- coding: utf-8 -*-
"""
Helper module defining the enriched presenter notes and dynamic per-slide glossaries.
"""

# Glosario dinámico para cada una de las 17 diapositivas
SLIDE_GLOSSARIES = {
    1: [
        {"term": "Metodología de la Investigación", "easy": "El camino ordenado y comprobable que se sigue para descubrir la verdad sin caer en suposiciones."},
        {"term": "Defensa Colegiada", "easy": "Exposición formal donde todos los miembros del equipo demuestran dominio integral de los temas defendidos."},
        {"term": "Triangulación Metodológica", "easy": "Combinar números y palabras para tener una visión 100% completa de la realidad investigada."}
    ],
    2: [
        {"term": "Tabulación de Datos", "easy": "Pasar de tener una montaña de encuestas desordenadas a una tabla ordenada y limpia lista para contar."},
        {"term": "Unidad de Análisis", "easy": "Cada persona, documento o entidad individual a la que se le aplicó la encuesta (ej. un docente o un estudiante)."},
        {"term": "Registro Primario", "easy": "El cuestionario original tal cual fue respondido por la persona, antes de cualquier modificación."}
    ],
    3: [
        {"term": "Matriz de Datos (N × K)", "easy": "Una tabla como Excel donde las filas (N) son las personas y las columnas (K) son las preguntas evaluadas."},
        {"term": "Libro de Códigos (Codebook)", "easy": "El 'diccionario de traducción' que define qué número representa cada respuesta (ej. 1 = Varón, 2 = Mujer)."},
        {"term": "Pre-codificación vs. Post-codificación", "easy": "Pre-codificar es poner números antes de encuestar; post-codificar es leer respuestas de texto libre y agruparlas en números después."}
    ],
    4: [
        {"term": "Missing Data (Valores Perdidos)", "easy": "Casillas vacías en la tabla porque la persona no quiso responder, no sabía o se saltó la pregunta."},
        {"term": "Eliminación Listwise", "easy": "El grave error de botar a la basura a toda la persona encuestada solo porque dejó una preguntita en blanco."},
        {"term": "Tabla de Contingencia (2 × 2)", "easy": "Una tablita de 4 casillas para comparar dos grupos frente a dos alternativas (ej. Varones vs. Mujeres que usan aula virtual)."}
    ],
    5: [
        {"term": "Frecuencia Absoluta (fᵢ)", "easy": "La cantidad exacta de personas que eligieron una opción específica."},
        {"term": "Porcentaje Válido", "easy": "El porcentaje real calculado únicamente sobre los que sí respondieron, sin contar las casillas en blanco."},
        {"term": "Frecuencia Acumulada (Fᵢ)", "easy": "La suma progresiva de personas desde la primera opción hasta la actual ('hasta aquí acumulamos tantos')."}
    ],
    6: [
        {"term": "Intervalo de Clase", "easy": "Grupos de valores para no hacer una fila por cada número (ej. notas de 51 a 60, de 61 a 70)."},
        {"term": "Marca de Clase (Xᵢ)", "easy": "El punto medio exacto de cada grupo; representa matemáticamente a todo el intervalo en los cálculos."},
        {"term": "Amplitud (c)", "easy": "El ancho o tamaño de cada grupo (ej. en el intervalo de 51 a 60 hay una amplitud de 10 puntos)."}
    ],
    7: [
        {"term": "Escala Nominal", "easy": "Etiquetas o nombres que no tienen orden ni jerarquía (ej. Carreras: Sistemas, Derecho, Medicina). Se grafican con barras separadas."},
        {"term": "Escala Continua", "easy": "Números que pueden tener decimales y van seguidos sin saltos (ej. notas de 0 a 100). Exigen un Histograma."},
        {"term": "Histograma", "easy": "Gráfico de barras que van completamente pegadas para mostrar que los números continuos no tienen interrupciones."}
    ],
    8: [
        {"term": "Boxplot (Diagrama de Caja)", "easy": "Una radiografía visual que resume en un solo dibujo las notas mínimas, máximas y el 50% de la gente del medio."},
        {"term": "Mediana", "easy": "La nota exacta que divide a los participantes en dos mitades iguales (50% arriba y 50% abajo)."},
        {"term": "Rango Intercuartílico (IQR)", "easy": "El tamaño de la caja central; contiene exactamente al 50% central de los participantes."},
        {"term": "Outlier (Dato Atípico)", "easy": "Un caso rarísimo o extremo muy separado del resto (ej. alguien que sacó 99 cuando el promedio del curso fue 50)."}
    ],
    9: [
        {"term": "Estadística Descriptiva", "easy": "Resumir y mostrar lo que ocurrió con los encuestados que participaron en el estudio."},
        {"term": "Estadística Inferencial", "easy": "Generalizar y sacar conclusiones para toda una población a partir de una muestra de participantes."},
        {"term": "Distribución Normal (Campana de Gauss)", "easy": "Cuando la mayoría de notas se concentran en el centro y muy pocas en los extremos."}
    ],
    10: [
        {"term": "Correlación (r de Pearson)", "easy": "Un número de -1 a +1 que mide si dos cosas suben o bajan juntas (ej. a más horas de estudio, mayor nota)."},
        {"term": "Regresión Lineal", "easy": "Una fórmula matemática que permite predecir el futuro (ej. predecir la nota exacta según las horas estudiadas)."},
        {"term": "Variable Independiente (X) y Dependiente (Y)", "easy": "X es la causa que manejamos (horas de estudio) e Y es el efecto resultante (nota obtenida)."}
    ],
    11: [
        {"term": "Minería de Datos", "easy": "Usar computadoras potentes para descubrir patrones y secretos ocultos en gigantescos volúmenes de datos."},
        {"term": "Proceso KDD", "easy": "Los pasos científicos ordenados desde seleccionar los datos hasta transformarlos en decisiones inteligentes."},
        {"term": "Patrón Oculto", "easy": "Una relación importante que los humanos no pueden notar a simple vista en una tabla común."}
    ],
    12: [
        {"term": "Correlación NO es Causalidad", "easy": "Regla de oro: que dos cosas ocurran a la vez no significa que una cause a la otra (ej. helados y ahogamientos)."},
        {"term": "Sobreajuste (Overfitting)", "easy": "Cuando un modelo se aprende los datos de memoria y falla al intentar predecir casos nuevos de la realidad."},
        {"term": "Precedencia Temporal", "easy": "Para afirmar que A causa B, la causa A tiene que ocurrir obligatoriamente antes en el tiempo que el efecto B."}
    ],
    13: [
        {"term": "IBM SPSS Statistics", "easy": "El software estadístico más utilizado en universidades para procesar datos cuantitativos sin errores de cálculo."},
        {"term": "Vista de Variables", "easy": "La pestaña donde se configuran y bautizan las preguntas (nombre, tipo de dato, etiquetas y valores)."},
        {"term": "Vista de Datos", "easy": "La hoja parecida a Excel donde se observan las respuestas reales persona por persona."}
    ],
    14: [
        {"term": "p-valor (Sig. bilateral)", "easy": "El detector de mentiras científico: la probabilidad de que nuestro hallazgo haya sido producto de la suerte o casualidad."},
        {"term": "Regla p < 0.05", "easy": "Si el p-valor es menor al 5%, festejamos: el resultado es estadísticamente real y se rechaza la casualidad."},
        {"term": "Hipótesis Nula (H₀)", "easy": "La postura escéptica que afirma: 'Aquí no hay relación alguna, todo fue simple coincidencia'."}
    ],
    15: [
        {"term": "Análisis Cualitativo", "easy": "Investigar a profundidad palabras, entrevistas, vivencias y opiniones humanas en lugar de números."},
        {"term": "Unidad Hermenéutica", "easy": "El proyecto o contenedor en ATLAS.ti que agrupa todos los documentos, audios y entrevistas de la investigación."},
        {"term": "Citas (Quotations)", "easy": "Fragmentos textuales exactos de lo que dijeron los entrevistados que usamos como evidencia viva."}
    ],
    16: [
        {"term": "Red Semántica", "easy": "Un mapa conceptual en ATLAS.ti donde conectamos ideas con flechas que tienen significado (ej. 'es causa de', 'contradice')."},
        {"term": "Codificación Axial", "easy": "El proceso de encontrar cuál es el tema o problema principal que conecta todas las opiniones de la gente."},
        {"term": "Triangulación Cualitativa-Cuantitativa", "easy": "Respaldar los porcentajes de SPSS con los testimonios de ATLAS.ti para una investigación sólida."}
    ],
    17: [
        {"term": "Ciclo Metodológico Completo", "easy": "El recorrido ordenado: ordenar los datos -> graficar -> probar hipótesis -> escuchar testimonios."},
        {"term": "Rigor Científico", "easy": "Cumplir cada paso del método para que ningún evaluador pueda dudar de la veracidad de los resultados."},
        {"term": "Auditoría de Datos", "easy": "Mantener la matriz y el libro de códigos limpios para que cualquiera pueda verificar la investigación."}
    ]
}

# Notas pedagógicas del expositor enriquecidas para las 17 diapositivas
PRESENTER_NOTES = {
    1: {
        "speaker": "Equipo de Investigación UPDS",
        "goal": "Apertura formal de la defensa, presentación del equipo y contextualización del informe metodológico.",
        "script": "Buenos días estimado docente evaluador, Licenciado Marcial Villarroel Siles, y compañeros. Hoy nuestro equipo presenta la defensa formal del informe metodológico correspondiente a los puntos 6.4 al 6.7. A lo largo de esta exposición demostraremos cómo los datos brutos se transforman paso a paso en conocimiento científico riguroso: desde la recolección y tabulación, pasando por la distribución de frecuencias y selección gráfica, hasta llegar a las pruebas estadísticas en SPSS y la interpretación cualitativa en ATLAS.ti. Cada uno de los 8 expositores defenderá un subtema clave articulado de manera colegiada.",
        "metaphor": "Investigar es como construir un edificio: si los cimientos (la tabulación y la matriz de datos) están desordenados, todo el análisis que se construya encima se vendrá abajo.",
        "faq": "¿Por qué es indispensable este proceso secuencial? Respuesta: Porque la ciencia exige que cualquier otro investigador pueda repetir nuestros pasos (replicabilidad) y llegar exactamente a los mismos resultados.",
        "pass": "Para dar inicio al Bloque 1, cedo la palabra a mi compañero Deivy Melgar Perez, quien expondrá el concepto y rol metodológico de la tabulación."
    },
    2: {
        "speaker": "Deivy Melgar Perez (Expositor 1)",
        "goal": "Explicar de forma clara qué es la tabulación de datos, para qué sirve y cómo evita errores graves en la investigación.",
        "script": "Muchas gracias. Estimado jurado, cuando aplicamos una encuesta a decenas o cientos de personas, lo primero que tenemos en las manos es un cúmulo caótico de papeletas o registros sueltos. La tabulación de datos es precisamente el puente metodológico que transforma ese desorden en un sistema ordenado y listo para ser analizado. Consiste en contar, agrupar y organizar las respuestas en tablas sintéticas. Como vemos en el ejemplo en pantalla, si preguntamos a 5 docentes de la UPDS su antigüedad y su uso de tecnología, la tabulación nos permite pasar de hojas sueltas a un conteo ordenado que revela de inmediato los patrones de la muestra.",
        "metaphor": "La tabulación es como clasificar la correspondencia en una oficina postal: antes de entregar las cartas, hay que separarlas por barrio y calle para no perder nada.",
        "faq": "¿Cuál es la diferencia entre tabulación manual y electrónica? Respuesta: La manual usa palotes de conteo para muestras pequeñas; la electrónica procesa matrices masivas en hojas de cálculo o SPSS garantizando velocidad y cero error de cálculo.",
        "pass": "Habiendo sentado las bases de la tabulación, doy paso a mi compañera María Teresa Paco Flores, quien explicará el proceso técnico de codificación y la estructura de la matriz de datos."
    },
    3: {
        "speaker": "María Teresa Paco Flores (Expositor 2)",
        "goal": "Demostrar cómo se codifican preguntas cualitativas y cuantitativas y explicar la anatomía de la matriz de datos (N × K).",
        "script": "Gracias Deivy. Continuando con el punto 6.4, las computadoras y los programas estadísticos no leen discursos ni sentimientos: leen números. La codificación es la técnica que traduce las respuestas de las personas en valores numéricos bien definidos. Si la pregunta es cerrada, como el género, usamos pre-codificación: 1 para masculino y 2 para femenino. Si la pregunta es abierta, usamos post-codificación: leemos todas las respuestas, identificamos las ideas que más se repiten y les asignamos un código en nuestro 'Libro de Códigos'. Toda esta información se vuelca en una Matriz de Datos rectangular: cada fila es un participante (N) y cada columna es una pregunta o variable (K). En el inspector interactivo de la lámina vemos cómo el Sujeto 4 tiene sus códigos perfectamente asignados.",
        "metaphor": "El Libro de Códigos es como el diccionario de traducción entre lo que la persona respondió en su propio idioma y lo que la computadora necesita para calcular.",
        "faq": "¿Qué pasa si cambio un código a mitad de la investigación? Respuesta: Se contamina toda la base de datos. Por eso el Libro de Códigos se redacta antes y se respeta como documento oficial de auditoría.",
        "pass": "Continuando con mi intervención, paso ahora a explicar el tratamiento de los datos faltantes y las tablas de contingencia 2 × 2."
    },
    4: {
        "speaker": "María Teresa Paco Flores (Expositor 2 - Cont.)",
        "goal": "Alertar sobre el peligro de los datos faltantes (Missing Data) y explicar las tablas de contingencia 2 × 2 con porcentajes de fila.",
        "script": "Un aspecto crítico en toda investigación es: ¿qué hacemos cuando una persona no responde una pregunta? En estadística jamás debemos dejar la casilla vacía. Si dejamos un espacio en blanco, SPSS lo asume como 'perdido por el sistema' y suele cometer la 'eliminación por lista', desechando a toda la persona de cálculos futuros. La solución profesional es usar códigos de usuario: 8 para 'no aplica' o 9 para 'no contestó'. Asimismo, cuando necesitamos cruzar dos variables cualitativas, utilizamos las tablas de contingencia 2 por 2. En el ejemplo en pantalla de 150 docentes, cruzamos género y uso del aula virtual. Al mirar los porcentajes de fila, vemos claramente que el 75% de las mujeres utiliza el aula frente al 57% de los varones, insumo clave para la prueba Chi-cuadrado.",
        "metaphor": "Botar a un encuestado completo porque le faltó una respuesta es como tirar a la basura un libro entero de 300 páginas porque le falta una sola línea.",
        "faq": "¿Por qué calculamos porcentaje de fila y no de columna? Respuesta: Porque el porcentaje debe calcularse en el sentido de la variable independiente (género) para poder comparar los subgrupos de manera equitativa.",
        "pass": "Para dar inicio al Bloque 2 sobre sistematización y distribución de frecuencias, cedo la palabra a mi compañero José Maria Peredo Barba."
    },
    5: {
        "speaker": "José Maria Peredo Barba (Expositor 3)",
        "goal": "Explicar los 5 componentes obligatorios de una tabla de frecuencias y demostrar por qué el porcentaje válido es indispensable.",
        "script": "Muchas gracias María Teresa. En el punto 6.5 abordamos la sistematización. Sistematizar significa resumir las observaciones en una tabla de distribución de frecuencias canónica con cinco columnas: la categoría, la frecuencia absoluta, el porcentaje total, el porcentaje válido y el porcentaje acumulado. Quiero llamar la atención del jurado sobre el 'Porcentaje Válido'. En la simulación interactiva que tienen en pantalla, de 10 personas encuestadas, 2 dejaron la casilla vacía. Si calculamos sobre el total de 10, la satisfacción parece ser solo del 50%. Pero si calculamos el Porcentaje Válido sobre las 8 personas que sí respondieron, la satisfacción real es del 62.5%. Usar el porcentaje total falsearía la realidad.",
        "metaphor": "El porcentaje válido es como calificar un examen: la nota se saca sobre las preguntas que estaban en el examen, no sobre preguntas que el profesor olvidó imprimir.",
        "faq": "¿Cuándo coinciden el porcentaje total y el porcentaje válido? Respuesta: Únicamente cuando no existe ningún dato faltante en la muestra analizada.",
        "pass": "A continuación, en mi segunda lámina, explicaré cómo agrupar variables continuas en intervalos y el cálculo de la marca de clase."
    },
    6: {
        "speaker": "José Maria Peredo Barba (Expositor 3 - Cont.)",
        "goal": "Detallar cómo se agrupan datos continuos en intervalos de clase, calculando la marca de clase y la amplitud.",
        "script": "Cuando medimos variables cuantitativas continuas con decenas de notas distintas, como un examen de 0 a 100 puntos, no podemos hacer una fila por cada nota individual porque tendríamos una tabla kilométrica e inútil. Por eso agrupamos los datos en 'Intervalos de Clase'. Calculamos el Rango total (nota mayor menos nota menor), definimos el número de grupos y establecemos una amplitud constante. Cada intervalo tiene su 'Marca de Clase' o punto medio, que es el número representativo de todo ese grupo. En la tabla real en pantalla de 63 docentes, vemos que el grupo con mayor cantidad de docentes es el de 56 a 60 puntos con 16 docentes, y el porcentaje acumulado nos dice de inmediato que el 51.7% obtuvo 70 puntos o menos.",
        "metaphor": "Los intervalos de clase son como las tallas de ropa: en vez de fabricar una camisa para cada milímetro de persona, las agrupamos en Small, Medium y Large para organizarnos mejor.",
        "faq": "¿Qué representa la Marca de Clase en las fórmulas matemáticas? Respuesta: Es el valor promedio del intervalo que se utiliza como representante de todos los datos de ese grupo para calcular la media y la varianza.",
        "pass": "Habiendo organizado las frecuencias, doy paso a mi compañera Mishel Alcázar Valdez para abordar la selección gráfica y detección de anomalías."
    },
    7: {
        "speaker": "Mishel Alcázar Valdez (Expositor 4)",
        "goal": "Demostrar que la escala de medición de la variable impone el tipo de gráfico correcto y exhibir errores metodológicos habituales.",
        "script": "Gracias José María. En investigación científica un gráfico no es un adorno estético; es una herramienta de síntesis visual determinada estrictamente por la escala de medición de la variable. Si medimos una variable cualitativa o categórica (como carreras universitarias o estado civil), debemos usar gráficos de barras con separación entre barra y barra, o un gráfico circular de sectores si hay menos de 5 categorías. Pero si medimos una variable cuantitativa continua (como notas, sueldos o tiempo), es una falta metodológica usar barras separadas; estamos obligados a usar un Histograma, donde las barras están totalmente pegadas porque los valores numéricos no tienen saltos. En pantalla mostramos el error común frente al gráfico técnicamente correcto.",
        "metaphor": "Elegir un gráfico estadístico es como elegir el calzado: no puedes ir a jugar fútbol con zapatos de vestir ni a una cena de gala con zapatillas deportivas.",
        "faq": "¿Por qué las barras de un histograma van unidas? Respuesta: Porque representan variables continuas donde el final de un intervalo coincide inmediatamente con el inicio del siguiente.",
        "pass": "En mi siguiente intervención explicaré el diagrama de caja y bigotes (Boxplot) para la detección de valores atípicos u outliers."
    },
    8: {
        "speaker": "Mishel Alcázar Valdez (Expositor 4 - Cont.)",
        "goal": "Explicar la anatomía del Boxplot y el procedimiento para detectar valores atípicos (outliers) que distorsionan el promedio.",
        "script": "El diagrama de caja y bigotes o Boxplot es la herramienta visual más completa de la estadística descriptiva. En un solo gráfico resume 5 datos fundamentales: el mínimo, el Cuartil 1, la Mediana, el Cuartil 3 y el máximo. La caja encierra al 50% de las personas del medio y su altura se llama Rango Intercuartílico. Pero lo más valioso del Boxplot es su capacidad para detectar 'Outliers' o datos atípicos: aquellos valores que están ridículamente lejos del grupo. En el ejemplo en pantalla, mientras la mayoría de docentes obtuvo entre 50 y 75 puntos, el Sujeto 42 obtuvo 99 puntos. Identificar este dato atípico es vital, porque si lo dejamos sin revisar, alterará el promedio y dará una falsa impresión del rendimiento general.",
        "metaphor": "El dato atípico es como tener a un basquetbolista de la NBA de 2.20 metros en un curso de niños de primaria: si promedias la estatura, creerás que los niños son gigantes.",
        "faq": "¿Qué se hace con un outlier una vez detectado? Respuesta: Se audita el instrumento original para verificar si fue un error de digitación; si el dato es verídico, se reporta y se prefiere usar la mediana en lugar de la media.",
        "pass": "Con los datos verificados y graficados, cedo la palabra a mi compañero Carlos Alberto Choque Serrano para iniciar el análisis cuantitativo inferencial."
    },
    9: {
        "speaker": "Carlos Alberto Choque Serrano (Expositor 5)",
        "goal": "Explicar las 4 fases secuenciales del análisis cuantitativo y la transición de lo descriptivo a lo inferencial.",
        "script": "Muchas gracias Mishel. En el punto 6.6 ingresamos al corazón del análisis cuantitativo. Este análisis no se realiza de forma desordenada; sigue 4 fases secuenciales obligatorias. La Fase 1 es la Limpieza y Exploración: verificar que no haya casillas vacías ni datos disparatados. La Fase 2 es la Descripción: calcular medias, modas y porcentajes para conocer a la muestra. La Fase 3 es la Verificación de Supuestos: comprobar si los datos siguen una distribución normal en forma de campana de Gauss. Y la Fase 4 es la Inferencia Estadística: aplicar pruebas para comprobar si nuestras hipótesis de investigación se cumplen para toda la población. En pantalla pueden observar el diagrama de flujo interactivo de estas 4 fases.",
        "metaphor": "Las 4 fases son como el despegue de un avión: primero revisas los motores (limpieza), carreteas en la pista (descripción), pides permiso a la torre de control (supuestos) y finalmente vuelas a tu destino (inferencia).",
        "faq": "¿Qué ocurre si nos saltamos la fase de supuestos de normalidad? Respuesta: Se corre el riesgo de aplicar pruebas paramétricas incorrectas que llevarían a conclusiones totalmente falsas e inválidas.",
        "pass": "En mi siguiente lámina profundizaré en los modelos estadísticos clásicos: la correlación de Pearson y la regresión lineal."
    },
    10: {
        "speaker": "Carlos Alberto Choque Serrano (Expositor 5 - Cont.)",
        "goal": "Explicar de manera sencilla la correlación de Pearson (r) y la ecuación de regresión lineal para predecir resultados.",
        "script": "Uno de los objetivos más comunes en investigación es responder: ¿estas dos variables están relacionadas? Para eso usamos la Correlación de Pearson, simbolizada con la letra r. Este coeficiente oscila entre -1 y +1. Si da cerca de cero, no hay relación. Si da positivo, como el valor de r = .68 que vemos en pantalla, significa que a mayor cantidad de horas de estudio, mayor es el rendimiento académico. Y si queremos ir más allá y predecir el futuro, construimos una ecuación de Regresión Lineal: Y = 42.5 + 1.45 * X. Esta fórmula nos dice que si un estudiante estudia cero horas, su nota esperada es 42.5; pero por cada hora adicional de estudio, su calificación aumentará en 1.45 puntos. Así convertimos datos en modelos predictivos.",
        "metaphor": "La correlación te dice si dos amigos caminan siempre juntos; la regresión te dice exactamente cuántos pasos dará uno si el otro da diez pasos.",
        "faq": "¿Qué porcentaje de las notas explica el tiempo de estudio en este ejemplo? Respuesta: Se eleva r al cuadrado: (.68)^2 = 0.468, es decir, el 46.8% de la variación en las notas se explica por las horas de estudio.",
        "pass": "Habiendo presentado los modelos estadísticos clásicos, doy paso a mi compañera Dapne Scarlet Salvatierra Nina para abordar la minería de datos y KDD."
    },
    11: {
        "speaker": "Dapne Scarlet Salvatierra Nina (Expositor 6)",
        "goal": "Explicar qué es la minería de datos, el ciclo de 5 fases del proceso KDD y su aplicación en la investigación educativa.",
        "script": "Gracias Carlos. En el punto 6.6 damos un salto cualitativo hacia la Minería de Datos y el proceso KDD, que significa Descubrimiento de Conocimiento en Bases de Datos. En la actualidad, las instituciones educativas almacenan gigabytes de registros de asistencia, calificaciones y uso de plataformas virtuales. La minería de datos utiliza algoritmos avanzados para encontrar patrones ocultos que ningún ser humano podría descubrir mirando tablas comunes. El proceso KDD tiene 5 etapas: seleccionar los datos pertinentes, limpiarlos, transformarlos, aplicar algoritmos de minería y, finalmente, interpretar los resultados. En el ejemplo en pantalla, el sistema detecta tempranamente patrones de estudiantes en riesgo de deserción antes de que reprueben.",
        "metaphor": "La minería de datos es como buscar pepitas de oro en el lecho de un río: tienes que cribar toneladas de arena y lodo (datos brutos) para quedarte con las joyas valiosas de conocimiento.",
        "faq": "¿En qué se diferencia la estadística clásica de la minería de datos? Respuesta: La estadística clásica prueba hipótesis preconcebidas por el investigador; la minería de datos descubre relaciones novedosas e inesperadas dentro de grandes volúmenes de información.",
        "pass": "A continuación, en mi segunda lámina, explicaré la selección de modelos predictivos y la advertencia metodológica sobre la causalidad."
    },
    12: {
        "speaker": "Dapne Scarlet Salvatierra Nina (Expositor 6 - Cont.)",
        "goal": "Advertir con firmeza sobre la falacia de confundir correlación con causalidad y explicar los peligros del sobreajuste (overfitting).",
        "script": "Al construir modelos predictivos, el investigador debe estar alerta ante dos peligros metodológicos. El primero es el 'Sobreajuste' o Overfitting: cuando el modelo se aprende los datos de memoria como un estudiante que solo memoriza las respuestas del examen; si le cambiamos una pregunta en la realidad, fracasa. El segundo peligro, y el más grave, es la falacia de confundir correlación con causalidad. Que dos variables se muevan juntas no significa que una cause la otra. Existe un ejemplo clásico: el consumo de helados y las muertes por ahogamiento aumentan al mismo tiempo; ¿comer helado hace que la gente se ahogue? ¡No! La causa real es una tercera variable: el calor del verano. Para afirmar causalidad se exige asociación, precedencia en el tiempo y descartar variables extrañas.",
        "metaphor": "Confundir correlación con causalidad es como creer que el gallo hace salir el sol solo porque canta todas las mañanas unos minutos antes del amanecer.",
        "faq": "¿Cuáles son las 3 condiciones para demostrar causalidad? Respuesta: 1) Asociación estadística demostrada, 2) Precedencia temporal (la causa ocurre antes que el efecto), y 3) No espuriedad (ausencia de terceras variables que expliquen la relación).",
        "pass": "Para iniciar el Bloque 4 correspondiente al software computacional, cedo la palabra a mi compañero Yord Gember Rojas Rocha para exponer el uso de IBM SPSS."
    },
    13: {
        "speaker": "Yord Gember Rojas Rocha (Expositor 7)",
        "goal": "Explicar la arquitectura de IBM SPSS Statistics, diferenciando claramente la Vista de Variables de la Vista de Datos.",
        "script": "Muchas gracias Dapne. En el punto 6.7 entramos al procesamiento computarizado con IBM SPSS Statistics, el estándar internacional en ciencias sociales y de la salud. Para que SPSS procese los datos sin errores, el investigador debe dominar sus dos entornos de trabajo. En primer lugar, la 'Vista de Variables': es la ficha técnica donde bautizamos cada variable, le asignamos su etiqueta descriptiva, declaramos qué números representan a las categorías y definimos el nivel de medición (nominal, ordinal o escala). En segundo lugar, la 'Vista de Datos': es la planilla donde se vacían las respuestas reales fila por fila. En el simulador interactivo de la lámina pueden alternar entre ambas vistas para apreciar cómo la configuración técnica de la variable gobierna los datos ingresados.",
        "metaphor": "La Vista de Variables es como armar el molde de una torta; la Vista de Datos es verter los ingredientes reales dentro de ese molde.",
        "faq": "¿Qué ocurre si defino una variable continua como nominal en SPSS? Respuesta: SPSS restringirá los análisis matemáticos, impidiendo calcular medias y desviaciones estándar sobre esa variable.",
        "pass": "En mi siguiente lámina explicaré la lectura rigurosa de una salida de SPSS y la interpretación científica del p-valor."
    },
    14: {
        "speaker": "Yord Gember Rojas Rocha (Expositor 7 - Cont.)",
        "goal": "Explicar cómo se interpreta una tabla de correlación en SPSS y cómo se lee correctamente el p-valor frente al umbral Alfa = 0.05.",
        "script": "Cuando SPSS termina de calcular, genera una tabla de resultados como la que ven en pantalla. Lo fundamental ante un jurado evaluador es saber leer la fila de 'Sig. bilateral', que representa el p-valor. El p-valor es la probabilidad de que los resultados obtenidos sean producto de la pura casualidad. En ciencia establecemos un umbral estricto llamado Alfa, normalmente fijado en 0.05, es decir, el 5%. Si el p-valor es menor a 0.05, como en nuestra tabla donde figura .000 (reportado formalmente en normas APA como p < .001), rechazamos la Hipótesis Nula y confirmamos que la relación entre las variables es estadísticamente real y comprobada. Si el p-valor fuera mayor a 0.05, no tendríamos evidencia suficiente y no podríamos afirmar nada.",
        "metaphor": "El p-valor es como el veredicto en un juicio: si la probabilidad de inocencia por azar cae por debajo del 5%, la evidencia es contundente para dictar sentencia.",
        "faq": "¿Por qué en APA 7 nunca se escribe 'p = 0.000'? Respuesta: Porque una probabilidad nunca es exactamente cero; se debe escribir 'p < .001' indicando que es infinitesimalmente pequeña.",
        "pass": "Habiendo cubierto el procesamiento cuantitativo en SPSS, doy paso a mi compañero Rodrigo Arauz Mercado para abordar el análisis cualitativo en ATLAS.ti."
    },
    15: {
        "speaker": "Rodrigo Arauz Mercado (Expositor 8)",
        "goal": "Fundamentar el enfoque cualitativo computarizado y explicar los 4 componentes de la Unidad Hermenéutica en ATLAS.ti.",
        "script": "Muchas gracias Yord. En el punto 6.7 damos paso a la otra mitad indispensable de la investigación científica: el análisis cualitativo mediante ATLAS.ti. Los números de SPSS nos dicen 'cuánto' ocurre un fenómeno, pero las palabras en ATLAS.ti nos revelan 'por qué' y 'cómo' lo viven los protagonistas. El corazón de ATLAS.ti es la Unidad Hermenéutica, un proyecto digital que articula 4 componentes: 1) Los Documentos Primarios, que son las entrevistas transcritas; 2) Las Citas, que son fragmentos textuales seleccionados por su fuerza testimonial; 3) Los Códigos, que son etiquetas conceptuales que colocamos a esos fragmentos; y 4) Los Memos, donde el investigador anota sus reflexiones teóricas. En pantalla pueden explorar interactivamente cada uno de estos 4 componentes.",
        "metaphor": "Analizar con ATLAS.ti es como ser un detective: subrayas las pistas en las declaraciones de los testigos (citas), les pones un nombre (códigos) y conectas las pistas en tu pizarra de investigación.",
        "faq": "¿Cuál es la diferencia entre un código cuantitativo y uno cualitativo? Respuesta: En lo cuantitativo un código es un número asignado previamente; en lo cualitativo es una categoría conceptual que surge de la interpretación del discurso de las personas.",
        "pass": "En mi siguiente lámina explicaré la construcción de redes semánticas en ATLAS.ti y la triangulación metodológica."
    },
    16: {
        "speaker": "Rodrigo Arauz Mercado (Expositor 8 - Cont.)",
        "goal": "Explicar la construcción de redes semánticas en ATLAS.ti y cómo se logra la triangulación entre lo cualitativo y lo cuantitativo.",
        "script": "Una de las mayores virtudes de ATLAS.ti es permitir la codificación axial mediante Redes Semánticas. Una red semántica es un mapa conceptual visual donde conectamos las categorías teóricas con vínculos que tienen significado explícito: 'es causa de', 'está asociado con' o 'contradice'. Como observamos en la red interactiva en pantalla, los testimonios revelan que la 'Sobrecarga de trabajo' es causa de 'Estrés Docente', lo que impacta negativamente en el 'Rendimiento en el aula', mientras que el 'Apoyo familiar' actúa como un factor protector. Lo trascendental ante este jurado es la 'Triangulación Metodológica': no nos quedamos solo con los porcentajes de SPSS ni solo con las palabras de ATLAS.ti; unimos ambos enfoques para construir una investigación con rigor y profundidad.",
        "metaphor": "La triangulación metodológica es como la visión de los dos ojos humanos: un ojo te da la luz y la distancia (SPSS) y el otro te da la profundidad y los colores (ATLAS.ti); juntos te dan la realidad completa en 3D.",
        "faq": "¿Qué validez científica tiene una red semántica? Respuesta: Permite la trazabilidad conceptual: cualquier evaluador puede hacer clic en un nodo y leer directamente las citas textuales de los participantes que respaldan esa conexión teórica.",
        "pass": "Para finalizar nuestra defensa oral, paso a exponer junto a todo el equipo la síntesis y conclusiones metodológicas generales."
    },
    17: {
        "speaker": "Rodrigo Arauz Mercado y Equipo de Investigación",
        "goal": "Presentar la conclusión metodológica colegiada de alto impacto, sintetizando los 4 grandes aprendizajes y las referencias en APA 7.",
        "script": "Para concluir nuestra defensa formal ante el Licenciado Marcial Villarroel Siles, queremos sintetizar los 4 grandes aprendizajes metodológicos del ciclo: 1) En Tabulación aprendimos que el orden y el libro de códigos son los cimientos de la auditoría; 2) En Sistematización y Gráficos comprobamos que las frecuencias válidas y el respeto a las escalas evitan distorsiones visuales; 3) En Modelado y SPSS confirmamos que la significancia estadística p < 0.05 nos da certeza científica frente a la casualidad; y 4) En ATLAS.ti recuperamos el significado humano de las vivencias de los sujetos. Concluimos con la regla de oro metodológica: 'Los softwares computacionales procesan datos; pero es el investigador quien razona, contrasta y produce conocimiento científico al servicio de la sociedad'. Quedamos a su disposición. Muchas gracias.",
        "metaphor": "Investigar no es llenar casillas en una computadora; es responder preguntas reales para solucionar problemas reales de nuestra comunidad.",
        "faq": "¿Cómo se garantiza la calidad total de una investigación mixta? Respuesta: Mediante la consistencia metodológica: coherencia estricta entre el problema, los objetivos, la recolección, el procesamiento estadístico en SPSS y la interpretación teórica en ATLAS.ti.",
        "pass": "Concluimos formalmente la defensa oral del informe metodológico. ¡Muchas gracias por su atención!"
    }
}
