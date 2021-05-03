import numpy as np
import seaborn as sns
import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# Text/Title
st.title("Data Analysis Dictionary")
st.text("online source for Data Analysis definitions, synonyms, word origins and etymologies, example sentences")

# load csv data

sheetid = "1O3Ig5AMCgX_CIlRvFn9CDDCrK_cjuMMhjlwFj88-68s"
sheet_name = ""

sheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(
    sheetid, sheet_name)

sheet_url

df = pd.read_csv(sheet_url)
df
