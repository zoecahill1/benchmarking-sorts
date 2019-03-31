from random import randint
import time
import csv

def bubblecsv():
    firstline = [100, 250, 500, 750, 1000, 1250, 2500, 3750, 5000, 6250, 7500, 8750, 10000]
    bubbletest = []
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


    with open ("res/results.csv", "a", newline = "") as csvFile:
        csvFile.truncate()
        #writer=csv.DictWriter(
            #csvFile, fieldnames = ["Algorithim", "100", "250", "500", "750", "1000", "1250", "2500", "3750", "5000", "6250", "7500", "8750"])
        #writer.writeheader()

        writer = csv.writer(csvFile)
        writer.writerow(firstline)
        writer.writerow(bubbletest)

    csvFile.close()

def run_test_of_size_bubble(n):
    list = random_array(n)
    results = []
    for i in range (0,9):
        start_time = time.time()
        result = bubbleSort(list)
        end_time = time.time()
        time_elapsed = end_time - start_time
        results.append(time_elapsed*10)
        i=i+1

    avg = (sum(results)/len(results))
    return "{:.3f}".format(avg)
        # time elapsed is in seconds


# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist

def random_array(n):
    array = []
    for i in range(0,n,1):
        array.append(randint(0,100))
    return array