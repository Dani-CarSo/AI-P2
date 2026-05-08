#43
#Tratamiento Probabilístico del Lenguaje

# Importamos Counter para contar elementos fácilmente (como un diccionario con suma automática)
# y defaultdict para crear diccionarios con valor por defecto sin lanzar KeyError
from collections import Counter, defaultdict

# re   → módulo de expresiones regulares, para extraer palabras del texto
# math → funciones matemáticas: log, exp (necesarias para probabilidades)
# random → para generar texto aleatorio ponderado por probabilidades
import re, math, random

# CORPUS DE EJEMPLO
# El corpus es el texto de entrenamiento sobre el que calculamos todas las probabilidades.
# Las tres comillas """ permiten un string multilínea en Python.
corpus = """
el gato come pescado el perro come carne
el gato duerme el perro ladra el gato juega
el pájaro vuela alto el gato caza al pájaro
el perro corre rápido el gato salta alto
"""

#  Función tokenizar

def tokenizar(texto):
    # re.findall busca todas las coincidencias del patrón dentro del texto.
    # \w+ significa "uno o más caracteres alfanuméricos o guión bajo".
    # texto.lower() convierte todo a minúsculas para no distinguir "El" de "el".
    return re.findall(r'\w+', texto.lower())

# Aplicamos tokenizar al corpus → obtenemos una lista plana de palabras
tokens = tokenizar(corpus)

# set() elimina duplicados → vocabulario = conjunto de palabras únicas del corpus
vocabulario = set(tokens)

# V es el tamaño del vocabulario; lo usaremos en suavizado de Laplace
V = len(vocabulario)

# Imprimimos un encabezado decorativo y la estadística básica del corpus
print("=" * 60)
print("  TRATAMIENTO PROBABILÍSTICO DEL LENGUAJE")
print("=" * 60)
# f-string: embebe variables directamente dentro del string con {}
print(f"\nCorpus: {len(tokens)} tokens | Vocabulario: {V} palabras únicas\n")


# Un UNIGRAMA modela la probabilidad de cada palabra independientemente.
# Fórmula: P(w) = conteo(w) / total_de_tokens

print("─" * 60)
print("1. PROBABILIDADES UNIGRAMA  P(w)")
print("─" * 60)

# Counter recibe una lista y devuelve un diccionario {elemento: frecuencia}
conteo = Counter(tokens)

# total_tok es el número total de tokens (denominador de la probabilidad)
total_tok = len(tokens)

# Creamos un diccionario de probabilidades dividiendo cada conteo entre el total.
# Dict comprehension: {clave: valor for clave, valor in iterable}
prob_uni = {w: c / total_tok for w, c in conteo.items()}

# Imprimimos encabezado de tabla con formato de ancho fijo:
# :<12 = alineado a la izquierda en 12 caracteres
# :>6  = alineado a la derecha en 6 caracteres
print(f"{'Palabra':<12} {'Conteo':>6} {'P(w)':>8}")
print("-" * 28)

# sorted() ordena el diccionario; key=lambda x: -x[1] ordena por probabilidad descendente.
# [:10] toma solo las 10 palabras más frecuentes.
for w, p in sorted(prob_uni.items(), key=lambda x: -x[1])[:10]:
    # {p:.4f} imprime p con 4 decimales
    print(f"  {w:<10} {conteo[w]:>6}   {p:.4f}")



# MODELO DE BIGRAMAS 
# Un BIGRAMA captura la probabilidad de una palabra dado que conocemos la anterior.
# Fórmula: P(w2 | w1) = conteo(w1, w2) / conteo(w1)
# Esto modela dependencias locales entre palabras consecutivas.

print("\n" + "─" * 60)
print("2. MODELO DE BIGRAMAS  P(w2 | w1)")
print("─" * 60)

# zip(tokens, tokens[1:]) empareja cada token con el siguiente:
# ej. ["el","gato","come"] → [("el","gato"), ("gato","come")]
# Counter cuenta cuántas veces aparece cada par (bigrama)
bigramas = Counter(zip(tokens, tokens[1:]))

