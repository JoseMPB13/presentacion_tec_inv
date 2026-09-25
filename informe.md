Introducción
La investigación científica busca responder preguntas y resolver problemas prácticos y teóricos mediante la recolección y el análisis riguroso de información. Sin embargo, los datos que se obtienen directamente de cuestionarios, entrevistas, pruebas o mediciones no hablan por sí solos. Para que estas respuestas se conviertan en conocimiento confiable y útil, es indispensable aplicar un proceso ordenado que las organice, las resuma, descubra patrones ocultos y permita interpretarlas con claridad (Hernández-Sampieri et al., 2014).
Este camino metodológico comprende cuatro fases interconectadas: en primer lugar, la tabulación, que consiste en ordenar y limpiar las respuestas dentro de una tabla rectangular organizada llamada matriz de datos (Pardo & Ruiz, 2005); en segundo lugar, la sistematización gráfica y estadística, que agrupa los datos en tablas de frecuencias y gráficos específicos para ver cómo se comportan sin cometer errores de lectura; en tercer lugar, el análisis mediante modelos de detección de patrones, que va desde estadísticas clásicas de correlación y predicción hasta algoritmos de minería de datos (KDD) y análisis cualitativo inductivo (Hernández Orallo et al., 2004; San Martín, 2014); y, finalmente, la interpretación en herramientas informáticas como IBM SPSS (para análisis numérico e inferencial) y ATLAS.ti (para análisis textual y conceptual) (ATLAS.ti Scientific Software Development GmbH, 2023).
El propósito de este informe es presentar estos fundamentos con el máximo rigor metodológico, pero con una redacción directa, fluida y transparente, eliminando la jerga innecesariamente enrevesada y explicando paso a paso cada concepto matemático y conceptual. Asimismo, se incluye una sección dedicada a clarificar y definir en detalle los términos técnicos clave, garantizando una comprensión integral tanto para investigadores en formación como para evaluadores académicos, bajo los estándares de citación de las normas APA (7.ª edición).

1. Tabulación de datos
   1.1 Concepto, finalidad y rol metodológico
   La tabulación de datos es el procedimiento mediante el cual las respuestas o puntuaciones obtenidas a través de los instrumentos de medición se cuentan, clasifican y organizan de forma sistemática en tablas ordenadas (Hernández-Sampieri et al., 2014). Funciona como un puente indispensable entre el trabajo de campo (cuando se aplican encuestas o exámenes) y el análisis estadístico (cuando se extraen conclusiones) (Pardo & Ruiz, 2005). Si los datos no se tabulan primero, es imposible aplicar fórmulas estadísticas o calcular promedios de manera confiable.
   Finalidad analítica: La tabulación cumple tres objetivos fundamentales en la investigación:
1. Resumir y condensar la información: Permite que cientos o miles de respuestas aisladas se resuman en una estructura compacta y fácil de leer.
1. Limpieza y control de errores: Hace visible si hubo errores de llenado, preguntas mal marcadas o números fuera de lugar para corregirlos a tiempo.
1. Asegurar cálculos exactos: Permite separar las respuestas reales de las preguntas que los participantes dejaron en blanco, asegurando que los porcentajes se calculen únicamente sobre quienes respondieron de verdad (Pardo & Ruiz, 2005).
   En términos sencillos, el flujo de trabajo sigue tres pasos continuos: primero se recolectan las respuestas en el campo, luego se codifican (asignando un número a cada opción de respuesta) y finalmente se tabulan (organizando los números en una tabla general para su cálculo) (Hernández-Sampieri et al., 2014).
   1.2 Datos brutos frente a datos organizados
   Es esencial diferenciar entre los datos brutos y los datos organizados (Pardo & Ruiz, 2005):
   • Datos brutos (raw data): Son las respuestas tal cual se recogen de los cuestionarios o formatos de campo, dispersas y sin clasificar. En este estado resulta imposible sacar conclusiones claras, pues la información es caótica y propensa a confusiones (Hernández-Sampieri et al., 2014).
   • Datos organizados o tabulados: Es la información una vez que ha sido revisada, agrupada y estructurada por categorías. En los datos organizados ya se puede observar con facilidad cuántas personas respondieron cada opción, qué porcentaje representa cada grupo y qué tendencias predominan en el estudio (Pardo & Ruiz, 2005).
   1.3 Codificación técnica y estructura formal de la matriz de datos
   La codificación consiste en convertir las respuestas escritas o verbales en números para que un programa de computadora (como Excel o SPSS) pueda procesarlas matemáticamente (Pardo & Ruiz, 2005). Por ejemplo, si se pregunta el género, se asigna el número 1 a 'Masculino' y el número 2 a 'Femenino'. En preguntas con escalas de opinión (escalas Likert), se asignan números del 1 al 5, donde 1 significa 'Totalmente en desacuerdo' y 5 significa 'Totalmente de acuerdo'. Cuando se trata de preguntas abiertas (donde la persona responde con sus propias palabras), primero se leen todas las respuestas, se identifican las ideas que más se repiten y luego se crea un código numérico para cada idea común (Hernández-Sampieri et al., 2014).
   Una vez codificadas las respuestas, se construyen dentro de una **matriz de datos**. Esta matriz es una tabla rectangular perfecta formada por tres componentes indispensables (Pardo & Ruiz, 2005):
