# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

#User function Template for python3

class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)-1):
            mini = i
            for j in range(i+1 , len(arr)):
                if arr[j] < arr[mini]:
                    mini = j
            arr[mini],arr[i] = arr[i],arr[mini]
        return arr
        
        
