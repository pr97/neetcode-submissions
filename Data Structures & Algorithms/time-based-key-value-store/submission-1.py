def binary_search(arr, val):
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        # print(arr)
        # print(val)
        # print(type(val))
        # print(type(arr[0][0]), type(arr[0][1]))
        # print(mid)
        # print(arr[mid])
        if arr[mid][1] < val:
            if (mid + 1 <= r and arr[mid + 1][1] > val) or (mid == r and arr[mid][1] <= val):
                return mid
            l = mid + 1
        elif arr[mid][1] > val:
            if (mid - 1 >= l and arr[mid - 1][1] < val) or (mid == l) and arr[mid][1] <= val:
                return mid - 1
            r = mid - 1
        else:
            return mid
    return -1

class TimeMap:
    def __init__(self):
        self.m = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = [(value, timestamp)]
        else:
            self.m[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""
        idx = binary_search(self.m[key], timestamp)
        if idx != -1:
            return self.m[key][idx][0]
        else:
            return ""

        
