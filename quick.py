from bubble import random_array
import csv 
import time

def quickcsv():
    quicktest = []
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


    with open ("res/results.csv", "a", newline = "") as csvFile:
        #writer=csv.DictWriter(
            #csvFile, fieldnames = ["Algorithim", "100", "250", "500", "750", "1000", "1250", "2500", "3750", "5000", "6250", "7500", "8750"])
        #writer.writeheader()

        writer = csv.writer(csvFile)
        writer.writerow(quicktest)

    csvFile.close()

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)
   return alist

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

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
    list = random_array(n)
    results = []
    for i in range (0,9):
        start_time = time.time()
        result = quickSort(list)
        end_time = time.time()
        time_elapsed = end_time - start_time
        results.append(time_elapsed*10)
        i=i+1

    avg = (sum(results)/len(results))
    return "{:.3f}".format(avg)
        # time elapsed is in seconds
