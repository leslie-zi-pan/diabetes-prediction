import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def plot_split_stratfied_distributions(
    df_train: pd.DataFrame, df_test: pd.DataFrame, stratify: str,
    title=None) -> None:
    fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True)

    sns.barplot(ax=axes[0], data=df_train[stratify].value_counts().reset_index(), x="index", y=stratify)
    sns.barplot(ax=axes[1], data=df_test[stratify].value_counts().reset_index(), x="index", y=stratify)
    
    for idx, axis in enumerate(axes):
        is_train = idx == 0
        
        prefix_datatype = "train" if is_train else "test"
        
        axis.set_xlabel(f"{prefix_datatype.title()} {stratify.title()} Dataset", fontsize=10)
        axis.set_ylabel("Frequency", fontsize='medium')
        
    if not title:
        fig.suptitle(f"Train Test Split Stratified by {stratify.title()} Column", fontsize=14)
    else:
        fig.suptitle(title, fontsize=14)
    
    return fig


def save_plot(plt: plt.Figure , fp: str) -> None:
    plt.savefig(fp, format="png")

def save_split_stratfied_distributions_plot(
        df_train: pd.DataFrame, df_test: pd.DataFrame, stratify: str, 
        file_path: str, title=None) -> None:

    plot = plot_split_stratfied_distributions(
    df_train, df_test, stratify, title) 

    save_plot(plot, file_path)