1. Filas (Casos o Participantes): Cada fila horizontal corresponde a una persona, participante o caso del estudio. Si en la investigación participaron 100 personas, la matriz tendrá exactamente 100 filas (N = 100).
1. Columnas (Variables o Ítems): Cada columna vertical representa una pregunta, variable o característica medida (por ejemplo: edad, género, salario, puntaje en una prueba).
1. Celdas (Intersección): Es el punto exacto donde se cruza una fila y una columna. En cada celda solo puede existir un único número, que representa la respuesta exacta de ese participante en esa pregunta específica.
   1.4 Tratamiento de los valores perdidos (Missing Data)
   En la investigación científica, una matriz de datos debe ser rectangular y completa: no deben quedar celdas vacías (Pardo & Ruiz, 2005). Si una celda se deja en blanco en programas como IBM SPSS, el software asumirá que es un 'valor perdido por el sistema' (mostrado con un punto). Esto puede causar problemas graves, pues el programa podría eliminar automáticamente a ese participante de análisis posteriores más avanzados (Hernández-Sampieri et al., 2014).
   Códigos numéricos de usuario: Para evitar esto, el investigador debe asignar códigos numéricos especiales que expliquen con claridad por qué no hay un dato en esa casilla:
   • Código 8 u 88 ('No aplica'): Se utiliza cuando una pregunta no le correspondía a la persona (por ejemplo, preguntar sobre hijos a alguien que previamente contestó que no tiene hijos).
   • Código 9 o 99 ('No contestó' o 'No sabe'): Se asigna cuando la persona vio la pregunta pero prefirió no contestar o dijo no saber la respuesta.
   • Código 4 o 44 ('Respuesta inválida'): Se registra cuando el participante marcó dos opciones en una pregunta que solo permitía una, o cuando la respuesta fue ilegible.
   Al indicar al software qué significan estos números, el programa sabe que debe excluirlos al momento de calcular promedios y porcentajes, evitando distorsionar la realidad (Pardo & Ruiz, 2005). La Tabla 1 ilustra cómo se presenta una tabla de frecuencias donde se discriminan correctamente los datos válidos de las omisiones.
   Tabla 1. Distribución de frecuencias con discriminación de valores perdidos (Satisfacción con la infraestructura tecnológica).
   Categoría de Respuesta
   Código
   Frecuencia (f)
   Porcentaje Total (%)
   Porcentaje Válido (%)
   Porcentaje Acumulado (%)
   Insatisfecho
   1
   2
   20.0
   25.0
   25.0
   Satisfecho
   2
   5
   50.0
   62.5
   87.5
   Muy Satisfecho
   3
   1
   10.0
   12.5
   100.0
   Subtotal de Respuestas Válidas
   —
   8
   80.0
   100.0
   —
   No contestó (Valor perdido)
   8
   1
   10.0
   Excluido
   —
   Error de marcación (Valor perdido)
   9
   1
   10.0
   Excluido
   —
   Total de la Muestra
   —
   10
   100.0
   —
   —

Nota: Muestra piloto de N = 10 participantes. Obsérvese que al descontar las 2 omisiones (códigos 8 y 9), el porcentaje válido se calcula sobre 8 personas reales, mostrando que el 87.5% de quienes respondieron válidamente está Satisfecho o Muy Satisfecho (Hernández-Sampieri et al., 2014; Pardo & Ruiz, 2005).
1.5 Tabulación cruzada y tablas de contingencia bidimensionales
Cuando el objetivo de la investigación es analizar cómo se relacionan dos variables cualitativas al mismo tiempo, se utiliza una **tabla de tabulación cruzada** o **tabla de contingencia** (Hernández-Sampieri et al., 2014). Se trata de una tabla de doble entrada donde las categorías de una variable se colocan en las filas y las categorías de la otra variable se colocan en las columnas (Pardo & Ruiz, 2005).
En el interior de la tabla se muestran las frecuencias observadas (cuántas personas cumplen ambas condiciones a la vez) y los porcentajes calculados sobre el total de cada fila o de cada columna. Este tipo de tabla es el paso previo indispensable para calcular pruebas de asociación estadística, como la prueba Chi-cuadrada (Pardo & Ruiz, 2005). La Tabla 2 presenta un ejemplo claro de cruce entre género y el uso de entornos virtuales.
Tabla 2. Tabla de contingencia bidimensional 2 × 2 con recuentos y porcentajes de fila.
Género de los Docentes (Filas)
Usa Entorno Virtual: SÍ
Usa Entorno Virtual: NO
Total por Fila
Masculino
40 (57.1%)
30 (42.9%)
70 (100.0%)
Femenino
60 (75.0%)
20 (25.0%)
80 (100.0%)
Total por Columna
100 (66.7%)
50 (33.3%)
150 (100.0%)

Nota: Muestra de N = 150 docentes. Al leer los porcentajes de cada fila, se aprecia que el 75.0% de las docentes mujeres utiliza entornos virtuales, frente al 57.1% de los docentes varones (Pardo & Ruiz, 2005). 2. Sistematización de datos en tablas y gráficos estadísticos
2.1 Distribución de frecuencias completa: los 5 elementos clave
Sistematizar los datos significa organizarlos de manera ordenada y metódica para poder interpretarlos con facilidad (Hernández-Sampieri et al., 2014). En lugar de tener una lista interminable de calificaciones individuales, se crea una tabla de frecuencias que resume la distribución de las respuestas en cinco columnas indispensables (Pardo & Ruiz, 2005):

