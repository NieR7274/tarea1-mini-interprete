# Análisis — Tarea 1

**Integrantes:**
1. Angel Aaron Lopez Cruz
2. Gabriel Lugo Rosete

**Fork:**
**Rama:**

---

## 1. Arquitectura

### 1.1 ¿Cuál es la responsabilidad de cada componente?


| Componente | Representacion |
| :--- | :--- |
| **`lexer`** | **Recibe:** Cadena de texto<br>**Entrega:** Lista de tokens<br>**Responsabilidad:** Partir el texto plano en unidades lexicas individuales. |
| **`parser`** | **Recibe:** Lista de tokens<br>**Entrega:** Arbol de sintaxis abstracta (AST)<br>**Responsabilidad:** Construir la estructura jerarquica respetando la precedencia de operadores. |
| **`ast`** | **Recibe:** Clases/datos<br>**Entrega:** Estructuras de nodos<br>**Responsabilidad:** Definir los objetos que representan la expresion. |
| **`evaluator`** | **Recibe:** Nodo raiz del AST<br>**Entrega:** Resultado numerico<br>**Responsabilidad:** Recorrer el arbol de abajo hacia arriba para calcular el valor final. |

### 1.2 ¿Qué recorrido sigue una expresión desde que se recibe como texto hasta que produce un resultado?

// cual dejamos, no probocan errores los acento?

### 1.2 Que recorrido sigue una expresion desde que se recibe como texto hasta que produce un resultado?

| Etapa | Representacion |
| :--- | :--- |
| **Texto** | `"(3 + 4) * 2"` |
| **Tokens** | `[PAR_IZQ, NUMERO(3), MAS, NUMERO(4), PAR_DER, POR, NUMERO(2)]` |
| **AST** | `OperacionBinaria('*', OperacionBinaria('+', Numero(3), Numero(4)), Numero(2))` |
| **Resultado** | `14` |

## 2. Las pruebas que ya estaban

### 2.1 ¿Qué pruebas venían incluidas?

| Prueba | Componente | Comportamiento que verifica | ¿Cuántos operadores usa? | ¿Normal, frontera o inválida? |
| :--- | :--- | :--- | :--- | :--- |
| `test_suma` | Evaluador | Suma dos numeros enteros correctamente | 1 | Normal |
| `test_resta` | Evaluador | Resta dos numeros enteros correctamente | 1 | Normal |
| `test_multiplicacion` | Evaluador | Multiplica dos numeros enteros correctamente | 1 | Normal |
| `test_division` | Evaluador | Divide dos numeros enteros correctamente | 1 | Normal |
| `test_precedencia_sin_parentesis` | Evaluador | Respeta la precedencia de operadores | 2 | Normal |
| `test_precedencia_con_parentesis` | Evaluador | Da prioridad a los parentesis sobre la precedencia normal | 2 | Normal |
| `test_tokeniza_un_numero_solo` | Lexer | Tokeniza correctamente un unico numero suelto | 0 | Frontera |
| `test_tokeniza_una_suma` | Lexer | Tokeniza una expresion de suma sin espacios | 1 | Normal |
| `test_los_espacios_no_producen_tokens` | Lexer | Ignora los espacios en blanco sobrantes al tokenizar | 1 | Frontera |
| `test_tokeniza_parentesis` | Lexer | Reconoce e identifica los parentesis y numeros correctamente | 0 | Frontera |
| `test_construye_el_arbol_de_una_suma` | Parser | Construye el AST correcto para una suma | 1 | Normal |
| `test_la_multiplicacion_se_agrupa_antes_que_la_suma` | Parser | Agrupa la multiplicacion antes en el AST por precedencia | 2 | Normal |
| `test_los_parentesis_cambian_la_agrupacion` | Parser | Modifica el orden de agrupacion del AST usando parentesis | 2 | Normal |


Se puede observar que no se encuentrar entrada invalidas en las pruebas.

### 2.2 ¿Qué comportamientos **no** estaban probados?

- **Errores de sintaxis:** No hay pruebas para cuando al usuario se le olvida cerrar un parentesis (como `(3 + 4`) o escribe cosas que no van.
- **Dividir entre cero:** Aunque el codigo ya tiene preparado un aviso para cuando intentas dividir un numero entre cero, no se esta probando de forma automatica.
- **Letras o simbolos raros:** Falta probar que pasa si le metes caracteres extranos que el interprete no conoce 

---

## 3. Las pruebas que agregaron

### 3.1 ¿Cuáles son casos normales, cuáles frontera y cuáles inválidos?

