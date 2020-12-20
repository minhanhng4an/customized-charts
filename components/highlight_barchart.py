import streamlit as st
import pandas as pd
import json
from charts.highlight_barchart import highlight_barchart
from io import StringIO

# TODO: Write doc

def show_highlight_barchart():
  st.header("Bar Chart with Highlight")

  st.markdown('''<Description>''')
  with open("charts/highlight_barchart.py", "r") as f:
    dots_plot_code = f.read()
    
  if st.checkbox("Show Code"):
    st.markdown(f'''
    ```python
    {dots_plot_code}
    ''')

  with open("data/highlight_barchart_data.csv", "r") as f:
    example_text = f.read()
  

  st.sidebar.header("Chart Properties")

  st.sidebar.markdown('''
  **Required**
  ''')

  DATA = st.sidebar.text_input("Input Data (csv). Open csv file in a text editor and copy the content to this field.", value=example_text)
  DATA="\n".join(DATA.split(" "))
  string_data = StringIO(DATA)
  data = pd.read_csv(string_data)
  st.markdown("__Data__")
  st.dataframe(data)

  CATEGORY_NAME = st.sidebar.text_input("Name of Category Column. If left empty, select first column.", value="category")
  VALUE_NAME= st.sidebar.text_input("Name of Value Column. If left empty, select second column.", value="valueA")
  HIGHLIGHT_INDEX = int(st.sidebar.number_input("Index of Highlighted Value (In current sorting order)", value=3, min_value=0, max_value=len(data)-1))

  st.sidebar.markdown('''
  **Optional**
  ''')

  GRID_WIDTH = int(st.sidebar.number_input("Width of the grid", value=7))
  GRID_HEIGHT = int(st.sidebar.number_input("Height of the grid", value=5))
  C_DEFAULT = st.sidebar.text_input("Default bar color", value="#bdc3c7")
  C_HIGHLIGHT = st.sidebar.text_input("Color of highlighted bar", value="#2980b9")
  ALIGNTMENT = st.sidebar.text_input("Bar Alignment Stype, either vertical or horizontal.", value="vertical")
  SORTED = st.sidebar.checkbox("Whether to sort data by value. Default: Sort by key", value=False)
  ASCENDING = st.sidebar.checkbox("Sort in ascending order", value=False)
  XLABEL = st.sidebar.text_input("X-axis label", value="")
  YLABEL = st.sidebar.text_input("Y-axis label", value="")
  SHOW_LABEL = st.sidebar.checkbox("Whether to show data label. (Coming soon)", value=True)
  LABLE_STYLE = st.sidebar.text_input("Label font style (Matplotlib fontdict)", value="{}")
  st.sidebar.markdown('''
  See more about [Here](https://matplotlib.org/3.1.0/gallery/text_labels_and_annotations/text_fontdict.html)
  ''')

  LABLE_STYLE = str(json.loads(LABLE_STYLE))

  st.pyplot(highlight_barchart(data,
             CATEGORY_NAME,
             VALUE_NAME,
             HIGHLIGHT_INDEX,
             grid_width=GRID_WIDTH, 
             grid_height=GRID_HEIGHT,
             c_default=C_DEFAULT, 
             c_highlight=C_HIGHLIGHT, 
             alignment=ALIGNTMENT, 
             sorted=SORTED,
             ascending=ASCENDING,
             xlabel=XLABEL,
             ylabel=YLABEL,
             show_label=SHOW_LABEL,
             lable_style=LABLE_STYLE))