1. Categorías o Intervalos: Son las distintas opciones o rangos de puntuaciones que puede tomar la variable estudiada.
2. Frecuencia Absoluta (f): Es el conteo directo de cuántas personas u observaciones cayeron exactamente en esa categoría.
3. Porcentaje Total (%): Indica qué parte del total general de la muestra representa esa categoría, calculándose sobre todos los casos recolectados (incluyendo quienes no respondieron): Porcentaje = (f / Total General) × 100.
4. Porcentaje Válido (%): Es el porcentaje recalculado únicamente sobre las personas que respondieron de forma válida, descontando a quienes dejaron la pregunta vacía. Es el porcentaje más importante para interpretar los resultados reales.
5. Porcentaje Acumulado (%): Es la suma acumulada de los porcentajes válidos, sumando fila por fila desde la primera opción hasta la última. Permite responder de inmediato preguntas como: ¿Qué porcentaje del grupo obtuvo una calificación menor o igual a 70 puntos? (Pardo & Ruiz, 2005).
   2.2 Criterios para agrupar datos continuos en intervalos de clase
   Cuando se evalúan variables numéricas con muchas calificaciones distintas (por ejemplo, notas de 0 a 100 o salarios mensuales), hacer una fila para cada número individual generaría una tabla gigantesca y confusa (Pardo & Ruiz, 2005). Para solucionarlo, las puntuaciones se agrupan en **intervalos de clase** (tramos de puntuación) siguiendo estos pasos sencillos (Hernández-Sampieri et al., 2014):
   a) Calcular el Rango Total: Se resta la calificación más baja de la más alta (Rango = Nota Máxima - Nota Mínima).
   b) Definir la cantidad de intervalos: Se divide el rango en una cantidad práctica de grupos, habitualmente entre 5 y 15 grupos.
   c) Mantener la misma amplitud: Todos los intervalos deben tener exactamente el mismo ancho de puntos para no distorsionar las comparaciones.
   d) Calcular la Marca de Clase (Punto Medio): Es el número intermedio de cada intervalo, calculado sumando el límite inferior y el superior y dividiéndolo entre 2. Este valor representa a todo el grupo al momento de calcular promedios o trazar gráficos.
   La Tabla 3 muestra cómo se organiza una evaluación docente de 0 a 100 puntos en tramos de 5 en 5 puntos.
   Tabla 3. Distribución de frecuencias agrupada en intervalos con marcas de clase (Desempeño pedagógico).
   Intervalos de Calificación
   Punto Medio (Marca de Clase)
   Frecuencia Absoluta (f)
   Porcentaje Total (%)
   Porcentaje Válido (%)
   Porcentaje Acumulado (%)
   55 o menos puntos
   52.5
   3
   4.8
   5.0
   5.0
   56 a 60 puntos
   58.0
   16
   25.4
   26.7
   31.7
   61 a 65 puntos
   63.0
   9
   14.3
   15.0
   46.7
   66 a 70 puntos
   68.0
   3
   4.8
   5.0
   51.7
   71 a 75 puntos
   73.0
   7
   11.1
   11.7
   63.3
   76 a 80 puntos
   78.0
   9
   14.3
   15.0
   78.3
   81 a 85 puntos
   83.0
   4
   6.3
   6.7
   85.0
   86 a 90 puntos
   88.0
   9
   14.3
   15.0
   100.0
   Subtotal de Evaluaciones Válidas
   —
   60
   95.2
   100.0
   —
   Omisión / Sin examen (Perdido)
   —
   3
   4.8
   Excluido
   —
   Total de la Muestra
   —
   63
   100.0
   —
   —

Nota: Muestra de N = 63 docentes evaluados. La calificación más frecuente se ubica en el intervalo 56-60 puntos (16 docentes). Al revisar la columna de porcentaje acumulado, se observa que exactamente el 51.7% de los docentes obtuvo 70 puntos o menos (Hernández-Sampieri et al., 2014; Pardo & Ruiz, 2005).
2.3 Selección de gráficos según la escala de medición de la variable
Un gráfico estadístico no es una simple ilustración decorativa; es una herramienta analítica diseñada para mostrar con rapidez si las puntuaciones están concentradas en el centro, si están dispersas o si hay calificaciones extrañas (Pardo & Ruiz, 2005). La regla de oro metodológica establece que **el tipo de variable determina obligatoriamente qué gráfico se debe utilizar** (Hernández-Sampieri et al., 2014):
A. Gráficos para variables cualitativas o categóricas: Se utilizan para datos que representan categorías o nombres (ej. género, profesión, nivel de satisfacción):
• Gráfico de Barras: Rectángulos verticales u horizontales donde la altura representa la cantidad o porcentaje de personas. Regla técnica fundamental: las barras deben estar separadas entre sí por un espacio en blanco para indicar visualmente que cada categoría es independiente y separada de las demás.
• Gráfico de Sectores (Pastel): Círculo dividido en porciones proporcionales al porcentaje de cada grupo. Regla de uso: solo debe usarse cuando la variable tiene pocas categorías (máximo entre 3 y 5) y cuando todas las categorías juntas suman exactamente el 100%. No debe usarse para variables numéricas ni preguntas de respuesta múltiple (Hernández-Sampieri et al., 2014).
B. Gráficos para variables cuantitativas continuas: Se utilizan para variables numéricas que provienen de mediciones o escalas continuas (ej. peso, notas, tiempo, ingresos):
• Histograma: Similar a las barras, pero con una diferencia esencial: las barras están completamente unidas entre sí (sin espacio interbarras). Esta unión gráfica expresa que los números continúan de manera ininterrumpida a lo largo de la escala de medición (Pardo & Ruiz, 2005).
• Polígono de Frecuencias: Gráfico de líneas que se construye uniendo con trazos rectos los puntos medios superiores (marcas de clase) de cada barra del histograma. Es especialmente útil para comparar dos o más grupos sobre el mismo gráfico.
2.4 Diagrama de caja y bigotes (Boxplot) y detección de valores atípicos
El diagrama de caja y bigotes (_Boxplot_) es una de las herramientas visuales más útiles de la estadística, ya que resume el comportamiento de una variable numérica a través de cinco cifras fundamentales (Pardo & Ruiz, 2005):

