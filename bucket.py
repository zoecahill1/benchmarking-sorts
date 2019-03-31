from bubble import random_array
import csv 
import time
import math


def bucketcsv():
    buckettest = []
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


    with open ("res/results.csv", "a", newline = "") as csvFile:
        #writer=csv.DictWriter(
            #csvFile, fieldnames = ["Algorithim", "100", "250", "500", "750", "1000", "1250", "2500", "3750", "5000", "6250", "7500", "8750"])
        #writer.writeheader()

        writer = csv.writer(csvFile)
        writer.writerow(buckettest)

    csvFile.close()

def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index
        
        while position>0 and alist[position-1]>currentvalue:
            alist[position]=alist[position-1]
            position = position-1
            
        alist[position]=currentvalue
    
    return alist     
              
def hashing(array):
    m = array[0]
    for i in range(1, len(array)):
        if ( m < array[i] ):
            m = array[i]
    result = [m,int(math.sqrt( len(array)))]
    return result
 
def re_hashing(i, code ):
    return int(i/code[0]*(code[1]-1))
 #https://gist.github.com/joaofeitoza13/95bc455570ed5471830379c90a1349e7
def bucketSort(array):
    code = hashing(array)
    buckets = [list() for _ in range( code[1] )]
    for i in array:
        x = re_hashing( i, code )
        buck = buckets[x]
        buck.append( i )
    for bucket in buckets:
        insertionSort(bucket)
         
    ndx = 0
    for b in range( len( buckets ) ):
        for v in buckets[b]:
            array[ndx] = v
            ndx += 1
    return array


def run_test_of_size_bucket(n):
    list = random_array(n)
    results = []
    for i in range (0,9):
        start_time = time.time()
        result = bucketSort(list)
        end_time = time.time()
        time_elapsed = end_time - start_time
        results.append(time_elapsed*10)
        i=i+1

    avg = (sum(results)/len(results))
    return "{:.3f}".format(avg)
        # time elapsed is in seconds

