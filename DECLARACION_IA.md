# Declaración de uso de Inteligencia Artificial

**Actividad: Tarea 1: mini interprete**

**Integrantes: <br> Angel Aaron Lopez Cruz <br> Gabriel Lugo Rosete**

**Fecha: 19/10/2026**

---

## 0. ¿Se usó IA en esta actividad?


 **Sí.** 

---

## 1. Herramienta(s) utilizada(s)

| Herramienta | Versión o modelo, si lo saben |
|---|---|
| ChatGPT | GPT-6 Luna |

Adicionalmete un integrante "uso" el autocompletado de Copilot (Simplete esta pero no se le dio utilidad.)


---

## 2. Objetivo del uso

| Para qué la usamos | En qué parte del entregable |
|---|---|
| Para verificar el uso de Factory Method y una considerción de su uso| En Analisis.md en la pregunta 5.3 |


---

## 3. Prompts principales

Textuales, tal como los escribieron. No los limpien ni los reescriban.

```
Se podría usar factory method en alguna parte del programa actulamente y que valga la pena, como usar factory method para los operadores de suma y otro para los de producto
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
|---|---|---|---|
| Un analisis sobre Factory Method y su posible uso en el programa, al igual si era pertinente o no en el ejemplo de uso propuesto | Se aceptó su analisis sobre Factory Method y la propuesta, aunque se modificó en el analisis el uso de Factory Method o no más generalmente  | Se enfocó mucho en la propuesta del ejemplo de su uso y no era completamente claro porque sería pertinente o no el uso de Factory Method o no generalmente, por lo que se modifico para tomar otro enfoque. | En analisis.md en commit de pregunta 5.3 ¿Sería pertinente usar Factory Method, Adapter o ninguno?|


### 4.1 Si la usaron para el análisis: el contraste

Se les pidió intentarlo primero por su cuenta. Si lo hicieron así:

|  |  |
|---|---|
| ¿Qué encontró la herramienta que ustedes **no** habían notado? | Se uso en el analisis extra para ver el flujo del programa y encontrar la causa del primer fallo. Ayudo a ahorrar tiempo para ver el orden exacto de por que fallaba, algo que no se noto en una revision rapida. <br><br> Se usó en el analisis de la pregunta 5.3 y encontró una explicación más centrada de porque en la implementación actual en la propuesta no sería el mejor uso Factory Method y como aun aplicandolo las operaciones tenian que ser representadas por OperacionBinaria, por lo que las fábricas tenian la misma tarea. |
| ¿Qué **no** encontró, que en este curso sí consideramos un problema? | Solo detecto el fallo para un ejemplo en especifico (`"1.1 + 1"`), dando una solucion solo para ese caso sin impartarle  que el mismo error pasaba en expresiones mas largas (como `"2 + 3 + 5.1 * 20"`) u otros casos . No vio el problema general que abarcaba mas codigo lo puedo comparar a lo dicho en clase (que una pruba pase no significa que el el programa sea correcto).<br><br> No encontró muchas más razones generales de porque Factory Method no sería pertinente actualmente fuera del ejemplo dado del uso de Factory Method y no mencionó casi cuando si podría ser útil su uso. |


### 4.2 ¿Cómo verificaron que lo que incorporaron era correcto?

El resultado dio una serie de pasos que ejecuta el programa , se realizaron los mismos pasos a mano con otros ejemplos y se detecto el mismo problema.

Revisando el código y como ambas si son representadas mediante la misma clase OperacionBinaria y junto con los apuntes de clase de cuando si es útil usar Factory Method y su propósito.


---

## 5. Reflexión

### 5.1 ¿Qué limitación concreta observaron **en esta actividad**?


    Si pasas un ejemplo particular para preguntar ¿Porque el programa tiene este comportamiento (Ejemplo)?, se enfoca demasiado en ese caso en particular, luego sin pedirselo te da soluciones, recomendaciones y cambios, que no son del todo correctos, no cosidera nada mas alla de responderte eso especifico en el momento. Al encontrarse mas casos desde antes, se entendio que la respuesta estaba incompleta.
    Para Factory Method se enfocó demasiado en el ejemplo sobre el que se le preguntó cómo se aplicaría y cuando valdría la pena ese ejemplo específicamente, no dió una explicación o un enfoque más general.

    La IA puede hacerte confiar de mas en el resultado que se tiene al final.


### 5.2 ¿Qué harían distinto la próxima vez?

Ser mas especifico en lo que se pide, dar mas contexto, pero lo realmente importante es entender mejor el tema y asegurarse siempre de que la respuesta es correcta, pensando en varios casos, y de ser posible demostrarla despues de entender bien su respuesta.
---

## Firma


| Nombre | Número de cuenta |
|---|---|
| Angel Aaron Lopez Cruz| 426006422 |
| Gabriel Lugo Rosete| 323017523 |
