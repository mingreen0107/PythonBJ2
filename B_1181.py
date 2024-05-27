#  N개의 단어 받고 길이가 짧은 순 -> 같으면 사전 순으로 정렬

n = int(input())

words = [str(input()) for i in range(n)]

words = list(set(words))
words.sort()
words.sort(key=len)

for i in words:
    print(i)