import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

def plot_residuals(res, pred, title):
    """
    Plot graphics to analyze residuals

    res : a trained model object from statsmodels
    """

    residus = res
    predicted_values = pred
    
    fig = plt.figure(figsize=(16,5))

    ax1 = fig.add_subplot(1, 3, 1)
    plt.hist(residus, bins=30, edgecolor='black')
    # sns.displot(residus, kind="kde", fill=True)
    ax1.set_xlabel('Residuals')
    ax1.set_xlabel('Frequence')
    ax1.set_title('Histogram of residuals')

    ax2 = fig.add_subplot(1, 3, 2)
    plt.scatter(predicted_values, residus, s=15)
    ax2.set_xlabel('Predicted values')
    ax2.set_ylabel('Residuals')
    plt.axhline(y=0, color='red', linestyle='--')  # Ajout d'une ligne à zéro pour la référence
    ax2.set_title('Scatter plot of residuals')

    ax3 = fig.add_subplot(1, 3, 3)
    stats.probplot(residus, dist="norm", plot=plt)
    ax3.set_xlabel('Theoretical quantiles')
    ax3.set_ylabel('Residuals quantiles')
    ax3.set_title('QQ-residual plot')

    plt.suptitle(title, y = 1.03, fontsize=15)

    plt.show()
    plt.tight_layout()
    plt.close()