def insertionSort(input_list):
    # Listenin ikinci elemanından (indis 1) başlarız çünkü
    # ilk elemanın (indis 0) zaten kendi içinde sıralı olduğunu varsayarız.
    for i in range(1, len(input_list)):
        key = input_list[i]  # Sıralanacak olan mevcut eleman
        j = i - 1

        # Key'den büyük olan elemanları bir sağa kaydırarak
        # key için doğru boşluğu açıyoruz.
        while j >= 0 and input_list[j] > key:
            input_list[j + 1] = input_list[j]
            j -= 1

        # Doğru boşluk bulunduğunda elemanı yerleştiriyoruz.
        input_list[j + 1] = key

    return input_list


# Uygulama:
L = [4, 3, 2, 1, 6]
print(f"Sırasız Liste: {L}")
sorted_L = insertionSort(L)
print(f"Sıralı Liste: {sorted_L}")