class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        def binarySearch(A, start, end, target):
            while (start <= end):
                mid = (start+end)/2
                if A[mid] == target:
                    return mid
                elif A[mid] > target:
                    end = mid-1
                elif A[mid] < target:
                    start = mid+1
            return -1

        mid = binarySearch(A, 0, len(A)-1, target)
        result = [mid, mid]

        end1 = mid-1
        mid1 = -1
        while True:
            mid1 = binarySearch(A, 0, end1, target)
            if (mid1 == -1):
                break
            result[0] = mid1
            end1 = mid1-1

        start1 = mid+1
        mid2 = -1
        while True:
            mid2 = binarySearch(A, start1, len(A)-1, target)
            if mid2 == -1:
                break
            result[1] = mid2
            start1 = mid2+1

        return result