# unigramas cuenta la frecuencia de cada palabra sola (para el denominador)
unigramas = Counter(tokens)

def prob_bigrama_raw(w1, w2):
    # Dividimos la frecuencia del par (w1,w2) entre la frecuencia de w1.
    # La condición "if unigramas[w1]" evita división por cero si w1 no existe.
    return bigramas[(w1, w2)] / unigramas[w1] if unigramas[w1] else 0

print(f"{'Bigrama':<22} {'Conteo':>6} {'P(w2|w1)':>10}")
print("-" * 42)

# most_common(8) devuelve los 8 bigramas más frecuentes como lista de ((w1,w2), conteo)
for (w1, w2), c in bigramas.most_common(8):
    p = prob_bigrama_raw(w1, w2)   # calculamos la probabilidad del bigrama
    print(f"  P({w2:<8} | {w1:<8}) {c:>4}     {p:.4f}")


#  SUAVIZADO DE LAPLACE
# PROBLEMA: si un bigrama nunca aparece en el corpus, P(w2|w1) = 0.
# Esto es peligroso: hace que la probabilidad de toda una frase sea 0
# aunque solo un par sea desconocido.
#
# SOLUCIÓN — Suavizado de Laplace (additive smoothing):
# Sumamos 1 a cada conteo de bigrama y V al denominador.
# Fórmula: P(w2|w1) = (C(w1,w2) + 1) / (C(w1) + V)
# Así, ningún bigrama tiene probabilidad 0.

print("\n" + "─" * 60)
print("3. SUAVIZADO DE LAPLACE (Additive Smoothing)")
print("─" * 60)
print("   Evita probabilidades 0 para palabras no vistas\n")
print("   Formula: P(w2|w1) = (C(w1,w2) + 1) / (C(w1) + V)\n")

def prob_laplace(w1, w2):
    # bigramas.get((w1,w2), 0) devuelve 0 si el bigrama no existe (en vez de KeyError)
    num = bigramas.get((w1, w2), 0) + 1    # numerador: conteo del par + 1

    # unigramas.get(w1, 0) devuelve 0 si w1 nunca apareció en el corpus
    den = unigramas.get(w1, 0) + V         # denominador: conteo de w1 + tamaño vocabulario

    return num / den   # probabilidad suavizada

# Lista de pares de prueba: algunos conocidos, otros inexistentes en el corpus
pares_prueba = [
    ("el",   "gato"),    # bigrama muy frecuente en el corpus
    ("gato", "come"),    # bigrama que existe en el corpus
    ("gato", "ladra"),   # bigrama que NO existe → sin suavizado daría 0
    ("perro","vuela"),   # bigrama que NO existe → sin suavizado daría 0
]

print(f"{'Par':<28} {'Sin suavizado':>14} {'Con Laplace':>12}")
print("-" * 57)
for w1, w2 in pares_prueba:
    p_raw    = prob_bigrama_raw(w1, w2)   # probabilidad original (puede ser 0)
    p_smooth = prob_laplace(w1, w2)       # probabilidad con suavizado (siempre > 0)
    print(f"  P({w2:<8} | {w1:<8})      {p_raw:>8.4f}     {p_smooth:>8.4f}")


#GENERACIÓN DE TEXTO CON BIGRAMAS
# Usamos el modelo de bigramas para generar texto nuevo de forma probabilística:
# dado el token actual, elegimos el siguiente pesando por P(siguiente | actual).

print("\n" + "─" * 60)
print("4. GENERACIÓN DE TEXTO CON BIGRAMAS")
print("─" * 60)

