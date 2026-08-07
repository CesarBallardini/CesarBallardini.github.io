### A1-22 — El modelo de objetos de Python: `__class__`, `__dict__` y `__slots__`

- **Archivo seed:** _nace el 2026-08-05, de lo que quedó afuera de [[C-17]] (DCI en Python)_
- **Slug propuesto:** `modelo-de-objetos-python-class-dict-slots`
- **Comando:** `hugo new content/es/posts/YYYY-MM-DD-modelo-de-objetos-python-class-dict-slots/index.md`
- **Serie:** lenguajes
- **Cross-links:** [[C-17]] (DCI en Python — de ahí sale el material y ahí está el caso de uso que lo motiva), [[C-09]] (DCI, la idea)
- **Idioma:** es
- **Madurez:** semilla con material verificado (2026-08-05). **Todo lo que está en «Material ya verificado» fue ejecutado**, no recordado.
- **Length target:** medium — ~2000 palabras, con mucho código corto y salidas reales.

> **Ojo con el encuadre de la serie.** Va en `lenguajes/` porque es un post sobre un lenguaje, pero la serie A1 es sobre todo historia y biografías de lenguajes clásicos, y éste es un post de internals. Si al escribirlo pesa más lo técnico que lo histórico, quizá quiera ser su propia cosa. Decisión de César.

**Concepto:** Casi todo programador de Python sabe que los objetos guardan sus atributos en un `__dict__` y que `__slots__` «ahorra memoria». Muy pocos saben qué es exactamente lo que `__slots__` cambia, y prácticamente nadie sabe que a una instancia viva se le puede reasignar la clase — ni bajo qué regla Python lo permite. Este post recorre el modelo de objetos por el lado por el que casi nunca se lo mira: el de las tres cosas que definen el *layout* de una instancia, y qué operaciones habilita o prohíbe cada una.

El gancho es que la regla que todo el mundo repite —«`__slots__` te saca el `__dict__`»— **es falsa**, y se demuestra en cinco líneas.

**Hook:** `obj.__class__ = OtraClase` es una línea de Python perfectamente legal que cambia de qué clase es un objeto que ya existe, sin destruirlo, sin copiarlo y sin que cambie su `id()`. A veces anda. A veces te dice `object layout differs`. La explicación que vas a encontrar en Stack Overflow es que los slots le sacan el diccionario al objeto, y es mentira: un `__slots__ = ()` no le saca nada a nadie y rompe igual.

**Outline:**

1. **El truco de entrada**: reasignar `__class__` a una instancia viva. Anda, conserva `id()`, conserva `isinstance`. La reacción normal es «esto no debería ser legal».
2. **Dónde viven los atributos**: `__dict__` por instancia, el `__dict__` de la clase, y el MRO. Por qué `a.x` no es una sola búsqueda.
3. **Qué es realmente `__slots__`**: descriptores a offsets fijos en la estructura C de la instancia, en vez de una entrada en un diccionario. El ahorro de memoria es consecuencia, no propósito.
4. **La regla que Python aplica de verdad**: `__basicsize__`, `__dictoffset__`, `__weakrefoffset__` y la *solid base*. Acá va la demolición del mito, con la tabla de casos de más abajo.
5. **Managed dict**: por qué desde 3.11 `__dictoffset__` da negativo y qué significa eso.
6. **Para qué sirve todo esto**: los usos reales de la reasignación de `__class__` — el patrón State, los objetos que cambian de comportamiento al inicializarse del todo, y la inyección de roles de DCI ([[C-17]]).
7. **Lo que se rompe igual**: `pickle` no puede serializar una instancia cuya clase se construyó en runtime, aunque la reasignación haya sido legal. `copy.deepcopy` sí puede.
8. Cierre: el modelo de objetos de Python es más maleable de lo que su documentación sugiere y más rígido de lo que su reputación sugiere, y las dos cosas se explican con la misma regla.

**Material ya verificado** _(ejecutado el 2026-08-05 en CPython 3.14.4; hay que re-verificar en la versión vigente al escribir)_

Reasignación de `__class__` mezclando un rol sobre la clase de datos, `type(f'{cls.__name__}@{role.__name__}', (role, cls), {})`:

| Clase de datos | Rol sin `__slots__` | Rol con `__slots__ = ()` | ¿La instancia tenía `__dict__`? |
| --- | :---: | :---: | :---: |
| clase común | ✅ anda | ❌ falla | sí |
| `__slots__ = ()` | ❌ falla | ❌ falla | **no** |
| subclase de una `__slots__ = ()` | ❌ falla | ❌ falla | **sí** |
| `__slots__ = ('a',)` | ❌ falla | ❌ falla | no |
| `@attrs.define` (slots por defecto) | ❌ falla | ❌ falla | no |
| `@dataclass(frozen=True)` | ❌ `FrozenInstanceError` | ❌ ídem | sí |
| `DeclarativeBase` de SQLAlchemy | ❌ falla | ❌ falla | **sí** |
| `BaseModel` de pydantic v2 | ✅ anda | — | sí |

