import matplotlib.pyplot as plt
from scipy import stats
from sklearn.metrics import root_mean_squared_error, r2_score

def plot_residuals(y_true, pred, title):
    """
    Function to plot residuals of a model
    
    Parameters
    ----------
    res : array-like
        residuals of a model
    pred : array-like
        predicted values of a model
    title : str
        title of the plot
    """
    
    residus = y_true - pred
    
    fig = plt.figure(figsize=(16,5))

    ax1 = fig.add_subplot(1, 3, 1)
    plt.hist(residus, bins=30, edgecolor='black')
    ax1.set_xlabel('Residuals')
    ax1.set_xlabel('Frequence')
    ax1.set_title('Histogram of residuals')

    ax2 = fig.add_subplot(1, 3, 2)
    plt.scatter(pred, residus, s=15)
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


def adjusted_r2(r2, n, p):
    """
    Calculate the adjusted R-squared of a model.

    Parameters
    ----------
    r2 : float
        The R-squared of the model.
    n : int
        The sample size.
    p : int
        The number of parameters in the model.

    Returns
    -------
    float
        The adjusted R-squared of the model.
    """
    """"""
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)


def plot_boxplot(dataframe, title='', fliers = True, return_whiskers = True, feature_name=''):
    """
    Plot a boxplot of the given dataframe and feature.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        The dataframe containing the data.
    title : str, optional
        The title of the plot. Defaults to ''.
    fliers : bool, optional
        Whether to show outliers. Defaults to True.
    return_whiskers : bool, optional
        Whether to return the lower and upper whiskers. Defaults to True.
    feature_name : str, optional
        The name of the feature to plot. Defaults to ''.

    Returns
    -------
    tuple, optional
        If return_whiskers is True, returns the lower and upper whiskers.
    """
    fig, ax = plt.subplots(1, 1)# figsize=(20, 7))
    box = ax.boxplot(dataframe[feature_name], showfliers=fliers)
    ax.set_title(feature_name)
    lower_whisker = box['whiskers'][0].get_ydata()[1]
    upper_whisker = box['whiskers'][1].get_ydata()[1]
    print(f'--------{feature_name}--------')
    print(f"Lower Whisker: {lower_whisker}")
    print(f"Upper Whisker: {upper_whisker}\n")
    plt.tight_layout()

    plt.show()
    plt.close()
    if return_whiskers:
        return lower_whisker, upper_whisker
    


def print_results(y_true, y_pred, n, p):
    """
    Print the results of a model evaluation.

    Parameters
    ----------
    y_true : array-like
        The true values.
    y_pred : array-like
        The predicted values.
    n : int
        The number of samples.
    p : int
        The number of features.

    Returns
    -------
    None
    """
    rmse = root_mean_squared_error(y_true, y_pred)
    mse = pow(rmse, 2)
    r2 = r2_score(y_true, y_pred)
    print(f"MSE : {mse:.3f}")
    print(f"R2 : {r2:.3f}")
    print(f"Adjusted R2 : {adjusted_r2(r2, n, p):.3f}\n")



