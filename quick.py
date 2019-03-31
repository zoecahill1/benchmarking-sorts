from bubble import random_array
import csv 
import time

# Defines a function to write quick test results to csv file
def quickcsv():
    # Initialises empty list to store test results of different input sizes
    quicktest = []
    # Calls run_test function to generate a random list of 100 numbers and 
    # add the average of 10 runs to the quicktest list
    quicktest.append(run_test_of_size_quick(100))
    quicktest.append(run_test_of_size_quick(250))
    quicktest.append(run_test_of_size_quick(500))
    quicktest.append(run_test_of_size_quick(750))
    quicktest.append(run_test_of_size_quick(1000))
    quicktest.append(run_test_of_size_quick(1250))
    quicktest.append(run_test_of_size_quick(2500))
    quicktest.append(run_test_of_size_quick(3750))
    quicktest.append(run_test_of_size_quick(5000))
    quicktest.append(run_test_of_size_quick(6250))
    quicktest.append(run_test_of_size_quick(7500))
    quicktest.append(run_test_of_size_quick(8750))
    quicktest.append(run_test_of_size_quick(10000))


    # Opens results.csv to write selection results
    with open ("res/results.csv", "a", newline = "") as csvFile:
        # Writer method for csvfile
        writer = csv.writer(csvFile)
        # Write results to row of csv file
        writer.writerow(quicktest)

    # Closes csv file when finished
    csvFile.close()

# Source code downloaded from:
# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheQuickSort.html
# Defines a finction called quick sort used for sorting lists
# Quick sort takes last element as pivot, places
# the pivot element at its correct position in the sorted list
# then places all elements smaller than the pivot to the left of the pivot
# and all that are greater to the right
def quickSort(alist):

   quickSortHelper(alist,0,len(alist)-1)
   return alist

# alist - list to be sorted
# first - starting index
# last - ending index
def quickSortHelper(alist,first,last):
   if first<last:

        # splitpoint is partitioning index meaning alist[splitpoint]
        # is now sorted
       splitpoint = partition(alist,first,last)

        # Sort elements before partition
       quickSortHelper(alist,first,splitpoint-1)
       # Sort elements after partition
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   # pivot
   pivotvalue = alist[first]
    # index of bigger element
   leftmark = first+1
   rightmark = last

   done = False
   while not done:
       # when current element is smaller than or equal to pivot
       # increment index of smaller element
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
        # when current element is greater than or equal to pivot
        # decrement index of bigger element
       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   return rightmark


def run_test_of_size_quick(n):
    # Calls random_array which will generate list of random elements to be tested
    list = random_array(n)
    # Initialises results list to store run times
    results = []
    # This loop will run the sort 10 times
    for i in range (0,9):
        # The time() function will track the start time of the sort
        start_time = time.time()
        # Call to run bubbblesort list of random numbers
        result = quickSort(list)
        # Tracks when the sort finishes
        end_time = time.time()
        # To get the run time we subtract the 2 numbers
        time_elapsed = end_time - start_time
        # Store the answer to the results list. Multiply *10 to get results in miliseconds
        results.append(time_elapsed*10)
        # Counter - for loop
        i=i+1

    # Get the average by adding all results in the list together and 
    # dividing by the number of elements in the list
    avg = (sum(results)/len(results))
    # End the program and returns the average formatted to 3 decimals
    return "{:.3f}".format(avg)