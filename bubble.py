from random import randint
import time
import csv

# Defines a function to write bubble test results to csv file
def bubblecsv():
    # Stores the input size to be tested and will be first line of csv file
    firstline = [100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000]
    # Initialises empty list to store test results of different input sizes
    bubbletest = []
    # Calls run_test function to generate a random list of 100 numbers and 
    # add the average of 10 runs to the bubbletest list
    bubbletest.append(run_test_of_size_bubble(100))
    bubbletest.append(run_test_of_size_bubble(250))
    bubbletest.append(run_test_of_size_bubble(500))
    bubbletest.append(run_test_of_size_bubble(750))
    bubbletest.append(run_test_of_size_bubble(1000))
    bubbletest.append(run_test_of_size_bubble(1250))
    bubbletest.append(run_test_of_size_bubble(2500))
    bubbletest.append(run_test_of_size_bubble(3750))
    bubbletest.append(run_test_of_size_bubble(5000))
    bubbletest.append(run_test_of_size_bubble(6250))
    bubbletest.append(run_test_of_size_bubble(7500))
    bubbletest.append(run_test_of_size_bubble(8750))
    bubbletest.append(run_test_of_size_bubble(10000))

    # Opens results.csv to write bubbletest results
    with open ("res/results.csv", "a", newline = "") as csvFile:
        # Deletes any previous entries in file as bubbletest is the first test to be run
        csvFile.truncate()
        # Writer method for csvfile
        writer = csv.writer(csvFile)
        # Writes 2 rows of results to csv file
        writer.writerow(firstline)
        writer.writerow(bubbletest)

    # Closes csv file when finished
    csvFile.close()

def run_test_of_size_bubble(n):
    # Calls random_array which will generate list of random elements to be tested
    list = random_array(n)
    # Initialises results list to store run times
    results = []
    # This loop will run the sort 10 times
    for i in range (0,9):
        # The time() function will track the start time of the sort
        start_time = time.time()
        # Call to run bubbblesort list of random numbers
        bubbleSort(list)
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
# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
# Defines a finction called bubble sort used for sorting lists
def bubbleSort(alist):
    # This will travese through the whole list
    for passnum in range(len(alist)-1,0,-1):
      for i in range(passnum):
            # Last i elements are already in place
            if alist[i]>alist[i+1]:
                # Compares the adjacent elements
                # Swap if the element found is greater 
                # than the next element
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    # Finishes function and returns sorted array
    return alist



# Defines a function which will generate a given number
# of elements in a list
def random_array(n):
    # Initialising an empty list for values to be stored in
    array = []
    # Loops through each element ending on n
    for i in range(0,n,1):
        # For each iterations through the loop add a random number
        # to the list
        array.append(randint(0,100))
    # Finishes function and returns generated list
    return array