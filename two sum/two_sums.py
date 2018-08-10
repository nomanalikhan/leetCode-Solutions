def twoSum(arr, target):
    for i, n in enumerate(arr):
        pair = target - n
        if pair in arr[i + 1:]:
            return [i, arr.index(pair, i + 1)]


inpArr = [2, 7, 11, 15]
inpNum = 9

print(twoSum(inpArr, inpNum))