def generar_texto(palabra_inicio, n=7, seed=42):
    # seed fija el generador aleatorio para reproducibilidad (siempre el mismo resultado)
    random.seed(seed)

    # resultado es la lista de tokens generados; empezamos con la palabra inicial
    resultado = [palabra_inicio]

    # Generamos n-1 tokens adicionales (ya tenemos 1)
    for _ in range(n - 1):
        w1 = resultado[-1]   # la última palabra generada es el contexto actual

        # Buscamos todos los bigramas que empiezan con w1 y guardamos sus frecuencias
        # Dict comprehension filtrando solo los pares donde el primer elemento es w1
        candidatos = {w2: bigramas[(w1, w2)] for (a, w2) in bigramas if a == w1}

        # Si no hay continuaciones posibles (w1 nunca tuvo sucesor), terminamos
        if not candidatos:
            break

        # random.choices elige aleatoriamente de la lista, ponderando por frecuencias.
        # Palabras más frecuentes tienen más probabilidad de ser elegidas.
        # [0] porque random.choices devuelve una lista, tomamos el primer (y único) elemento
        siguiente = random.choices(
            list(candidatos.keys()),      # opciones posibles
            weights=list(candidatos.values())  # sus pesos (frecuencias)
        )[0]

        # Añadimos la palabra elegida a la secuencia generada
        resultado.append(siguiente)

    # Unimos la lista de tokens en un string separado por espacios
    return " ".join(resultado)

# Probamos la generación con tres palabras de inicio distintas
inicios = ["el", "gato", "perro"]
for ini in inicios:
    texto_gen = generar_texto(ini, n=7)   # generamos 7 tokens
    print(f"  Inicio '{ini}' → {texto_gen}")



# CLASIFICADOR NAIVE BAYES
# Naive Bayes clasifica un texto calculando la probabilidad de que pertenezca
# a cada categoría y eligiendo la más alta.
#
# Fórmula (en log para evitar underflow numérico):
# log P(clase | texto) = log P(clase) + Σ log P(palabra | clase)
#
# Se llama "naive" (ingenuo) porque asume que cada palabra es independiente de las demás.

print("\n" + "─" * 60)
print("5. CLASIFICADOR NAIVE BAYES")
print("─" * 60)

# Dataset de entrenamiento: lista de tuplas (texto, categoría)
datos_train = [
    ("el banco tiene dinero",         "finanzas"),
    ("invertir en acciones bolsa",    "finanzas"),
    ("pagar impuestos banco",         "finanzas"),
    ("préstamo hipoteca interés",     "finanzas"),
    ("el gato come pescado",          "animales"),
    ("el perro ladra al gato",        "animales"),
    ("el pájaro vuela alto",          "animales"),
    ("el gato caza ratones",          "animales"),
]

# Fase de entrenamiento
# clase_docs almacena, por clase, la lista de documentos (listas de palabras)
# defaultdict(list) crea automáticamente una lista vacía si la clave no existe
clase_docs = defaultdict(list)

# clase_words almacena, por clase, el conteo de cada palabra
# defaultdict(Counter) crea automáticamente un Counter vacío si la clave no existe
clase_words = defaultdict(Counter)

for texto, clase in datos_train:
    palabras = tokenizar(texto)              # tokenizamos el texto de entrenamiento
    clase_docs[clase].append(palabras)       # guardamos la lista de palabras bajo su clase
    clase_words[clase].update(palabras)      # sumamos las frecuencias al Counter de esa clase

# vocab_nb = conjunto de TODAS las palabras que aparecen en cualquier clase
# Necesitamos V_nb para el suavizado de Laplace dentro de Naive Bayes
vocab_nb = set(w for ws in clase_words.values() for w in ws)
V_nb     = len(vocab_nb)   # tamaño del vocabulario de Naive Bayes

# N_docs = número total de documentos de entrenamiento (para calcular el prior)
N_docs = len(datos_train)

