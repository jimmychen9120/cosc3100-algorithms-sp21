array=[4,-20,12,5,4,-10,2,5,-5,3,2,1,1,-10,-4,5]


def calcSubArray(arr, first, last):
	firstNegInd=0
	secNegInd=0

	negCount=0
	begSum=0
	for i in range(first, last+1):
		if arr[i]<0:
			if negCount==0:
				firstNegInd=i
			negCount+=1
			if arr[i+1]<0:
				if begSum==0:
					continue;
				else:
					break;
			if negCount>1:
				secNegInd=i
				if begSum==0:
					continue;
				else:
					break;
		begSum=begSum+arr[i]
	#print(begSum)

	negCount=0
	endSum=0
	for i in range(last, first-1, -1):
		if arr[i]<0:
			negCount+=1
			if arr[i-1]<0:
				if begSum==0:
					continue;
				else:
					break;
			if negCount>1:
				if begSum==0:
					continue;
				else:
					break;
		endSum=endSum+arr[i]
	#print(endSum)

	negCount=0
	midSum=0
	for i in range(firstNegInd+1, secNegInd):
		midSum=midSum+arr[i]
	#print(midSum)

	maxSum=max(begSum, endSum, midSum)
	#print(maxSum)
	if first==0:
		return maxSum, endSum
	else:
		return maxSum, begSum


def subarrayDivide(arr, first, last):
	if(first==last):
		return arr[first]
	else:
		mid=(first+last)//2
		leftMax, leftEnd=calcSubArray(arr, first, mid)
		rightMax, rightBeg=calcSubArray(arr, mid+1, last)

		combSum=leftEnd+rightBeg

		return max(leftMax, rightMax, combSum)

print(subarrayDivide(array, 0, len(array)-1))