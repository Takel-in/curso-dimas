#DataFrame

import pandas as pd

personas = {
    "nombre": ["dimas", "Juan", "Ana"],
    "edad" : [23, 24, 25],
    "país" : ["España", "Mexico", "Chile"]
}

df = pd.DataFrame(personas)
df