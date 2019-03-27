from sys import argv

def binsearch(arr, elem, start=0, end=None):
    if end is None:
        end = len(arr) - 1
    if start > end:
        return "not found"

    mid = (start + end) // 2
    if elem == arr[mid]:
        return mid
    if elem < arr[mid]:
        return binsearch(arr, elem, start, mid-1)
    return binsearch(arr, elem, mid+1, end)

sortedarr = [30, 40, 50, 52, 56, 62, 70, 91, 100, 131, 132, 166, 170, 195,
             202, 205, 212, 248, 249, 256, 263, 272, 288, 289, 290, 296, 
             332, 345, 352, 364, 380, 390, 407, 412, 429, 430, 438, 444,
             486, 493, 497, 499, 510, 513, 514, 519, 521, 521, 535, 546,
             552, 554, 556, 570, 584, 638, 640, 655, 655, 657, 692, 692,
             711, 713, 731, 739, 740, 842, 858, 885, 887, 888, 893, 898,
             900, 903, 908, 909, 959, 988]

n = int(argv[1])

res = binsearch(sortedarr,n)
if res != "not found":
    print "found at" , res
else: print res