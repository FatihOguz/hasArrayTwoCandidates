
def merge(arr, l, m, r): 
	n1 = m - l + 1
	n2 = r- m 

	# create temp arrays 
	L = [0] * (n1) 
	R = [0] * (n2) 

	# Copy data to temp arrays L[] and R[] 
	for i in range(0 , n1): 
		L[i] = arr[l + i] 

	for j in range(0 , n2): 
		R[j] = arr[m + 1 + j] 

	# Merge the temp arrays back into arr[l..r] 
	i = 0	 # Initial index of first subarray 
	j = 0	 # Initial index of second subarray 
	k = l	 # Initial index of merged subarray 

	while i < n1 and j < n2 : 
		if L[i] <= R[j]: 
			arr[k] = L[i] 
			i += 1
		else: 
			arr[k] = R[j] 
			j += 1
		k += 1

	 
	while i < n1: 
		arr[k] = L[i] 
		i += 1
		k += 1

	
	while j < n2: 
		arr[k] = R[j] 
		j += 1
		k += 1


def mergeSort(arr,left,right): 
	if left < right: 

		
		m = (left+(right-1))//2

		mergeSort(arr, left, m) 
		mergeSort(arr, m+1, right) 
		merge(arr, left, m, right) 

def hasArrayTwoCandidates(arr, arr_size, multiply):
     
    #merge sort the array (this O(n*logn) complexity)
    mergeSort(arr, 0, arr_size-1)
    left = 0
    right = arr_size-1
     
    
    while left<right:
        if (arr[left] * arr[right] > multiply):
            right-=1
        elif (arr[left] * arr[right] < multiply):
            left += 1
        else:
            print(str(arr[left]) + " " + str(arr[right]))
            left+=1	
            right-=1
    return 0
 

     





 
arr = [1,2,42,2,15,3,6,5,6 , 7,21,14]
multiply = 42
hasArrayTwoCandidates(arr, len(arr), multiply)
 