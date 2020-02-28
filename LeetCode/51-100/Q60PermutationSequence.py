class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = ""
        num_1 = 1
        index_1 = 1
        while index_1 <= n:
            num_1 *= index_1
            if num_1 >= k:
                break
            index_1 += 1
        for i in range(1, n - index_1 + 1):
            result += str(i)
        num_left = list(range(n - index_1 + 1, n + 1))
        k -= 1
        while num_left:
            num_1 //= index_1
            index_1 -= 1
            index_num_left = k // num_1
            result += str(num_left[index_num_left])
            num_left.pop(index_num_left)
            k %= num_1
        return result


def main():
    print(Solution().getPermutation(4, 5))

if __name__ == '__main__':
    main()