1. La Caja Central: Es un rectángulo que encierra exactamente al 50% de las personas del estudio (las que están en la parte central de la distribución). Su base inferior es el Cuartil 1 (Percentil 25) y su parte superior es el Cuartil 3 (Percentil 75). La altura de la caja se llama Rango Intercuartílico (IQR = Q_3 - Q_1).
2. La Línea Mediana (Cuartil 2): Es una línea horizontal ubicada dentro de la caja que divide al grupo exactamente en dos mitades (50% por encima y 50% por debajo). Si la línea está en el centro de la caja, las notas están balanceadas de forma simétrica; si está más cerca de la base, revela que la mayoría obtuvo notas bajas (asimetría positiva).
3. Los Bigotes: Son líneas que salen de la caja hacia arriba y hacia abajo para señalar las puntuaciones máximas y mínimas normales dentro del grupo estudiado.
4. Valores Atípicos (Outliers): Son puntuaciones tan alejadas del resto del grupo que se consideran casos raros o extraordinarios. Si están a una distancia moderada (entre 1.5 y 3 veces el tamaño de la caja), se dibujan como pequeños círculos (o). Si están a una distancia extrema (más de 3 veces el tamaño de la caja), se dibujan como asteriscos (\*). Detectar estos casos a tiempo es crucial porque una nota absurdamente alta o baja puede alterar el promedio y distorsionar las conclusiones (Pardo & Ruiz, 2005).
   2.5 Errores metodológicos comunes en la elaboración de gráficos
   Al construir gráficos para informes formales se deben evitar fallas comunes que confunden al lector (Hernández-Sampieri et al., 2014):
   • Sobrecarga en gráficos de pastel: Usar gráficos de pastel para variables numéricas continuas o con más de 6 opciones, convirtiendo el gráfico en una rueda incomprensible.
   • Separar barras en un histograma: Separar las barras al graficar una variable cuantitativa continua, lo cual confunde al lector haciéndole creer que los números están fragmentados como si fueran palabras.
   • Cortar el eje vertical: Iniciar la escala vertical en un número distinto de cero sin avisar, lo que provoca que diferencias muy pequeñas parezcan enormes a simple vista.
   • Efectos tridimensionales innecesarios (3D): Añadir efectos de volumen 3D o sombras inclinadas en gráficos de barras o pastel. Esto no aporta ningún valor científico y engaña al ojo humano sobre el tamaño real de los porcentajes (Pardo & Ruiz, 2005).
5. Análisis de datos con apoyo de modelos para detección de patrones
   3.1 Propósito del análisis y las cuatro fases secuenciales
   El análisis de datos es la etapa en la cual las cifras organizadas en la matriz se procesan estadísticamente para responder a las preguntas y objetivos de la investigación (Hernández-Sampieri et al., 2014). Su meta es transformar números aislados en conocimiento comprobado, reduciendo la incertidumbre y calculando el margen de error de los hallazgos (Pardo & Ruiz, 2005).
   Para realizar un análisis cuantitativo formal, la investigación debe avanzar a través de cuatro etapas obligatorias (Hernández-Sampieri et al., 2014):
   Paso 1. Exploración y limpieza preliminar: Se revisa la base de datos en el computador para corregir errores de dedo y resolver los valores en blanco.
   Paso 2. Descripción individual de variables: Se calculan las frecuencias, promedios (media), puntuaciones intermedias (mediana) y el grado de dispersión (desviación estándar) de cada variable por separado.
   Paso 3. Evaluación de la confiabilidad del instrumento: Antes de probar hipótesis complejas, se debe demostrar que el cuestionario o prueba mide de manera precisa y consistente. En escalas de actitud o encuestas, el indicador más utilizado es el Coeficiente Alfa de Cronbach, exigiéndose valores superiores a 0.70 u 0.80 para considerar que el instrumento es confiable (Hernández-Sampieri et al., 2014).
   Paso 4. Comprobación de hipótesis e inferencia: Se aplican pruebas estadísticas para comprobar si los resultados encontrados en el grupo de participantes se pueden generalizar con seguridad a toda la población (Pardo & Ruiz, 2005).
   3.2 Modelos estadísticos tradicionales de relación y predicción
   Cuando se busca entender cómo se relacionan dos o más variables numéricas, se recurre a la correlación y a la regresión lineal (Pardo & Ruiz, 2005):
   • Coeficiente de Correlación de Pearson (r): Mide qué tan asociadas están dos variables numéricas continuas (por ejemplo: horas de estudio y calificación en el examen). Su valor siempre oscila entre -1.00 y +1.00. Si el valor es cercano a 0.00, no hay relación lineal. Si es positivo (ej. +0.70), significa que al aumentar una variable, la otra también aumenta. Si es negativo (ej. -0.70), significa que al aumentar una variable, la otra disminuye. Si este coeficiente se eleva al cuadrado (r²), se obtiene el Coeficiente de Determinación, que indica qué porcentaje de una variable se explica por la otra (Pardo & Ruiz, 2005).
   • Coeficiente de Correlación de Spearman (rho): Es la versión que se utiliza cuando las variables están en un orden de jerarquía (escala ordinal) o cuando los datos no tienen una forma acampanada normal (Hernández-Sampieri et al., 2014).
   • Regresión Lineal (Simple y Múltiple): Permite predecir el comportamiento de una variable de resultado (criterio, Y) a partir de una o más variables predictoras (X). Por ejemplo, un modelo de regresión permite predecir el rendimiento académico de un estudiante según sus horas de estudio y su asistencia a clases, calculando el impacto específico de cada predictor mediante una ecuación matemática clara (Pardo & Ruiz, 2005).
   3.3 Minería de datos y el proceso KDD (Descubrimiento de Conocimiento en Bases de Datos)
   En la actualidad, cuando se trabaja con grandes cantidades de información, el análisis de datos no se limita a contrastar hipótesis sencillas. La **minería de datos** permite descubrir patrones ocultos mediante algoritmos informáticos (Hernández Orallo et al., 2004). Según estos autores, un **patrón** es una regularidad o estructura descubierta en los datos que cumple cuatro condiciones básicas:
