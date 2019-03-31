from bubble import random_array
import csv 
import time

def selectioncsv():
    selectiontest = []
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


    with open ("res/results.csv", "a", newline = "") as csvFile:
        #writer=csv.DictWriter(
            #csvFile, fieldnames = ["Algorithim", "100", "250", "500", "750", "1000", "1250", "2500", "3750", "5000", "6250", "7500", "8750"])
        #writer.writeheader()

        writer = csv.writer(csvFile)
        writer.writerow(selectiontest)

    csvFile.close()

def selectionSort(alist):

   for i in range(len(alist)):

      # Find the minimum element in remaining
       minPosition = i

       for j in range(i+1, len(alist)):
           if alist[minPosition] > alist[j]:
               minPosition = j
                
       # Swap the found minimum element with minPosition       
       temp = alist[i]
       alist[i] = alist[minPosition]
       alist[minPosition] = temp

   return alist

def run_test_of_size_selection(n):
    #https://www.pythoncentral.io/selection-sort-implementation-guide/
    list = random_array(n)
    results = []
    for i in range (0,9):
        start_time = time.time()
        result = selectionSort(list)
        end_time = time.time()
        time_elapsed = end_time - start_time
        results.append(time_elapsed*10)
        i=i+1

    avg = (sum(results)/len(results))
    return "{:.3f}".format(avg)
        # time elapsed is in seconds