import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import bubble

import bucket
import merge
import quick
import selection

def genCsv():
    
    bubble.bubblecsv()
    selection.selectioncsv()
    bucket.bucketcsv()
    merge.mergecsv()
    quick.quickcsv()


def genPlot():
    #pd.read_csv('results.csv', header=None).T.to_csv('output.csv', header=False, index=False)
    
    df = pd.read_csv("output.csv")
    print(df.head())
    

    #https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
    x=df.iloc[:,0]
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

    plt.show()