| Prueba (archivo::nombre) | Entrada | Esperado | Categoria | Por que esa categoria? |
| :--- | :--- | :--- | :--- | :--- |
| `tests/test_evaluator.py::test_Suma_Resta` | `"3 + 4 - 5"` | `2` | Normal | Evalua una cadena combinada de operadores de suma y resta de igual precedencia. |
| `tests/test_evaluator.py::test_Multiplicacion_Divicion` | `"5 * 6 / 3"` | `10` | Normal | Evalua operaciones combinadas de multiplicacion y division de igual precedencia. |
| `tests/test_evaluator.py::test_Multiples_Parentesis` | `"((5))"` | `5` | Frontera | Pone a prueba el limite estructural de anidamiento de parentesis. |
| `tests/test_evaluator.py::test_Resta_Positivo_Negativo` | `"1 - (0 - 1)"` | `2` | Frontera | Prueba restar un numero negativo usando `(0 - x)`. |
| `tests/test_evaluator.py::test_Multiplicacion_Negativos` | `"(0 - 1) * (0 - 1 )"` | `1` | Frontera | Prueba multiplicar dos negativos `(0 - x)` con espacios extra. |
| `tests/test_evaluator.py::test_operador_incompleto` | `"3 +"` | `ErrorDeSintaxis` | Invalida | Falla por falta de un operando derecho, detectando un error de sintaxis. |
| `tests/test_evaluator.py::test_dato_no_numerico` | `"a + b"` | `ErrorDeSintaxis` | Invalida | Rechaza identificadores o caracteres no soportados por el lexer o parser. |
## 4. Los defectos

### 4.1 ¿Qué defecto reveló primero una prueba nueva?


La prueba de un operador incompleto (como `interpretar("3 +")`) revelo que el parser lanzaba un `IndexError`  en lugar de un `ErrorDeSintaxis` controlado cuando intentaba leer el operando derecho y se quedaba sin tokens.

### 4.2 ¿Por qué el comportamiento observado era incorrecto?

El comportamiento anterior provocaba un `IndexError` de Python cuando faltaba el operando derecho. Esto iba en contra de la regla de la semantica declarada en el README que exige: "Entrada invalida debe rechazarse con ErrorDeSintaxis, nunca con un error de Python."


### 4.3 ¿Qué cambio realizaron?

| Defecto | Entrada que lo revela | Daba | Deberia dar | Commit rojo | Commit verde |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Falta de validacion para operador incompleto al final de la expresion | `"3 +"` | `IndexError` (fallo interno de Python) | `ErrorDeSintaxis` controlado | `Agrega prueba de operador incompleto que falla` | `Arregla parser para lanzar ErrorDeSintaxis en operadores incompletos` |

### 4.4 ¿Cómo saben que la corrección es general y no sólo hace pasar ese ejemplo?  

La correccion es general porque la validacion se aplico directamente en los metodos del parser (`_expresion` y `_termino`) que procesan **cualquier** operador definido. Esto significa que no solo funciona para `"3 +"`, sino para cualquier combinacion donde un operador se quede sin su operando derecho, asegurando que siempre se lance un `ErrorDeSintaxis` controlado .

### Analisis extra

Como analisis extra, se encontraron otros tres errores adicionales en el lexer al procesar ciertas entradas:

1. **Numero decimal ignora el resto:** Si se ingresa un numero decimal (como `1.1`), el lexer descarta el punto decimal y los datos siguientes, devolviendo unicamente la parte entera del primer numero (`1`).
2. **Identificador despues de numero no detectado:** Al ingresar una letra pegada o despues de un numero (como `3a + 5`), el lexer no genera error por la letra y termina evaluando solo el numero entero (`8`).
3. **Simbolo no numerico lanza error no controlado:** Al escribir un simbolo o caracter invalido de forma aislada (como `b`), la ejecucion falla con un `IndexError` no controlado en lugar de capturarlo con `ErrorDeSintaxis`.

## 5. Diseño

### 5.1 ¿Qué duplicación o señal de mal diseño encontraron?

1. Hay duplicación de lógica en los métodos expresion() y termino() en el analizador. Ambos tienen una estructura similar, obtienen un operando izquierdo, comprueban si el token actual es un operador válido, consumen el operador, verifican si hay una operación siguiente y crean un nodo OperacionBinaria.

Es un problema, ya que si se necesita modificar la forma en que se procesan los operadores, o se manejan los errores, se necesitan modificar ambos métodos.

2. La clase Nodo no tiene una interfaz común para sus subclases y las operaciones que deben poder realizar los nodos del AST. Solo es una clase base de Numero y OperacionBinario, no define métodos para evaluarlos o recorrerlos.

