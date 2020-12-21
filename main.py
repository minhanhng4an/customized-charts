import streamlit as st
from components import *

# -- PROJECT TITLE --
st.title("Build Your Own Customized Charts")

# -- PROJECT DESCRIPTION --
st.markdown('''
Welcome!

This project provides a quick and eascky-to-use tool for everyone to create highly customizable plots. 

To save a plot, Right-click on the plot and select `Save Image As...`

If you want to reuse the plot template for your own project, select `Show Code` to see template source code.

Templates for the plots are created by our contributors. To become a contributor, [send me an email](mailto:anhminhnguyen.ds@gmail.com)!

Source: [GITHUB](https://github.com/minhanhng4an/customized-charts)

__-- GET STARTED BY SELECTING A PLOT TYPE --__
''')

# -- SELECT PLOT --
plot_types = {
  "Dots Plot": show_dots_plot,
  "Bar Chart with Highlight": show_highlight_barchart
}

plot_list = plot_types.keys()

selected_plot = st.selectbox("Plot Type",
                            ["None"] + sorted(plot_list),
                            0)

# -- PLOT AREA --
if selected_plot != "None":
  plot_types[selected_plot]()