Las tres filas en negrita son las que matan el mito: **la instancia tiene `__dict__` y la reasignación falla igual**. Y la primera fila de la segunda columna es la contracara: el rol con `__slots__ = ()` rompe un caso que andaba. No es una cuestión de diccionarios, es de qué clase se hereda el layout.

Números crudos del mismo experimento, útiles para el punto 4:

```
Acc (SQLAlchemy declarativo):
  Acc(d=-1,w=-32,b=16) -> JustBase(d=-1,w=-32,b=16) -> DeclarativeBase(d=-1,w=-32,b=16)
  -> Inspectable(d=0,w=0,b=16) -> Generic(d=0,w=0,b=16) -> object(d=0,w=0,b=16)
Clase común:
  Plain(d=-1,w=-32,b=16) -> object(d=0,w=0,b=16)
```

(`d` = `__dictoffset__`, `w` = `__weakrefoffset__`, `b` = `__basicsize__`.) El salto de `d=-1` a `d=0` entre `DeclarativeBase` e `Inspectable` es donde se corta la cadena, y `Inspectable` es la que declara `__slots__ = ()`.

Y la rotura del punto 7, también verificada:

```
pickle   -> PicklingError: Can't pickle <class '__main__.Plain@Role'>:
            it's not found as __main__.Plain@Role
deepcopy -> anda
```

**Bibliografía:** _(nada de esto está fetcheado todavía — es la lista de lo que hay que buscar, no de lo que está confirmado)_

- **`Objects/typeobject.c` de CPython** — la fuente real: `compatible_for_assignment()`, `equiv_structs()`, `same_slots_added()` y `solid_base()`. Es la única documentación de la regla que se aplica de verdad, porque el *Data model* no la enuncia. **Hay que citar el archivo y la función, con permalink a un tag de release, no a `main`.**
- **[Python Data model](https://docs.python.org/3/reference/datamodel.html)** — la sección de `__slots__` y la de `__class__`. Verificar qué dice y qué **no** dice sobre la reasignación: la impresión al escribir esta semilla es que la documenta como posible sin enunciar la condición.
- **PEP 412 — Key-Sharing Dictionary** — por qué el `__dict__` de una instancia no cuesta lo que uno cree, que es la mitad del argumento de memoria a favor de `__slots__`.
- **Los *What's New* de 3.11 y 3.12** — el *managed dict* (`Py_TPFLAGS_MANAGED_DICT`) y de dónde sale el `__dictoffset__` negativo. Confirmar en qué versión exacta entró.
- Documentación de **`attrs`** sobre `@define` y `slots=True` por defecto, y de **SQLAlchemy** sobre `DeclarativeBase`, para sostener que a los slots se llega sin pedirlos.
- El post [[C-17]] y su repo `dci-in-python`, de donde sale todo el material verificado.

**Imágenes:**

- **Hero**: un diagrama de la estructura C de una instancia — `PyObject_HEAD`, los slots como offsets fijos, el puntero al `__dict__` — contra la misma instancia sin slots. Material propio, sin problema de licencia. Alternativa barata: captura de terminal de la tabla ✅/❌ de más arriba.
- **Diagrama mermaid**: la cadena de *solid bases* de los dos casos —clase común y declarativo de SQLAlchemy— mostrando dónde se corta. Requiere `mermaid: true` y probablemente `mermaid_html_labels: true`.

**Tags propuestos:** `['Python', 'modelo de objetos', 'CPython', 'slots', 'metaprogramacion', 'internals']`

**Estado actual:** 🌱 **semilla con material fuerte.** Nació el 2026-08-05 mientras se verificaban las afirmaciones de [[C-17]]: al probar por qué fallaba la inyección de roles apareció que la explicación corriente del `__slots__` es falsa, y eso es demasiado bueno para gastarlo en un párrafo de otro post. El material experimental ya existe y está corrido; lo que falta es la bibliografía —**ninguna fuente está fetcheada todavía**— y decidir el encuadre.

**Pendiente:**

- Fetchear y confirmar **toda** la bibliografía. Nada de lo listado arriba está verificado; las afirmaciones sobre qué dice o no dice la documentación oficial son impresiones, no lecturas.
- Leer `compatible_for_assignment()` en el fuente de CPython y **contar la regla en castellano**, que es el corazón del post. Sin eso, el post describe un síntoma y no explica nada — que es justamente el pecado que le señala a Stack Overflow.
- Re-correr la tabla en la versión de Python vigente al escribir, y decir en el post con cuál se corrió.
- Decidir si el post se publica antes o después de [[C-17]]. Si va después, puede apoyarse en él; si va antes, [[C-17]] puede delegarle la explicación del `__slots__` y quedarse con una línea.
