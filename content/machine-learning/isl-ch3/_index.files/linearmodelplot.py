
import numpy as np
import pandas as pd
import scipy
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns

import statsmodels.api as sm
import statsmodels.formula.api as smf


import warnings
warnings.simplefilter('ignore',FutureWarning)

# Hard work credit: http://emredjan.github.io/blog/2017/07/11/emulating-r-plots-in-python/

def plot_add_label(ax, xlabel=None, ylabel=None, title=None):
    if ax == None: return ax
    if xlabel: ax.set_xlabel(xlabel);
    if ylabel: ax.set_ylabel(ylabel);
    if title: ax.set_title(title);
    return ax

def plot_add_lowess(x, y, ax, color='red'):
    if ax == None: raise RuntimeException('Lowess needs axes to work with!')
    smooth_data = sm.nonparametric.lowess(endog=y, exog=x)
    fig = sns.lineplot(x=smooth_data[:,0], y=smooth_data[:,1], color=color, ax=ax)
    return fig

def plot_1_resid_vs_fitted(lm_fit, 
                           ax = None, 
                           xlabel="fitted values",
                           ylabel="residuals",
                           title="Residuals vs fitted values"):
    if ax == None: ax = plt.gca()
    x = lm_fit.fittedvalues
    y = lm_fit.resid
    fig = sns.scatterplot(x=x, y=y, ax=ax);
    xrange = ax.get_xlim()
    zeros = np.zeros(2)
    sns.lineplot(xrange, zeros, color='gray', style = zeros, dashes=[[2,4]], legend=False, ax=ax);
    plot_add_lowess(x,y,ax)
    plot_add_label(ax, xlabel=xlabel, ylabel=ylabel, title=title)
    return fig

def plot_2_residuals_vs_normal (lm_fit, 
                                ax = None, 
                                xlabel="Theoretical Quantiles",
                                ylabel="Standardized Residuals",
                                title="Normal Q-Q"):
    y_residuals = lm_fit.get_influence().resid_studentized_internal
    if ax == None: ax = plt.gca()
    fig = sm.qqplot(y_residuals, line='q', ax=ax)
    plot_add_label(ax, xlabel=xlabel, ylabel=ylabel, title=title)
    return fig

def plot_3_std_resid_vs_fitted(lm_fit,
                               ax = None, 
                               xlabel="fitted values",
                               ylabel="$\sqrt{|{Standardized residuals}|}$",
                               title="Scale-Location"):
    if ax == None: ax = plt.gca()
    x = lm_fit.fittedvalues
    y = lm_fit.get_influence().resid_studentized_internal
    fig = sns.scatterplot(x=x, y=y, ax=ax)
    plot_add_lowess(x, y, ax)
    plot_add_label(ax, xlabel=xlabel, ylabel=ylabel, title=title)
    return fig

def plot_4_std_resid_vs_leverage(lm_fit,
                                 ax = None, 
                                 xlabel="Leverage",
                                 ylabel="Standardized residuals",
                                 title="Residuals vs Leverage"):
    if ax == None: ax = plt.gca()
    x = lm_fit.get_influence().hat_matrix_diag  # leverage
    y = lm_fit.get_influence().resid_studentized_internal # studentized residuals
    fig = sns.scatterplot(x=x, y=y, ax=ax)
    plot_add_lowess(x, y, ax)
    plot_add_label(ax, xlabel=xlabel, ylabel=ylabel, title=title)
    return fig

def plot_lm_summary(lm_fit,
                    title="Linear Model Summary (R-style)",
                    figsize=(15,10)):
    """Produce an R-style summary of a fitted linear model.
    The linear model must be the result of a StatsModel OLS."""
    fig, ax = plt.subplots(nrows=2,ncols=2, figsize=figsize)
    plot_1_resid_vs_fitted(lm_fit, ax=ax[0,0]);
    plot_2_residuals_vs_normal(lm_fit, ax=ax[0,1]);
    plot_3_std_resid_vs_fitted(lm_fit, ax=ax[1,0]);
    plot_4_std_resid_vs_leverage(lm_fit, ax=ax[1,1]);
    if title: fig.suptitle(title, fontsize=18)
    return fig

