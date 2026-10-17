# Declaración de uso de Inteligencia Artificial

**Actividad:**
**Integrantes:**
**Fecha:**

> Esta declaración es obligatoria en toda tarea, práctica y en el proyecto final.
> **No da ni quita puntos**: es un reporte adicional que se revisa aparte y se
> devuelve con comentarios. **No se evalúa cuánta IA usaron**, sino si pueden
> dar cuenta de lo que entregaron.

---

## 0. ¿Se usó IA en esta actividad?


 **Sí.** 

---

## 1. Herramienta(s) utilizada(s)

| Herramienta | Versión o modelo, si lo saben |
|---|---|
| | |

Un integrante "uso" el autocompletado de Copilot (Simplete esta pero no se le dio utilidad.)

> Cuenta también el autocompletado del editor (Copilot y similares). Si sólo
> fue eso, basta con decirlo en un renglón y seguir al punto 4.

---

## 2. Objetivo del uso

| Para qué la usamos | En qué parte del entregable |
|---|---|
| | |

> Sean específicos. *"Para la tarea"* no dice nada.
> *"Para generar las pruebas de `minimo_de_llaves`"* sí.

---

## 3. Prompts principales

Textuales, tal como los escribieron. No los limpien ni los reescriban.

```
(prompt 1)
```

```
(prompt 2)
```

---

## 4. Cómo se incorporó o se descartó lo obtenido

**Éste es el punto que más pesa.**

| Qué produjo la herramienta | ¿Aceptado, modificado o descartado? | Por qué | Dónde quedó (archivo / commit) |
|---|---|---|---|
| Propuso nombres para funciones y facilito la gramatica de python | No se aceptaron los nombres, se uso la gramatica que proporcionaba | Los nombres no se adaptaban al contexto. La gramatica era correcta y era necesario usarla. | En los primeros commits ayudo a adaptarse a python en test_evaluator |

> **"Lo descartamos" es una respuesta excelente**, si dicen por qué.
> Una declaración donde todo se aceptó sin cambios es una declaración que
> no muestra criterio.

### 4.1 Si la usaron para el análisis: el contraste

Se les pidió intentarlo primero por su cuenta. Si lo hicieron así:

|  |  |
|---|---|
| ¿Qué encontró la herramienta que ustedes **no** habían notado? | Se uso en el analisis extra para ver el flujo del programa y encontrar la causa del primer fallo. Ayudo a ahorrar tiempo para ver el orden exacto de por que fallaba, algo que no se noto en una revision rapida. |
| ¿Qué **no** encontró, que en este curso sí consideramos un problema? | Solo detecto el fallo para un ejemplo en especifico (`"1.1 + 1"`), dando una solucion solo para ese caso sin impartarle  que el mismo error pasaba en expresiones mas largas (como `"2 + 3 + 5.1 * 20"`) u otros casos . No vio el problema general que abarcaba mas codigo lo puedo comparar a lo dicho en clase (que una pruba pase no significa que el el programa sea correcto). |
> La segunda es la que más nos interesa. Una herramienta suele no señalar la
> duplicación de código, porque el programa funciona igual. Ustedes ya saben
> por qué eso sí importa.
>
> Si no usaron IA para el análisis, escriban *"no aplica"*.

### 4.2 ¿Cómo verificaron que lo que incorporaron era correcto?

El resultado dio una serie de pasos que ejecuta el programa , se realizaron los mismos pasos a mano con otros ejemplos y se detecto el mismo problema.

> Una prueba que escribieron, una ejecución, un contraste contra las notas de
> clase o contra el enunciado. *"Lo revisamos"* no es una verificación.

---

## 5. Reflexión

### 5.1 ¿Qué limitación concreta observaron **en esta actividad**?


    Si pasas un ejemplo particular para preguntar ¿Porque el programa tiene este comportamiento (Ejmplo)?, se enfoca demasiado en ese caso en particular, luego sin pedirselo te da soluciones, recomendaciones y cambios, que no son del todo correctos, no cosidera nada mas alla de responderte eso espesifico en el momento. Al encontrarse mas casos desde antes, se entendio que la respuesta estaba incompleta.

    La IA puede hacerte confiar de mas en el resultado que se tiene al final.

> Concreta. No *"a veces se equivoca"*, sino *"propuso pruebas sólo para
> m = 4 y nunca para órdenes impares, porque no conocía la definición del
> laboratorio"*.

### 5.2 ¿Qué harían distinto la próxima vez?

Ser mas especifico en lo que se pide, dar mas contexto, pero lo realmente importante es entender mejor el tema y asegurarse siempre de que la respuesta es correcta, pensando en varios casos, y de ser posible demostrarla despues de entender bien su respuesta.
---

## Firma

> Declaramos que entendemos y podemos explicar todo lo que entregamos,
> independientemente de las herramientas que hayamos utilizado.

| Nombre | Número de cuenta |
|---|---|
| Angel Aaron Lopez Cruz| 426006422 |
| | |
