# data_visualization/views.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from django.shortcuts import render
from django.http import HttpResponse
import base64
from io import BytesIO

def plot_graph(request):
    # Sample data generation using NumPy and Pandas
    data = np.random.rand(100)
    df = pd.DataFrame({'Data': data})

    # Data visualization using Matplotlib and Seaborn
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x=df.index, y='Data')
    plt.title('Random Data Trend')
    plt.xlabel('Index')
    plt.ylabel('Value')

    # Saving plot to a buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encoding plot image
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    # Render the plot in a simple HTML template
    return render(request, 'data_visualization/plot.html', {'graphic': graphic})

