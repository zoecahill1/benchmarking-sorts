![Python Banner](/res/python-banner.jpg)
# Benchmarking Sorting Algorithims

This repository contains my solutions to the Project for the module Computational Thinking with Algorithims at GMIT. 
<p>For this project we will be writing a Python application which will be used to benchmark 5 different sorting algorithims. The 5 sorting algorithims we will look at are as follows: </p>

1. Bubble Sort
2. Selection Sort
3. Merge Sort
4. Quick Sort
5. Bucket Sort

## How to download this repository

1. On GitHub, navigate to the main page of the repository.
2. Under the repository name, click Clone or download.
3. In the Clone with HTTPs section, click to copy the clone URL for the repository.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type git clone, and then paste the URL you copied in Step 2.
7. Press Enter. Your local clone will be created.

## How to run the code

1. Make sure you have python v. 3.7 installed. This can be downloaded here from the [anaconda website](https://www.anaconda.com/distribution/).
2. Run command line.
3. Navigate to where you have the files saved in your directory.
4. Type python followed by start.py to run the program. All files and their functions are listed below.

## Libraries Used 
1. [Pandas](https://pandas.pydata.org/) -  an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools.
2. [Matplotlib](https://matplotlib.org/) - is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms.
3. [numpy](https://www.numpy.org/) - NumPy is the fundamental package for scientific computing with Python. It contains among other things; a powerful N-dimensional array object, sophisticated (broadcasting) functions, tools for integrating C/C++ and Fortran code, useful linear algebra, Fourier transform, and random number capabilities.

## What each file contains

1. start.py - contains the main method for this program and is where all functions within this application are called from.
2. bubble.py - contains the bubble sort code itself, along with the code for testing various array sizes and the writing results to a CSV file. Also contains the code for generating the random arrays used in other files.
3. bucket.py - contains the bucket sort code itself, along with the code for testing various array sizes and the writing results to a CSV file.
4. merge.py - contains the merge sort code itself, along with the code for testing various array sizes and the writing results to a CSV file.
5. quick.py - contains the quick sort code itself, along with the code for testing various array sizes and the writing results to a CSV file.
6. selection.py - contains the selection sort code itself, along with the code for testing various array sizes and the writing results to a CSV file.
7. analysis.py - generates the tables and graphs from CSV file which we will use for analysis.
8. res - contains resources such as images, graphs and tables used in this project.


## References

1. [Bubble Sort Source Code](http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html)
2. [Selection Sort Source Code](https://www.pythoncentral.io/selection-sort-implementation-guide/)
3. [Merge Sort Source Code](http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html)
4. [Quick Sort Source Code](http://interactivepython.org/courselib/static/pythonds/SortSearch/TheQuickSort.html)
5. [Bucket Sort Source Code](https://gist.github.com/joaofeitoza13/95bc455570ed5471830379c90a1349e7)
6. [Iloc tutorial used in analysis.py](https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/)