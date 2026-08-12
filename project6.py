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
train=pd.read_csv("C:/Users/vijay/OneDrive/Desktop/project6/train.csv")
test=pd.read_csv("C:/Users/vijay/OneDrive/Desktop/project6/test.csv")
store=pd.read_csv("C:/Users/vijay/OneDrive/Desktop/project6/store.csv")
sample_submission=pd.read_csv("C:/Users/vijay/OneDrive/Desktop/project6/sample_submission.csv")
