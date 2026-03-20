# Visualization Utilities

This module includes utility functions for generating various types of charts and visualizations.

## Functions

### 1. `plot_bar_chart(data, title, xlabel, ylabel)`
Generates a bar chart from the given data.

- **Parameters:**
    - `data` (dict): A dictionary where keys are categories and values are their respective values.
    - `title` (str): The title of the chart.
    - `xlabel` (str): The label for the x-axis.
    - `ylabel` (str): The label for the y-axis.

### 2. `plot_line_chart(data, title, xlabel, ylabel)`
Generates a line chart from the given data.

- **Parameters:**
    - `data` (dict): A dictionary where keys are data points and values are their respective values.
    - `title`, `xlabel`, `ylabel`: Same as above.

### 3. `plot_pie_chart(data, title)`
Generates a pie chart for the given data.

- **Parameters:**
    - `data` (dict): A dictionary where keys are categories and values are their respective proportions.
    - `title` (str): The title of the chart.

### Example Usage
```python
import matplotlib.pyplot as plt

# Sample data
bar_data = {'Category A': 10, 'Category B': 20, 'Category C': 15}

plot_bar_chart(bar_data, 'Sample Bar Chart', 'Categories', 'Values')
plt.show()
```
