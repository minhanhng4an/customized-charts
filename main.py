
import streamlit as st
from charts.dots_plot import *

st.title("Build Your Own Customized Charts")

st.header("Dots Plot")

with open("charts/dots_plot.py", "r") as f:
  dots_plot_code = f.read()

if st.checkbox("Show Code"):

  f'''
  ```python
  {dots_plot_code}
  ```
  '''

st.sidebar.header("Chart Properties")

st.sidebar.markdown('''
**Required**
''')
NDOTS = st.sidebar.number_input("Number of dots", value=92)
FILLED_DOTS = st.sidebar.number_input("Number of dots", value=31)

st.sidebar.markdown('''
**Optional**
''')

GRID_NROW = int(st.sidebar.number_input("Number of rows of the grid (Use negative number to set to None)", value=-1))
GRID_NCOL = int(st.sidebar.number_input("Number of cols of the grid (Use negative number to set to None)", value=-1))
GRID_WIDTH = int(st.sidebar.number_input("Width of the grid", value=5))
GRID_HEIGHT = int(st.sidebar.number_input("Height of the grid", value=5))
C_UNFILLED = st.sidebar.text_input("Color of unfilled dots", value="#bdc3c7")
C_FILLED = st.sidebar.text_input("Color of filled dots", value="#2980b9")
MARKER = st.sidebar.text_input("Dot style (Matplotlib marker style)", value="o")
st.sidebar.markdown('''
See more about [Here](https://matplotlib.org/3.3.3/api/markers_api.html)
''')
MARKER_SIZE = int(st.sidebar.number_input("Dot size", value=15))
FONT_STYLE = st.sidebar.text_input("Title font style (Matplotlib fontdict)", value='''{"family": "sans-serif","size": 60, "color": "#2980b9", "weight": "bold"}''')
st.sidebar.markdown('''
See more about [Here](https://matplotlib.org/3.1.0/gallery/text_labels_and_annotations/text_fontdict.html)
''')

FONT_STYLE = eval(FONT_STYLE)

if GRID_NROW <= 0:
  GRID_NROW = None

if GRID_NCOL <= 0:
  GRID_NCOL = None

st.pyplot(dots_plot(ndots=NDOTS,
                    filled_dots=FILLED_DOTS,
                    grid_nrow = GRID_NROW,
                    grid_ncol = GRID_NCOL,
                    grid_width=GRID_WIDTH,
                    grid_height=GRID_HEIGHT,
                    c_unfilled = C_UNFILLED,
                    c_filled = C_FILLED,
                    marker=MARKER,
                    marker_size=MARKER_SIZE,
                    font_style=FONT_STYLE))