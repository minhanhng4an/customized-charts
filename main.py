import streamlit as st
from components import *

st.title("Build Your Own Customized Charts")

plot_types = {
  "Dots Plot": show_dots_plot,
  "Bar Chart with Highlight": show_highlight_barchart
}

plot_list = plot_types.keys()

selected_plot = st.selectbox("Plot Type",
                            ["None"] + sorted(plot_list),
                            0)

if selected_plot != "None":
  plot_types[selected_plot]()