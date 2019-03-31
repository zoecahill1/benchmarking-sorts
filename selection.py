from bubble import random_array
import csv 
import time

# Defines a function to write selection test results to csv file
def selectioncsv():
    # Initialises empty list to store test results of different input sizes
    selectiontest = []
    # Calls run_test function to generate a random list of 100 numbers and 
    # add the average of 10 runs to the selectiontest list
    selectiontest.append(run_test_of_size_selection(100))
    selectiontest.append(run_test_of_size_selection(250))
    selectiontest.append(run_test_of_size_selection(500))
    selectiontest.append(run_test_of_size_selection(750))
    selectiontest.append(run_test_of_size_selection(1000))
    selectiontest.append(run_test_of_size_selection(1250))
    selectiontest.append(run_test_of_size_selection(2500))
    selectiontest.append(run_test_of_size_selection(3750))
    selectiontest.append(run_test_of_size_selection(5000))
    selectiontest.append(run_test_of_size_selection(6250))
    selectiontest.append(run_test_of_size_selection(7500))
    selectiontest.append(run_test_of_size_selection(8750))
    selectiontest.append(run_test_of_size_selection(10000))

    # Opens results.csv to write selection results
    with open ("res/results.csv", "a", newline = "") as csvFile:

        # Writer method for csvfile
        writer = csv.writer(csvFile)
        # Write results to row of csv file
        writer.writerow(selectiontest)

    # Closes csv file when finished
    csvFile.close()

# Source code downloaded from:
# #https://www.pythoncentral.io/selection-sort-implementation-guide/
# Defines a finction called selection sort used for sorting lists
def selectionSort(alist):

    # Iterates through list
   for i in range(len(alist)):

      # Find the minimum element in remaining
       minPosition = i

        # Checks the min element with the current element
       for j in range(i+1, len(alist)):
           if alist[minPosition] > alist[j]:
               minPosition = j
                
       # Swap the found minimum element with minPosition       
       temp = alist[i]
       alist[i] = alist[minPosition]
       alist[minPosition] = temp

    # Ends function and returns sorted list
   return alist

def run_test_of_size_selection(n):
    # Calls random_array which will generate list of random elements to be tested
    list = random_array(n)
    # Initialises results list to store run times
    results = []
    # This loop will run the sort 10 times
    for i in range (0,9):
        # The time() function will track the start time of the sort
        start_time = time.time()
        # Call to run bubbblesort list of random numbers
        result = selectionSort(list)
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