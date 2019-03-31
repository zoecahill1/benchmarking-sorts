from bubble import random_array
import csv 
import time

# Defines a function to write merge test results to csv file
def mergecsv():
    # Initialises empty list to store test results of different input sizes
    mergetest = []
    # Calls run_test function to generate a random list of 100 numbers and 
    # add the average of 10 runs to the selectiontest list
    mergetest.append(run_test_of_size_merge(100))
    mergetest.append(run_test_of_size_merge(250))
    mergetest.append(run_test_of_size_merge(500))
    mergetest.append(run_test_of_size_merge(750))
    mergetest.append(run_test_of_size_merge(1000))
    mergetest.append(run_test_of_size_merge(1250))
    mergetest.append(run_test_of_size_merge(2500))
    mergetest.append(run_test_of_size_merge(3750))
    mergetest.append(run_test_of_size_merge(5000))
    mergetest.append(run_test_of_size_merge(6250))
    mergetest.append(run_test_of_size_merge(7500))
    mergetest.append(run_test_of_size_merge(8750))
    mergetest.append(run_test_of_size_merge(10000))

    # Opens results.csv to write selection results
    with open ("res/results.csv", "a", newline = "") as csvFile:
        # Writer method for csvfile
        writer = csv.writer(csvFile)
        # Write results to row of csv file
        writer.writerow(mergetest)

    # Closes csv file when finished
    csvFile.close()

def run_test_of_size_merge(n):
    # Calls random_array which will generate list of random elements to be tested
    list = random_array(n)
    # Initialises results list to store run times
    results = []
    # This loop will run the sort 10 times
    for i in range (0,9):
        # The time() function will track the start time of the sort
        start_time = time.time()
        # Call to run bubbblesort list of random numbers
        mergeSort(list)
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

# Source code downloaded from:
# http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html
# Defines a finction called merge sort used for sorting lists
def mergeSort(alist):
    if len(alist)>1:
        # Find the middle of the list
        mid = len(alist)//2
        # Dividing the array elements
        lefthalf = alist[:mid]
        # There are 2 halves - right and left
        righthalf = alist[mid:]

        # Calls merge sort on the first half of the list
        mergeSort(lefthalf)
        # Calls merge sort on the second half of the list
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        # Copies the data into temp list lefthalf and righthalf
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        # Checking if any element was left
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        # Same on other list
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    # End the function and returns sorted list
    return alist
