n = int(input("Введите количество элементов в массиве А : ")))
Ai = input("Введите элементы массива: ").split()
A = list(map(int, Ai))
X = int(input("Введите число X : "))
    min = (X - A[0])
    index = 0
    for i in range(1, n):
        count = (X - A[i])
        if count < min:
            min = count
            index = i
    print(f"Ближайшим по величине к числу {X} является число: {A[index]} ")
