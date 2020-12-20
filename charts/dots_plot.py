import matplotlib.pyplot as plt
import numpy as np
import math

def generate_grid(nrows, ncols, ndots):
  """
  Generate grid of dots coordinates.
  
  Parameters:
    @Required:
    - nrows: Number of rows of the grid
    - ncols: Number of cols of the grid
    - ndots: Number of dot coordinates

  Return:
    2-D Numpy Array of the coordinates

  Example:
  generate_grid(2, 2, 3)
  >> array([[1, 1],
            [1, 2],
            [2, 1]])
  """

  # Validation
  if nrows * ncols < ndots:
    raise Exception("ndots must be <= than grid size")

  rows = np.arange(1, nrows + 1)
  cols = np.arange(1, ncols + 1)

  # Create empty matrix
  grid = np.empty((len(rows), len(cols), 2), dtype=np.intp)
  grid[..., 0] = rows[:, None]
  grid[..., 1] = cols 

  return grid.reshape(nrows * ncols, -1)[:ndots]

def dots_plot(ndots, filled_dots, 
             grid_nrow=None, 
             grid_ncol=None, 
             grid_width=10, 
             grid_height=10,
             c_unfilled="#bdc3c7", 
             c_filled="#2980b9", 
             marker="o", 
             marker_size=10, 
             show_label=True,
             lable_style={}):
  
  """
  Create "dots" plot.
  If grid_nrow OR grid_ncol is given, will attempt to create grid to fit ndots with given nrow/ncol. 
  Will both are given, will raise error if cannot form a grid to fit ndots.
  If none are given, will create a square grid to fit ndots.

  Parameters:
    @Required:
    - ndots: Total number of dots on the plot
    - filled_dots: Number of filled dots

    @Optional:
    - grid_nrow: Number of rows of the grid
    - grid_ncol: Number of cols of the grid
    - grid_width: Width of the grid
    - grid_height: Height of the grid
    - c_unfilled: Color of unfilled dots
    - c_filled: Color of filled dots
    - marker: Dot style (Matplotlib marker style)
    - marker_size: Dot size
    - show_label: Whether to show/hide label
    - lable_style: Title font style (Matplotlib fontdict)

  Return:
    Figure containing drawn plot 
  """

  # Validation
  if filled_dots > ndots:
    raise "filled_dots must be smaller than ndots" 

  if (grid_nrow and grid_ncol) and (grid_nrow * grid_ncol != ndots):
      raise Exception(f"Only either of nrow or ncol allowed for {ndots} dots.")

  # Default: Square grid that fits ndots
  nrow = ncol = math.ceil(math.sqrt(ndots)) 

  # Calculate grid based on grid_nrow
  if grid_nrow: 
    nrow = grid_nrow
    ncol = math.ceil(ndots / grid_nrow)
  
  # Calculate grid based on grid_ncol
  if grid_ncol:
    ncol = grid_ncol
    nrow = math.ceil(ndots / grid_ncol)

  # Generate grid data
  data = generate_grid(nrow, ncol, ndots)

  # Fill colors based on filled_dots
  colors = np.full(len(data), c_unfilled)
  colors[:filled_dots] = c_filled

  # Create plot
  fig, ax = plt.subplots(figsize=(grid_width, grid_height))

  # Title
  if show_label:
    ax.set_title(filled_dots, lable_style)

  # Scatter plot
  ax.scatter(x=data[:,1],
             y=data[:,0], 
             s=marker_size*20, 
             c=colors, 
             marker=marker)

  # Hide axis
  ax.set_axis_off()

  return fig
