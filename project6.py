# -----------------------------------------
# Rossman Sales Data - Streamlit App
# -----------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# -----------------------------------------
# SETTINGS
# -----------------------------------------
sns.set(style="whitegrid")
st.set_page_config(page_title="Rossman Sales", layout="wide")

st.title("Rossman Sales Forcasting")

# -----------------------------------------
# LOAD DATA
# -----------------------------------------
train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")
store=pd.read_csv("store.csv")
sample_submission=pd.read_csv("sample_submission.csv")