6. Válido: Que siga funcionando con precisión cuando se aplique a datos nuevos del futuro.
7. Novedoso: Que revele algo que no se sabía con anticipación.
8. Potencialmente útil: Que sirva para tomar decisiones o realizar mejoras concretas en la práctica.
9. Comprensible: Que los investigadores puedan entender su lógica y explicarlo con facilidad.
   El proceso general para descubrir estos patrones se denomina **KDD** (_Knowledge Discovery in Databases_), el cual comprende cinco etapas secuenciales: 1) Recopilar e integrar bases de datos dispersas; 2) Limpiar y preparar los datos eliminando errores; 3) Aplicar algoritmos de minería de datos para extraer los modelos; 4) Evaluar e interpretar si los patrones descubiertos tienen sentido real; y 5) Utilizar ese nuevo conocimiento en la toma de decisiones (Hernández Orallo et al., 2004).
   3.4 Modelos avanzados: agrupamiento, árboles de decisión y reglas de asociación
   Existen tres técnicas muy conocidas para descubrir patrones en bases de datos (Hernández Orallo et al., 2004):
   A. Agrupamiento o Clustering (K-medias): Se utiliza cuando no se conoce de antemano a qué grupo pertenece cada persona. El algoritmo K-medias junta a los participantes en grupos de manera automática, de modo que los miembros de un mismo grupo sean lo más parecidos entre sí y lo más diferentes posible de los otros grupos. Es muy útil, por ejemplo, para descubrir perfiles de estudiantes con características similares de aprendizaje.
   B. Árboles de Decisión: Son modelos que clasifican y predicen resultados dividiendo los datos mediante preguntas sucesivas en forma de ramas de árbol (como algoritmos C4.5 o CART). Su gran ventaja es que se expresan en reglas lógicas muy fáciles de entender del tipo SI... ENTONCES (por ejemplo: 'SI el docente tiene más de 10 años de experiencia Y cuenta con posgrado, ENTONCES su nivel de desempeño es Alto').
   C. Reglas de Asociación: Técnicas diseñadas originalmente para ver qué productos se compran juntos en el supermercado, y que en investigación sirven para descubrir eventos que suelen ocurrir al mismo tiempo (ejemplo: 'Si un alumno reprueba la materia A, existe un 80% de probabilidad de que repruebe la materia B'). Se evalúan a través del Soporte (qué tan frecuente es esa combinación en general) y la Confianza (qué tan seguro es que ocurra la segunda cosa si ya ocurrió la primera) (Hernández Orallo et al., 2004).
   3.5 Detección de patrones cualitativos: Teoría Fundamentada y saturación
   Es fundamental contrastar la minería de datos con la forma en que se descubren patrones en la investigación cualitativa, guiada por la **Teoría Fundamentada** (_Grounded Theory_) (San Martín, 2014). Mientras que la minería de datos busca patrones numéricos mediante fórmulas matemáticas, la investigación cualitativa busca patrones de significado en las palabras, relatos y experiencias de las personas.
   En este enfoque se aplica el **Método de las Comparaciones Constantes**, donde el investigador lee y compara continuamente las entrevistas mediante tres niveles de análisis (San Martín, 2014):
10. Codificación Abierta: Se leen los textos, se seleccionan frases con significado importante (citas) y se les coloca una etiqueta conceptual breve (código).
11. Codificación Axial: Se conectan los códigos entre sí, identificando causas, contextos y consecuencias para agruparlos en categorías más amplias.
12. Codificación Selectiva: Se identifica la categoría central o idea maestra que explica todo el fenómeno investigado.
    Este análisis termina cuando se alcanza la **Saturación Teórica**: momento en el cual seguir haciendo más entrevistas o leyendo más documentos ya no aporta ninguna idea nueva a las categorías construidas (San Martín, 2014).
    3.6 Advertencia crítica: ¿Por qué correlación o patrón no significa causalidad?
    Tanto en la estadística clásica (Hernández-Sampieri et al., 2014; Pardo & Ruiz, 2005) como en la minería de datos (Hernández Orallo et al., 2004), existe una regla de oro irrenunciable: **que dos cosas ocurran juntas o tengan una alta correlación no significa que una cause la otra**.
    ■ ADVERTENCIA METODOLÓGICA CRÍTICA: COVARIACIÓN NO ES CAUSALIDAD
    Que dos variables se muevan al mismo tiempo solo demuestra que están asociadas en los datos observados. Por ejemplo, en los meses de verano aumenta la venta de helados y también aumenta la cantidad de personas que se ahogan en piscinas; sin embargo, comer helado no causa ahogamientos. Existe una tercera variable oculta que explica ambas cosas: el calor del verano. A esta coincidencia aparente sin relación de causa se le llama relación espuria.

Para que la ciencia acepte formalmente que una variable X es la causa real de un efecto Y, se deben cumplir obligatoriamente cuatro condiciones rigurosas (Hernández-Sampieri et al., 2014; Pardo & Ruiz, 2005):

