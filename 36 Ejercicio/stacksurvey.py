import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

result = pd.read_csv("./36 ejercicio/data/survey_results_public.csv", index_col="ResponseId")
resultSchema = pd.read_csv("./36 ejercicio/data/survey_results_schema.csv")