# Función de clasificación 
def clasificar(texto):
    palabras = tokenizar(texto)   # tokenizamos el texto a clasificar
    scores   = {}                 # aquí guardaremos el score log-probabilístico de cada clase

    for clase, docs in clase_docs.items():
        # PRIOR: log P(clase) = log(documentos de esta clase / total documentos)
        # Representa qué tan común es la clase antes de ver las palabras
        log_p = math.log(len(docs) / N_docs)

        # total_w = total de palabras en todos los documentos de esta clase
        # Es el denominador para calcular P(palabra | clase)
        total_w = sum(clase_words[clase].values())

        for w in palabras:
            # LIKELIHOOD con suavizado de Laplace:
            # P(w | clase) = (conteo(w en clase) + 1) / (total palabras en clase + V)
            # Usamos log para convertir multiplicaciones en sumas (más estable numéricamente)
            log_p += math.log((clase_words[clase][w] + 1) / (total_w + V_nb))

        # Guardamos el score total (prior + sum de likelihoods) para esta clase
        scores[clase] = log_p

    # La predicción es la clase con el mayor score log-probabilístico
    pred = max(scores, key=scores.get)
    return pred, scores   # devolvemos predicción y scores completos

#Pruebas

pruebas_nb = [
    "el gato come mucho",       # debería → animales
    "comprar acciones hoy",     # debería → finanzas
    "el perro tiene hambre",    # debería → animales
    "crédito bancario anual",   # debería → finanzas
]

print(f"\n  {'Texto':<35} {'Predicción':<12} {'Scores'}")
print("  " + "-" * 68)
for t in pruebas_nb:
    pred, sc = clasificar(t)
    # Construimos el string de scores: "finanzas=-14.55  animales=-11.86"
    sc_str = "  ".join(f"{cl}={s:.2f}" for cl, s in sc.items())
    print(f"  {t:<35} {pred:<12} {sc_str}")
#  PERPLEJIDAD  ─  evaluación del modelo
# La PERPLEJIDAD mide qué tan sorprendido está el modelo ante un texto nuevo.
# Un modelo bueno asigna alta probabilidad a frases naturales → baja perplejidad.
# Un modelo malo se "sorprende" mucho → alta perplejidad.
# Fórmula: PP = exp( -1/N * Σ log P(wi | wi-1) )

print("\n" + "─" * 60)
print("6. PERPLEJIDAD (evaluación del modelo de lenguaje)")
print("─" * 60)
print("   Fórmula: PP = exp(-1/N * Σ log P(wi | wi-1))")
print("   Cuanto MENOR la perplejidad, MEJOR el modelo.\n")

def perplejidad(texto_prueba):
    toks = tokenizar(texto_prueba)   # tokenizamos el texto de prueba

    # Necesitamos al menos 2 tokens para formar un bigrama
    if len(toks) < 2:
        return float('inf')   # inf = infinito, señal de que no se puede calcular

    N = len(toks)    # número total de tokens en el texto de prueba
    log_prob = 0     # acumulador de log-probabilidades

    # Recorremos todos los bigramas del texto de prueba
    for i in range(1, N):
        w1, w2 = toks[i-1], toks[i]       # par de palabras consecutivas
        p = prob_laplace(w1, w2)           # usamos Laplace para evitar log(0)
        log_prob += math.log(p)            # sumamos el logaritmo de la probabilidad

    # Aplicamos la fórmula: negamos la suma, dividimos entre N, exponenciamos
    return math.exp(-log_prob / N)

# Evaluamos frases con distintos grados de "rareza" respecto al corpus
frases_eval = [
    ("el gato come pescado",       "en corpus, conocida"),
    ("el perro ladra fuerte",      "parcialmente conocida"),
    ("el robot vuela rápido",      "palabras extrañas"),
    ("pizza integral salmón",      "totalmente fuera del corpus"),
]

print(f"  {'Frase':<35} {'Perplejidad':>12}  Contexto")
print("  " + "-" * 68)
for frase, nota in frases_eval:
    pp = perplejidad(frase)   # calculamos la perplejidad de cada frase
    # {pp:>12.2f} → alineado a la derecha, 2 decimales
    print(f"  {frase:<35} {pp:>12.2f}  ({nota})")

# DETECCIÓN DE IDIOMA (Naive Bayes a nivel de caracteres)
# En vez de palabras usamos n-gramas de CARACTERES (substrings de longitud n).
# Cada idioma tiene patrones de combinaciones de letras muy distintos.
# Ej.: "qu" es muy frecuente en español e inglés pero poco en francés; "ou" es
# muy frecuente en francés. Estos perfiles nos permiten distinguir idiomas.