1. Demostrar la relación estadística: Las dos variables deben variar juntas de forma estadísticamente comprobada.
2. Precedencia en el tiempo: La causa (X) debe ocurrir antes en el tiempo que el efecto (Y). Si ambas cosas se miden en el mismo instante, no se puede asegurar cuál provocó a cuál.
3. Eliminar explicaciones alternativas: Se debe descartar que exista una tercera variable oculta responsable de la relación, mediante un diseño de investigación controlado o técnicas estadísticas de control.
4. Respaldo teórico creíble: Debe existir una explicación lógica y teórica fundamentada que explique paso a paso cómo y por qué X produce un cambio en Y.
5. Interpretación de datos con sistema SPSS y ATLAS.ti
   4.1 Procesamiento e interpretación en IBM SPSS
   El programa IBM SPSS organiza la información a través de dos pantallas principales organizadas como pestañas complementarias (Pardo & Ruiz, 2005):
   • Vista de Variables: Funciona como el libro de instrucciones de la base de datos. Cada fila representa una variable (pregunta) y en las columnas se configuran sus propiedades: Nombre (nombre corto sin espacios), Tipo (números, texto o fechas), Etiqueta (texto largo que describe la pregunta para los reportes), Valores (donde se define qué significa cada número; ej. 1 = Varón, 2 = Mujer), Perdidos (donde se indican los números para datos en blanco como 8 o 9) y Medida (si la escala es Nominal, Ordinal o Continua).
   • Vista de Datos: Es la tabla de datos real donde cada columna es una variable ya configurada y cada fila horizontal es una persona evaluada.
   En IBM SPSS, todas las operaciones de análisis se solicitan mediante el menú superior **Analizar** (Pardo & Ruiz, 2005):
   a) Tablas de Frecuencias: Ruta: `Analizar > Estadísticas descriptivas > Frecuencias...` Genera tablas con recuentos, porcentajes totales, válidos y acumulados.
   b) Medidas Descriptivas: Ruta: `Analizar > Estadísticas descriptivas > Descriptivos...` Calcula medias, desviaciones típicas y rangos de variables numéricas continuas.
   c) Tablas Cruzadas de Contingencia: Ruta: `Analizar > Estadísticas descriptivas > Tablas cruzadas...` Cruza dos variables cualitativas y permite solicitar la prueba de independencia Chi-cuadrada.
   4.2 Cómo interpretar la significancia estadística: El p-valor frente al umbral 0.05
   Cuando se realizan pruebas de hipótesis en IBM SPSS, el software entrega un valor clave llamado **p-valor** (etiquetado en las tablas de resultados como _Sig. bilateral_ o _Sig. asintótica_). Este número se compara contra el nivel de riesgo prefijado por el investigador, llamado **umbral alfa (α)** (Pardo & Ruiz, 2005):
   • El Umbral Alfa (α = 0.05): Es el riesgo máximo que el investigador está dispuesto a aceptar de cometer una equivocación (Error Tipo I: asegurar que algo existe cuando en realidad fue producto de la suerte). En ciencias sociales y de la educación, se fija formalmente en α = 0.05, lo que representa un margen de error admisible de solo el 5% y un nivel de seguridad o confianza del 95% (Hernández-Sampieri et al., 2014).
   • El p-valor (Sig.): Es la probabilidad de que los resultados obtenidos hayan ocurrido por pura casualidad o suerte del azar.
   El criterio de decisión para comprobar las hipótesis es simple y contundente (Pardo & Ruiz, 2005):
6. Si el p-valor es MENOR o IGUAL a 0.05 (Sig. ≤ 0.05): El resultado es estadísticamente significativo. Se rechaza la idea de que todo fue casualidad (Hipótesis Nula) y se concluye con respaldo formal que la relación o diferencia observada es real y válida para toda la población.
7. Si el p-valor es MAYOR a 0.05 (Sig. > 0.05): El resultado no es estadísticamente significativo. No hay pruebas suficientes para afirmar que la relación es real; pudo deberse a la suerte del muestreo.
   La Tabla 4 muestra un ejemplo práctico de una salida de SPSS donde se evalúa la correlación entre el estrés docente y el agotamiento emocional.
   Tabla 4. Matriz de correlación bivariada de Pearson generada en IBM SPSS.
   Variable Evaluada
   Estadístico de la Salida
   Nivel de Estrés (estres)
   Agotamiento Emocional (agotamiento)
   Nivel de Estrés (estres)
   Correlación de Pearson (r)
   1
   .684\*\*

Sig. (bilateral)

.000

N (casos)
120
120
Agotamiento Emocional (agotamiento)
Correlación de Pearson (r)
.684\*\*
1

Sig. (bilateral)
.000

N (casos)
120
120

Nota: \*\* La correlación es significativa en el nivel 0.01 (bilateral). Muestra efectiva de n = 120 docentes (Pardo & Ruiz, 2005).
Lectura interpretativa de la Tabla 4: La lectura metódica de esta salida se realiza en tres pasos muy claros:

1. Intensidad y sentido de la relación: El coeficiente es r = 0.684. Es un valor positivo de intensidad considerable, indicando que los docentes con mayor nivel de estrés muestran también niveles notablemente más altos de agotamiento emocional.
2. Evaluación del p-valor: En la tabla figura Sig. = .000 (en normas APA 7 se escribe p < .001). Al ser ampliamente menor que 0.05, se comprueba formalmente que esta correlación no es casualidad y existe verdaderamente en la población.
3. Porcentaje de explicación (r²): Si elevamos 0.684 al cuadrado obtenemos 0.468 (r² = 0.468). Esto significa que el estrés de los docentes explica o comparte el 46.8% de las variaciones observadas en su agotamiento emocional (Pardo & Ruiz, 2005).
   4.3 Análisis e interpretación cualitativa asistida por ATLAS.ti
   A diferencia de SPSS, que trabaja con fórmulas y números para comprobar hipótesis preestablecidas, el software **ATLAS.ti** fue creado para ayudar al investigador a comprender y analizar información cualitativa (palabras, testimonios y relatos de vida) (San Martín, 2014). Su propósito no es calcular porcentajes matemáticos, sino descubrir ideas profundas, entender el punto de vista de las personas y construir explicaciones teóricas (ATLAS.ti Scientific Software Development GmbH, 2023).
   Todo el trabajo en ATLAS.ti se reúne dentro de un proyecto digital llamado **Unidad Hermenéutica**, la cual organiza cuatro elementos clave (San Martín, 2014):
