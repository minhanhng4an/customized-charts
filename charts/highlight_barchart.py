import matplotlib.pyplot as plt
import numpy as np
import math

def highlight_barchart(data,
             category_name,
             value_name,
             highlight_index,
             grid_width=10, 
             grid_height=10,
             c_default="#bdc3c7", 
             c_highlight="#2980b9", 
             alignment="vertical", 
             sorted=False,
             ascending=False,
             xlabel="",
             ylabel="",
             show_label=True,
             lable_style={}):
  """
  TODO: Write doc
  """

  if alignment not in ["vertical", "horizontal"]:
    raise Exception('alignment must be "vertical" or "horizontal".')

  # Data preprocessing
  if category_name:
    data = data.set_index(data[category_name])
  else:
    data = data.set_index(data.iloc[:,0])

  if value_name:
    data = data[value_name]
  else:
    data = data.iloc[:,1]

  if sorted:
    data = data.sort_values(ascending=ascending)


  fig, ax = plt.subplots(figsize=(grid_width, grid_height))

  colors = np.full(len(data), c_default)
  colors[highlight_index] = c_highlight

  if alignment == "vertical":
    ax.bar(data.index, data.values, color=colors)
  else:
    ax.barh(data.index, data.values, color=colors)

  ax.set(xlabel=xlabel,
         ylabel=ylabel)

  # TODO: Implement show_label
  # TODO: Add more customization options

  return fig