print("\n" + "─" * 60)
print("7. DETECCIÓN DE IDIOMA  (n-gramas de caracteres)")
print("─" * 60)

# Corpus de entrenamiento por idioma: lista de frases de ejemplo en cada idioma
corpus_idiomas = {
    "español": [
        "el gato está en la casa con la familia",
        "buenos días cómo estás hoy amigo",
        "me gustan mucho las películas españolas",
    ],
    "inglés": [
        "the cat is in the house with the family",
        "good morning how are you today friend",
        "i really enjoy watching english movies",
    ],
    "francés": [
        "le chat est dans la maison avec la famille",
        "bonjour comment allez vous aujourd hui",
        "j aime beaucoup les films français",
    ],
}

def ngramas_char(texto, n=2):
    # Reemplazamos espacios con "_" para que los límites de palabra sean parte del patrón
    texto = texto.lower().replace(" ", "_")
    # Generamos todos los substrings de longitud n deslizando una ventana de n caracteres
    # range(len(texto)-n+1) asegura que el último ngrama no se salga del string
    return [texto[i:i+n] for i in range(len(texto)-n+1)]


perfiles = {}    # diccionario {idioma: {ngrama: probabilidad}}

for idioma, textos in corpus_idiomas.items():
    todo   = " ".join(textos)        # concatenamos todas las frases del idioma
    ngrams = ngramas_char(todo, n=2) # extraemos todos los bigramas de caracteres
    total  = len(ngrams)             # total de bigramas (denominador)

    # Creamos el perfil: frecuencia relativa de cada bigrama de caracteres
    # Counter(ngrams) cuenta cuántas veces aparece cada bigrama de caracteres
    perfiles[idioma] = {ng: c/total for ng, c in Counter(ngrams).items()}

def detectar_idioma(texto):
    ngrams_test = ngramas_char(texto, n=2)   # bigramas de caracteres del texto a clasificar
    scores = {}

    for idioma, perfil in perfiles.items():
        # Para cada idioma, sumamos log-probabilidades de cada bigrama de caracteres.
        # perfil.get(ng, 1e-6) devuelve una probabilidad muy pequeña (1e-6 = 0.000001)
        # si el ngrama no está en el perfil, evitando log(0).
        score = sum(math.log(perfil.get(ng, 1e-6)) for ng in ngrams_test)
        scores[idioma] = score

    # El idioma ganador es el que maximiza la suma de log-probabilidades
    return max(scores, key=scores.get), scores

pruebas_idioma = [
    "hola cómo estás hoy",          # → español
    "hello how are you today",      # → inglés
    "bonjour comment allez vous",   # → francés
]

print(f"\n  {'Texto':<30} {'Predicción':>10}")
print("  " + "-" * 42)
for t in pruebas_idioma:
    pred, _ = detectar_idioma(t)   #  descarta los scores, solo usamos la predicción
    print(f"  {t:<30} → {pred}")

print("\n" + "=" * 60) 
print("  RESUMEN DE TÉCNICAS")
print("=" * 60)

# Lista de tuplas (nombre de la técnica, descripción breve)
tecnicas = [
    ("Unigrama P(w)",          "Frecuencia relativa de cada palabra"),
    ("Bigrama P(w2|w1)",       "Probabilidad condicional entre pares"),
    ("Suavizado Laplace",      "Evita probabilidades cero"),
    ("Generación de texto",    "Muestreo desde distribución bigrama"),
    ("Naive Bayes",            "Clasificación por categoría semántica"),
    ("Perplejidad",            "Métrica de calidad del modelo"),
    ("Detección de idioma",    "N-gramas de caracteres + Bayes"),
]

# Imprimimos cada técnica con formato de ancho fijo
for nombre, desc in tecnicas:
    # {nombre:<25} alinea el nombre a la izquierda en 25 caracteres
    print(f"  ✓  {nombre:<25} {desc}")

print("\n  Todo implementado con librería estándar Python \n")