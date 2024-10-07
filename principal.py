import streamlit as st
#import hydralit_components as hc
import datetime
import base64
import pandas as pd
from io import BytesIO
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as mplt
import matplotlib.font_manager as font_manager
import mplsoccer
from mplsoccer import Pitch, VerticalPitch, FontManager
import sklearn
from sklearn.preprocessing import StandardScaler
from scipy.spatial import ConvexHull
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patheffects as path_effects
from scipy.ndimage import gaussian_filter
import seaborn as sns
from matplotlib import colors as mcolors
import requests
#from PIL import Image
from matplotlib.patches import Rectangle
import math
############################################################################################################################################################################################################################
st.set_page_config(layout="wide")
navigation_tree = {
    "Menu": [
        st.Page("cont/WinStats.py", title="Win Stats", icon=":material/download:"),
        #st.Page("cont/OptaJoinData.py", title="Join Data", icon=":material/cell_merge:"),
        st.Page("cont/PilotData.py", title="Pilot Data", icon=":material/analytics:"),        
        st.Page("cont/RegisterData.py", title="Register Data", icon=":material/leaderboard:")]
}
nav = st.navigation(navigation_tree, position="sidebar")
nav.run()