Es un problema, ya que si se quisiera añadir algun nuevo tipo de nodo, se necesitarían modificar las funciones que recorren o procesan el árbol para reconocer el nuevo tipo de nodo. Lo cual aumenta el acoplamiento y hace más dificíl de extender sin tener que hacer muchas modificaciones.

### 5.2 ¿Qué refactorización realizaron, y por qué conserva el comportamiento?

Se creo un nuevo método auxiliar, _operación con la lógica común de _expresion() y _termino(), recibiendo como parámetros la función que analiza los operandos y los operadores que se permiten, así evitando la duplicación de lógica.

Conserva el comportamiento, ya que, se mantiene la estructura al cada método seguir analizando el mismo nivel de precedencia, _expresion() usa _termino() para analizar sus operandos y reconoce sumas y restas, y _termino() usa _factor() y reconoce multiplicaciones y divisiones. Así ambos todavía mantienen sus responsabilidades y funciones, pero se evita el duplicar la lógica. También el método auxiliar realiza las mismas operaciones que los métodos originales y además las pruebas siguen pasando.

### 5.3 ¿Sería pertinente usar Factory Method, Adapter o ninguno?

Consideramos que ninguno de los 2 es pertinente de usar actualmente.

Para Factory Method podría usarse en la creación de los nodos del árbol, pero actualmente solo se construyen los tipos de nodo Numero y OperacionBinario y son sencillos. Añadiría complejidad pero no aportaría mucho al programa actual.
Podría ser útil si hubieran distintas formas de crear nodos en el programa o si fuera más compleja su creación.

Para Adapter se podría usar para adaptar la interfaz de un componente a lo esperado, lo que espera el intérprete, pero actualmente se generan objetos Token con lo que el parser necesita, por lo que no hay alguna incompatibilidad o algo que haga necesario usar Adapter.
Podría ser útil si se usará algo externo que creara tokens con alguna estructura distinta y se tuvieran que convertir al formato esperado por el parser.

Es decir, no consideramos que ninguno de estos patrones de diseño sean pertinentes de usar actualmente, en esta implementación, ya que no resuelven algún problema o necesidad presente, y al añadirlos se aumentaría la complejidad, añadiendo clases y más dependencias. Si después se quisiera expandir o sucediera algún cambio en el sistema como los mencionados anteriormente podrían empezar a convenir y ser útiles de implementar.

### 5.4 ¿Qué parte del sistema sería más difícil de modificar si se agregara un operador nuevo?

Para poder agregar un nuevo operador como '%' se tendrían que al menos modificar y revisar lexer, parser y evaluator.
* Para lexer se tendría que agregar % a los símbolos que reconoce el analizador léxico.
* Para parser se tendíra que agregar % en el nivel de precedencia deseado y si tuviera la misma precedencia que algunos otros símbolos, como * y / se tendría que agregar a ese conjunto de operadores, como OPERADORES_PRODUCTO
* Para evaluator se tendría que agregar la operación para calcular lo que hace % es decir calcular el residuo de la división, y se tendrían que definir también nuevos manejos, como al hacerlo entre cero.

Tomando en cuenta esto, nosotros consideramos que la parte del sistema más difícil de modificar sería parser, ya que al agregar un nuevo operador se tendría que decidir su nivel de precedencia, como asociarse con los otros operadores. Mientras que lexer solo necesita reconocer el nuevo símbolo y evaluator el cálculo y el manejo de errores, aunque dependiendo de la complejidad del cálculo y los necesarios manejos de errores puede ser también una parte díficil de modificar.

---

## Antes de la declaración: inténtenlo primero ustedes

Usar IA o no es decisión de cada quien, y el curso la permite. Pero **les
pedimos, por favor, que primero hagan el análisis por su cuenta.**

No es una prueba de honestidad. Es que el orden cambia lo que aprenden:

1. **Primero ustedes.** Lean el código, corran las pruebas, escriban sus
   respuestas. Aunque queden incompletas, aunque no encuentren todo.

2. **Después, si quieren, la IA** — pero como contraste, no como sustituto.
   Y entonces contesten dos preguntas, en `DECLARACION_IA.md`:

   - **¿Qué encontró que ustedes no habían notado?**
     Eso es aprendizaje, y se declara sin ninguna pena.

   - **¿Qué *no* encontró, que en este curso sí consideramos un problema?**
     Ésta es la interesante. Una herramienta suele decir que el código
     "funciona bien" y no señalar, por ejemplo, la **duplicación** — porque
     duplicar no rompe nada, el programa corre igual. Pero ustedes ya saben
     por qué eso sí es un mal diseño, y saben nombrarlo. La herramienta no
     tomó esa clase.

---

## Declaración de uso de Inteligencia Artificial

En `DECLARACION_IA.md`