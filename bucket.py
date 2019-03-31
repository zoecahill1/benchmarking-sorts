from bubble import random_array
import csv 
import time
import math

# Defines a function to write quick test results to csv file
def bucketcsv():
    # Initialises empty list to store test results of different input sizes
    buckettest = []
    # Calls run_test function to generate a random list of 100 numbers and 
    # add the average of 10 runs to the buckettest list
    buckettest.append(run_test_of_size_bucket(100))
    buckettest.append(run_test_of_size_bucket(250))
    buckettest.append(run_test_of_size_bucket(500))
    buckettest.append(run_test_of_size_bucket(750))
    buckettest.append(run_test_of_size_bucket(1000))
    buckettest.append(run_test_of_size_bucket(1250))
    buckettest.append(run_test_of_size_bucket(2500))
    buckettest.append(run_test_of_size_bucket(3750))
    buckettest.append(run_test_of_size_bucket(5000))
    buckettest.append(run_test_of_size_bucket(6250))
    buckettest.append(run_test_of_size_bucket(7500))
    buckettest.append(run_test_of_size_bucket(8750))
    buckettest.append(run_test_of_size_bucket(10000))

    # Opens results.csv to write selection results
    with open ("res/results.csv", "a", newline = "") as csvFile:
        # Writer method for csvfile
        writer = csv.writer(csvFile)
        # Write results to row of csv file
        writer.writerow(buckettest)
    # Closes csv file when finished
    csvFile.close()

# Source code downloaded from:
# https://gist.github.com/joaofeitoza13/95bc455570ed5471830379c90a1349e7 
# Insertion sort function will be called to sort smaller 'buckets' of data
# as it is very fast on smaller input sizes
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
            
        alist[position]=currentvalue
    
    return alist     

# Determining the min and max values 
def hashing(array):
    m = array[0]
    for i in range(1, len(array)):
        if ( m < array[i] ):
            m = array[i]
    result = [m,int(math.sqrt( len(array)))]
    return result
 
def re_hashing(i, code ):
    return int(i/code[0]*(code[1]-1))

def bucketSort(array):
    code = hashing(array)
    # Initialize buckets
    buckets = [list() for _ in range( code[1] )]
    for i in array:
        x = re_hashing( i, code )
        buck = buckets[x]
        buck.append( i )
    # Distribute input list values into buckets
    for bucket in buckets:
        # Calls insertion sort on smaller lists
        insertionSort(bucket)      
    ndx = 0
    # Sort buckets and place back into input list
    for b in range( len( buckets ) ):
        for v in buckets[b]:
            array[ndx] = v
            ndx += 1
    # Ends program and returns sorted list
    return array


def run_test_of_size_bucket(n):
    # Calls random_array which will generate list of random elements to be tested
    list = random_array(n)
    # Initialises results list to store run times
    results = []
    # This loop will run the sort 10 times
    for i in range (0,9):
        # The time() function will track the start time of the sort
        start_time = time.time()
        # Call to run bubbblesort list of random numbers
        bucketSort(list)
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