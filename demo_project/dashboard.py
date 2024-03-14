import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime

dg_agg = pd.read_csv('Aggregated_Metrics_By_Video.csv').iloc[1:,:]
print(dg_agg)