#!/usr/bin/env python
# coding: utf-8

#  ### Is it possible to see the data in Python without having to export in a file? 
#  
#  # YES

# ### 1.0 Import necessary libraries

# In[1]:


# Libraries to help with data visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Libraries to help with reading and manipulating data
import numpy as np
import pandas as pd


# ### 1.1 Load the dataset
# The dataset containing the different attributes of used cars sold in different locations is contained in the file titled "anime_data_raw.csv" in my particular directory.

# In[2]:


# loading the dataset
my_dataset = pd.read_csv("RegisterData1.csv")
my_dataset


# In[3]:


my_dataset.head(10)


# ### 1.2 Check out the shape of the dataset

# In[4]:


print(
    f"The dataset contains {my_dataset.shape[0]} rows and {my_dataset.shape[1]} columns."
)


# In[5]:


# Copying the data to another variable to avoid any changes to the original data
data = my_dataset.copy()
data


# ## Checking the names of the columns in the data

# In[6]:


print(data.columns)


# In[7]:


# # function to plot a boxplot and a histogram along the same scale.


# def histogram_boxplot(data, feature, figsize=(12, 7), kde=False, bins=None):
#     """
#     Boxplot and histogram combined

#     data: dataframe
#     feature: dataframe column
#     figsize: size of figure (default (12,7))
#     kde: whether to the show density curve (default False)
#     bins: number of bins for histogram (default None)
#     """
#     f2, (ax_box2, ax_hist2) = plt.subplots(
#         nrows=2,  # Number of rows of the subplot grid= 2
#         sharex=True,  # x-axis will be shared among all subplots
#         gridspec_kw={"height_ratios": (0.25, 0.75)},
#         figsize=figsize,
#     )  # creating the 2 subplots
#     sns.boxplot(
#         data=data, x=feature, ax=ax_box2, showmeans=True, color="violet"
#     )  # boxplot will be created and a star will indicate the mean value of the column
#     sns.histplot(
#         data=data, x=feature, kde=kde, ax=ax_hist2, bins=bins, palette="winter"
#     ) if bins else sns.histplot(
#         data=data, x=feature, kde=kde, ax=ax_hist2
#     )  # For histogram
#     ax_hist2.axvline(
#         data[feature].mean(), color="green", linestyle="--"
#     )  # Add mean to the histogram
#     ax_hist2.axvline(
#         data[feature].median(), color="black", linestyle="-"
#     )  # Add median to the histogram


# In[8]:


# selecting numerical columns
# num_cols = data.select_dtypes(include=np.number).columns.tolist()

# for item in num_cols:
# histogram_boxplot(data, item, bins=50, kde=True, figsize=(10, 5))


# In[9]:


# function to create labeled barplots


def labeled_barplot(data, feature, perc=False, n=None):
    """
    Barplot with percentage at the top

    data: dataframe
    feature: dataframe column
    perc: whether to display percentages instead of count (default is False)
    n: displays the top n category levels (default is None, i.e., display all levels)
    """

    total = len(data[feature])  # length of the column
    count = data[feature].nunique()
    if n is None:
        plt.figure(figsize=(count + 1, 5))
    else:
        plt.figure(figsize=(n + 1, 5))

    plt.xticks(rotation=90, fontsize=15)
    ax = sns.countplot(
        data=data,
        x=feature,
        palette="Paired",
        order=data[feature].value_counts().index[:n].sort_values(),
    )

    for p in ax.patches:
        if perc == True:
            label = "{:.1f}%".format(
                100 * p.get_height() / total
            )  # percentage of each class of the category
        else:
            label = p.get_height()  # count of each level of the category

        x = p.get_x() + p.get_width() / 2  # width of the plot
        y = p.get_height()  # height of the plot

        ax.annotate(
            label,
            (x, y),
            ha="center",
            va="center",
            size=12,
            xytext=(0, 5),
            textcoords="offset points",
        )  # annotate the percentage

    plt.show()  # show the plot


# In[11]:


labeled_barplot(data, "CS_STATUS", perc=True)


# In[12]:


labeled_barplot(data, "CS_St_NAME_LANGUAGE", perc=True)


# In[13]:


labeled_barplot(data, "CS_TYPE", perc=True)


# In[15]:


labeled_barplot(data, "Bg_COORDINATE_TYPE", perc=True)


# In[16]:


labeled_barplot(data, "Bg_CIVIC_NUMBER_SUFFIX", perc=True)

