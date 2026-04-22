def BubbleSort(L):
    n = len(L)
    for i in range(n):
        for j in range(0, n - i - 1):  # Komşu elemanlar: j ve j+1
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L

print(BubbleSort([4, 2, 3, 1, 8, 90]))
# Çıktı: [1, 2, 3, 4, 8, 90]