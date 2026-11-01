class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        u = 0
        d = m - 1
        while d - u >= 0:
            mid = (u + d) // 2
            search_row = mid
            # print(mid, u, d)
            if d == u:
                break
            if matrix[mid][-1] < target:
                u = mid + 1
            elif matrix[mid][0] > target:
                d = mid - 1
            else:
                search_row = mid
                break

        l = 0
        r = n - 1
        while r - l >= 0:
            mid = (l + r) // 2
            if matrix[search_row][mid] < target:
                l = mid + 1
            elif matrix[search_row][mid] > target:
                r = mid - 1
            else:
                return True
        
        return False
        