4. Documentos Primarios: Son los archivos originales cargados al programa: transcripciones de entrevistas, observaciones de campo, grabaciones de audio, fotos o videos.
5. Citas (Quotations): Son fragmentos o párrafos específicos de las entrevistas que el investigador resalta porque contienen una idea importante para el estudio; son la evidencia textual directa.
6. Códigos (Codes): Son nombres o etiquetas cortas que el investigador coloca a las citas para identificar el concepto del que están hablando (ejemplo: 'Estrés laboral', 'Falta de tiempo', 'Apoyo familiar').
7. Memos o Notas Analíticas: Cuadernos de notas dentro del programa donde el investigador escribe sus reflexiones teóricas, ideas y conclusiones a medida que va leyendo el material.
   4.4 Detección de patrones textuales: tablas de coocurrencia y redes semánticas
   Para descubrir patrones en los relatos cualitativos, ATLAS.ti ofrece dos herramientas muy potentes (ATLAS.ti Scientific Software Development GmbH, 2023):
   A. Tablas de Coocurrencia de Códigos: Muestran cuántas veces dos códigos distintos coinciden en la misma frase o aparecen juntos en los testimonios. Por ejemplo, permite ver cuántas veces los docentes que hablaron de 'Sobrecarga de trabajo' mencionaron simultáneamente 'Dolores de cabeza'. Esto se visualiza con diagramas de flujo (Diagramas de Sankey), donde el grosor de las líneas muestra qué tan unidos están los temas en el discurso de las personas (San Martín, 2014).
   B. Redes Semánticas (Networks): Son mapas conceptuales visuales donde se conectan los códigos y las citas mediante flechas explicativas. Lo más valioso de ATLAS.ti es que permite especificar con precisión qué tipo de relación une a las ideas a través de Vínculos con Nombre: vínculos de causa (ejemplo: 'el estrés laboral es_causa_de desmotivación'), vínculos de asociación (ejemplo: 'el salario está_asociado_con satisfacción') o vínculos de conflicto (ejemplo: 'la política institucional contradice la práctica pedagógica') (ATLAS.ti Scientific Software Development GmbH, 2023; San Martín, 2014).
   4.5 Regla de oro metodológica: El rol insustituible del investigador
   Tanto IBM SPSS como ATLAS.ti son herramientas informáticas indispensables: SPSS calcula estadísticas a gran velocidad y ATLAS.ti organiza cientos de páginas de entrevistas con gran comodidad (Hernández-Sampieri et al., 2014; San Martín, 2014). Sin embargo, existe una **regla de oro metodológica** que todo investigador debe tener siempre presente:
   ■ LA REGLA DE ORO METODOLÓGICA
   El software computacional calcula números, dibuja gráficos y organiza citas con absoluta rapidez y exactitud, pero no piensa ni comprende la realidad social. La interpretación humana, el sentido de los resultados y la validez final de las conclusiones son responsabilidad exclusiva del investigador.

