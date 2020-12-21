import streamlit as st
from charts.dots_plot import dots_plot
import json

def show_dots_plot():

  st.header("Dots Plot")

  st.markdown('''_Author: [Anh Minh Nguyen](http://github.com/minhanhng4an)_
  
  This chart can be a good alternative to the traditional bar chart to show the composition of a sample within a population.''')

  with open("charts/dots_plot.py", "r") as f:
    dots_plot_code = f.read()
    
  if st.checkbox("Show Code"):
    st.markdown(f'''
    ```python
    {dots_plot_code}
    ```
    ''')
    
  # -- PLOT PROPERTIES -- 
  st.sidebar.header("Plot Properties")

  st.sidebar.markdown("**Required**")
  NDOTS = st.sidebar.number_input("Number of dots", value=92)
  FILLED_DOTS = st.sidebar.number_input("Number of filled dots", value=31)

  st.sidebar.markdown("**Optional**")
  GRID_NROW = int(st.sidebar.number_input("Number of rows of the grid (Set to 0 to automatically calculate the number of rows)", value=0, min_value=0, max_value=NDOTS))
  GRID_NCOL = int(st.sidebar.number_input("Number of cols of the grid (Set to 0 to automatically calculate the number of cols)", value=0, min_value=0, max_value=NDOTS))
  GRID_WIDTH = int(st.sidebar.number_input("Width of the grid", value=5))
  GRID_HEIGHT = int(st.sidebar.number_input("Height of the grid", value=5))
  C_UNFILLED = st.sidebar.text_input("Color of unfilled dots", value="#bdc3c7")
  C_FILLED = st.sidebar.text_input("Color of filled dots", value="#2980b9")
  MARKER = st.sidebar.text_input("Dot style (Matplotlib marker style)", value="o")
  st.sidebar.markdown("See more about [Here](https://matplotlib.org/3.3.3/api/markers_api.html)")
  MARKER_SIZE = int(st.sidebar.number_input("Dot size", value=15))
  SHOW_LABEL = st.sidebar.checkbox("Show/Hide Label", value = True)
  LABLE_STYLE = st.sidebar.text_input("Label font style (Matplotlib fontdict)", value='''{"family": "sans-serif","size": 60, "color": "#2980b9", "weight": "bold"}''')
  st.sidebar.markdown('''See more about [Here](https://matplotlib.org/3.1.0/gallery/text_labels_and_annotations/text_fontdict.html)''')

  LABLE_STYLE = json.loads(LABLE_STYLE) # Parse string to dictionary

  if GRID_NROW <= 0: 
    GRID_NROW = None

  if GRID_NCOL <= 0:
    GRID_NCOL = None

  # -- PLOT --
  st.markdown("__Plot__")
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
                      show_label=SHOW_LABEL,
                      lable_style=LABLE_STYLE))