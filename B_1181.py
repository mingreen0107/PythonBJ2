#  N개의 단어 받고 길이가 짧은 순 -> 같으면 사전 순으로 정렬

n = int(input())

words = [str(input()) for i in range(n)]

words = list(set(words))
words.sort()
words.sort(key=len)

for i in words:
    print(i)

'''
버블정렬은 배웠지만 시간 초과 문제를 해결하지 못 함

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

N = int(input())
list = []
result = []

for i in range(N):
    a = input()
    list.append(a)

listSet = set(list)
listSet = sorted(listSet)
bubble_sort(listSet)
N = len(listSet)

for j in listSet:
    result.append(j)

for k in range(N):
    print(result[k])
'''