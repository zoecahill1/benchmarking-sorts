import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import bubble

import bucket
import merge
import quick
import selection

# This function will generate a CSV file to store the results of
# the tests being run
def genCsv():
    
    bubble.bubblecsv()
    selection.selectioncsv()
    bucket.bucketcsv()
    merge.mergecsv()
    quick.quickcsv()

# Defines a function to graph results from csv file
def genPlot():
    # Transposes date as easier to graph
    # pd.read_csv('res/results.csv', header=None).T.to_csv('res/output.csv', header=False, index=False)
    
    # Reads transposed csv file to dataframe
    df = pd.read_csv("res/output.csv")

    # Refrenced this site for iloc tutorial
    # https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/

    # Setting x axis as 1st column in df
    x=df.iloc[:,0]
    # Setting y axis as 2 column in df
    bu=df.iloc[:,1]
    plt.plot(x, bu, "ro-", label = "Bubble")
    select=df.iloc[:,2]
    plt.plot(x,select,"bo-", label = "Select")
    bucket=df.iloc[:,3]
    plt.plot(x,bucket,"yo-", label = "Bucket")
    merge=df.iloc[:,4]
    plt.plot(x,merge,"go-", label = "Merge")
    quick=df.iloc[:,5]
    plt.plot(x, quick,"mo-", label = "Quick")

    plt.title('Benchmarking Sorting Algorithims') 
    plt.legend(loc='outside')
    plt.xlabel('Input Size (n)') 
    plt.ylabel('Running time (milliseconds)') 
    # Setting y axis limit to 50
    plt.ylim(0, 50)

    #plt.savefig("res/graph.png")
    plt.show()

# Defines a function to generate formatted output of csv file
def genTable():
    # Extending width of output to handle extra rows
    pd.set_option('display.width', 1000)
    # Read data from csv file
    df = pd.read_csv("res/results.csv")
    # Naming rows by index
    df.rename(index={0:"Size",1:"Bubble Sort",2:"Selection Sort",3:"Bucket Sort", 4:"Merge Sort", 5:"Quick Sort"}, inplace=True)
    # Outputs dataframe to console
    print(df)