Un programa informático puede procesar una encuesta mal diseñada sin protestar, y puede calcular correlaciones de datos sin sentido teórico. Por ello, el investigador es quien debe conectar las cifras o las frases con la teoría acumulada, los objetivos planteados y el contexto real en el que viven las personas evaluadas (Pardo & Ruiz, 2005; San Martín, 2014). 5. Guía conceptual y glosario explicativo de términos técnicos
Para facilitar la comprensión integral de todos los conceptos especializados mencionados a lo largo del informe, a continuación se presenta una guía didáctica con las definiciones claras y aplicaciones prácticas de los términos técnicos más relevantes:
• Matriz de datos rectangular: Estructura básica de una base de datos donde cada fila es una persona y cada columna es una pregunta. Se le llama 'rectangular' porque todos los participantes deben tener el mismo número de columnas registradas, sin dejar huecos o celdas en blanco.
• Valores perdidos (Missing Data): Respuestas que no se obtuvieron porque la persona omitió contestar, no sabía la respuesta o la pregunta no le aplicaba. Deben registrarse con números especiales (como 8 u 9) para que el computador no los confunda con puntuaciones reales ni altere los promedios.
• Porcentaje válido frente a Porcentaje total: El porcentaje total se calcula sobre todas las encuestas recibidas, incluso las que tienen preguntas en blanco. El porcentaje válido recalcula la proporción únicamente sobre las personas que respondieron de verdad; por eso es el valor más representativo.
• Intervalos de clase y Marcas de clase: Los intervalos de clase son tramos o rangos agrupados de notas (ejemplo: de 56 a 60 puntos) para resumir variables con muchos valores distintos. La marca de clase es el número medio exacto de ese tramo (en 56-60 es 58.0), utilizado para representar a todo ese grupo en cálculos posteriores.
• Rango Intercuartílico (IQR): Es la distancia entre el Cuartil 1 (Percentil 25) y el Cuartil 3 (Percentil 75). Representa el tamaño de la caja central en un Boxplot y mide la dispersión del 50% de las observaciones centrales.
• Valor atípico (Outlier): Una puntuación tan anormalmente alta o baja que se sale del comportamiento común del grupo. Puede deberse a un error al escribir el dato o a un caso extraordinario que debe analizarse con cuidado para que no desvíe el promedio general.
• Coeficiente Alfa de Cronbach: Indicador que mide qué tan confiable y coherente es una encuesta o cuestionario. Si sus preguntas apuntan al mismo objetivo de forma consistente, el valor superará 0.70 u 0.80, lo que demuestra que el instrumento es métricamente confiable.
• Coeficiente de correlación de Pearson (r): Número entre -1.00 y +1.00 que indica qué tan juntas se mueven dos variables continuas. Un número positivo cercano a +1 indica que cuando una sube, la otra también sube; un valor cercano a 0 indica que no tienen relación lineal.
• Coeficiente de determinación (r²): Se calcula multiplicando la correlación de Pearson por sí misma. Indica qué porcentaje de la variabilidad de una variable se debe o se comparte con la otra (ejemplo: si r = 0.684, r² = 0.468, lo que significa que el 46.8% de una variable se explica por la otra).
• Umbral alfa (α = 0.05) y p-valor (Sig.): El umbral alfa es el límite de riesgo que aceptamos de equivocarnos (máximo 5%). El p-valor es la probabilidad calculada por el programa de que lo que vimos sea pura suerte. Si el p-valor es menor a 0.05, concluimos que el hallazgo es real y no una casualidad.
• Proceso KDD y Minería de Datos: Metodología computacional orientada a explorar grandes bases de datos para descubrir patrones que sean válidos, novedosos, útiles y comprensibles para los humanos.
• Clustering (K-medias): Técnica que reúne a los participantes en grupos homogéneos de forma automática según sus características parecidas, sin necesidad de que el investigador les ponga una etiqueta previa.
• Árboles de decisión y reglas IF-THEN: Modelos de clasificación que explican decisiones mediante reglas condicionales claras (ejemplo: 'SI la nota es mayor a 80 Y la asistencia es de 90%, ENTONCES aprueba la materia').
• Reglas de asociación (Soporte y Confianza): Descubren hábitos o eventos que suelen coexistir al mismo tiempo. El Soporte mide qué tan común es esa combinación en general y la Confianza mide qué tan probable es que ocurra la segunda cosa cuando ya ocurrió la primera.
• Relación espuria: Coincidencia aparente entre dos cosas que parecen estar conectadas, pero que en realidad no tienen ninguna relación de causa, sino que dependen de una tercera variable oculta que no se había medido.
• Unidad Hermenéutica (en ATLAS.ti): Es el archivo de proyecto en ATLAS.ti que reúne todo el material cualitativo de la investigación: los documentos primarios, las frases seleccionadas (citas), las etiquetas (códigos) y las notas de reflexión (memos).
• Tablas de coocurrencia y Redes semánticas: Las tablas de coocurrencia cuentan cuántas veces dos ideas aparecen juntas en los testimonios. Las redes semánticas son esquemas visuales donde esas ideas se conectan con flechas que indican si una idea causa, complementa o contradice a la otra.
• Saturación teórica: Punto en la investigación cualitativa en el cual realizar más entrevistas o revisar más textos ya no aporta ideas nuevas, demostrando que la teoría construida es completa y sólida.
Conclusiones
El recorrido metodológico expuesto en este informe permite formular cinco conclusiones principales sobre la gestión y el análisis científico de la información empírica:

1. Organización y limpieza rigurosa de la base de datos: La tabulación es la base técnica indispensable que garantiza la calidad del análisis. Organizar los datos en una matriz rectangular sin casillas vacías y declarar previamente códigos para las respuestas no contestadas (8 u 9) evita errores graves de software y asegura que los porcentajes válidos describan fielmente a las personas evaluadas (Hernández-Sampieri et al., 2014; Pardo & Ruiz, 2005).
2. Disciplina visual según el tipo de variable: La construcción completa de tablas de frecuencias (con recuentos, porcentajes válidos y porcentajes acumulados) permite una lectura transparente de los resultados. De igual modo, la escala de medición de la variable impone el tipo de gráfico: barras separadas para categorías cualitativas, histogramas unidos para mediciones continuas y diagramas de caja (Boxplot) para detectar de forma matemática los casos atípicos o desproporcionados (Pardo & Ruiz, 2005).
3. Integración entre estadística tradicional y minería de datos: El análisis cuantitativo debe seguir un orden lógico: limpiar los datos, calcular descriptivos, verificar la consistencia del instrumento mediante el Alfa de Cronbach y luego contrastar hipótesis. Esta secuencia se enriquece con la minería de datos (KDD), que extrae patrones útiles mediante técnicas de agrupamiento (K-medias) y reglas intuitivas (Árboles de decisión) (Hernández Orallo et al., 2004).
4. Regla fundamental de causalidad frente a correlación: Encontrar que dos variables se mueven al mismo tiempo no autoriza a decir que una causa la otra. Probar una causa real requiere comprobar la relación estadística, asegurar que la causa ocurrió antes en el tiempo, descartar variables ocultas mediante el diseño metodológico y ofrecer una explicación teórica convincente (Hernández-Sampieri et al., 2014; Hernández Orallo et al., 2004).
5. Sinergia metodológica y protagonismo del investigador: La complementariedad entre IBM SPSS (para probar hipótesis cuantitativas con el p-valor frente al umbral 0.05) y ATLAS.ti (para estructurar significados cualitativos mediante citas, códigos y redes semánticas) ofrece una visión integral y profunda de los fenómenos de estudio. En ambos casos, las computadoras procesan algoritmos con exactitud, pero el sentido conceptual, la mirada crítica y la validez final de las conclusiones dependen de la inteligencia del investigador (ATLAS.ti Scientific Software Development GmbH, 2023; Pardo & Ruiz, 2005; San Martín, 2014).
