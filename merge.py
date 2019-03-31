from bubble import random_array
import csv 
import time

def mergecsv():
    mergetest = []
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


    with open ("results.csv", "a", newline = "") as csvFile:
        #writer=csv.DictWriter(
            #csvFile, fieldnames = ["Algorithim", "100", "250", "500", "750", "1000", "1250", "2500", "3750", "5000", "6250", "7500", "8750"])
        #writer.writeheader()

        writer = csv.writer(csvFile)
        writer.writerow(mergetest)

    csvFile.close()

def run_test_of_size_merge(n):
    list = random_array(n)
    results = []
    for i in range (0,9):
        start_time = time.time()
        result = mergeSort(list)
        end_time = time.time()
        time_elapsed = end_time - start_time
        results.append(time_elapsed*10)
        i=i+1

    avg = (sum(results)/len(results))
    return "{:.3f}".format(avg)
        # time elapsed is in seconds

#http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html
def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    return alist
