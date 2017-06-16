import csv
import pandas as pd
import sys
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split



def getRed():
    return pd.read_csv('winequality-red.csv',sep=';')

def getWhite():
    return pd.read_csv('winequality-white.csv',sep=';')

def getRedWine():
    # Read in red wine data
    f = open('winequality-red.csv', 'rt')
    red = pd.read_csv('winequality-red.csv',sep=';')
    print red.info()
    try:
        reader = csv.reader(f)
        for row in reader:
            print row
    finally:
        f.close()

def plot_corelation():
    red = getRed()
    red['type'] = 1
    white = getWhite()
    white['type'] = 0
    wines = red.append(white,ignore_index=True)
    X = wines.ix[:,0:11]

    y = np.ravel(wines.type)

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.33, random_state=42)




def plot_alcohol():
    fig, ax = plt.subplots(1, 2)
    red = pd.read_csv('winequality-red.csv',sep=';')
    white = pd.read_csv('winequality-white.csv',sep=';')
    ax[0].hist(red.alcohol, 10, facecolor='red', alpha=0.5, label="Red wine")
    ax[1].hist(white.alcohol, 10, facecolor='white', ec="black", lw=0.5, alpha=0.5, label="White wine")
    fig.subplots_adjust(left=0, right=1, bottom=0, top=0.5, hspace=0.05, wspace=1)
    ax[0].set_ylim([0, 1000])
    ax[0].set_xlabel("Alcohol in % Vol")
    ax[0].set_ylabel("Frequency")
    ax[1].set_xlabel("Alcohol in % Vol")
    ax[1].set_ylabel("Frequency")
    # ax[0].legend(loc='best')
    # ax[1].legend(loc='best')
    fig.suptitle("Distribution of Alcohol in % Vol")
    plt.show()

def plot_sulphates():
    fig,ax = plt.subplots(1,2,figsize=(8, 4))

    red =getRed()
    white = getWhite()

    ax[0].scatter(red['quality'], red["sulphates"], color="red")
    ax[1].scatter(white['quality'], white['sulphates'], color="white", edgecolors="black", lw=0.5)

    ax[0].set_title("Red Wine")
    ax[1].set_title("White Wine")
    ax[0].set_xlabel("Quality")
    ax[1].set_xlabel("Quality")
    ax[0].set_ylabel("Sulphates")
    ax[1].set_ylabel("Sulphates")
    ax[0].set_xlim([0, 10])
    ax[1].set_xlim([0, 10])
    ax[0].set_ylim([0, 2.5])
    ax[1].set_ylim([0, 2.5])
    fig.subplots_adjust(wspace=0.5)
    fig.suptitle("Wine Quality by Amount of Sulphates")

    plt.show()

def plot_numpy():

    red = pd.read_csv('',sep=';')
    white = pd.read_csv('', sep=';')

    print(np.histogram(red.alcohol, bins=[7, 8, 9, 10, 11, 12, 13, 14, 15]))
    print(np.histogram(white.alcohol, bins=[7, 8, 9, 10, 11, 12, 13, 14, 15]))


def getWhiteeWine():
    # Read in white wine data
    f = open('winequality-white.csv', 'rt')
    white = pd.read_csv('winequality-white.csv',sep=';')
    try:
        reader = csv.reader(f)
        for row in reader:
            print row
    finally:
        f.close()

if __name__ == '__main__':
    # plot_alcohol()
    # plot_sulphates()
    plot_corelation()