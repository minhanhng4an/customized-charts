# Build Your Own Customized Charts

Welcome!

This project provides a quick and eascky-to-use tool for everyone to create highly customizable plots.

To save a plot, Right-click on the plot and select `Save Image As...`

If you want to reuse the plot template for your own project, select `Show Code` to see template source code.

> **<a href="https://share.streamlit.io/minhanhng4an/customized-charts/main/main.py" target="_blank">See Project</a>**


## Contribute to the project

Plots of this project are made using Matplotlib.

Templates for the plots are created by our contributors. To become a contributor, [send me an email](mailto:anhminhnguyen.ds@gmail.com)!

After you accept your invitation, follow the steps below to add your own plot template.

1. Clone this project

```
git clone git@github.com:minhanhng4an/customized-charts.git
```

2. Navigate to the project folder

```
cd customized-charts
```

3. Create virtual environment. I highly recommend using `conda`.

```
conda create -n customized-charts
```

4. Activate virtual environment and install dependencies

```
conda activate customized-charts
pip install -r requirements.txt
```

5. To run the app:

```
streamlit run main.py
```

6. In folder `charts`, create `your_plot_name.py` (`your_plot_name` is the name of the plot you want to make)

This file contains the template (written in functions) to create your plot. Its content will be also be displayed when user clicks `Show Code`.

You are encouraged to add more customization options to the template.

Please also take the time to write documentation for the template.

_File template:_

```python

import matplotlib.pyplot as plt

def helper_function():
  """
  Helper Function for the template (if any)
  """

  return

def your_plot_name():
  """
  Plot Template
  """

  fig, ax = plt.subplots()

  return fig # Return the figure with drawn plot

```

7. In folder component, create `your_plot_name.py` (`your_plot_name` is the name of the plot you want to make)

This file contains the code (written in functions) to render the Plot Area and Plot Properties section on Streamlit (<a href="https://docs.streamlit.io/en/stable/api.html" target="_blank">Documentation</a>).



_File template:_

````python
import streamlit as st

from charts.your_plot_name import your_plot_name

def show_your_plot_name():

  # -- HEADER --
  st.header("Your Plot Name") # TODO


  # -- DESCRIPTION --
  st.markdown('''_Author: [Your Name](http://github.com/your_github)_

  <Short Description about the plot>
  ''') # TODO

  with open("charts/your_plot_name.py", "r") as f: # TODO
    dots_plot_code = f.read()

  # -- SHOW CODE --
  if st.checkbox("Show Code"):
    st.markdown(f'''
    ```python
    {dots_plot_code}
    ''')

  # -- PLOT PROPERTIES --
  # Use st.sidebar
  st.sidebar.header("Plot Properties")

  st.sidebar.markdown("**Required**")
  # TODO

  st.sidebar.markdown("**Optional**")
  # TODO

  # -- PLOT --
  st.markdown("__Plot__")
  st.pyplot(your_plot_name()) # TODO

````

8. Add to `components/__init__.py`:

```python
# ...
# ...
from .your_plot_name import show_your_plot_name
```

9. Add to dictionary `plot_types` in `main.py`

```python
plot_types = {
  # ...
  # ...
  "Your Plot Name": show_your_plot_name
}
```
