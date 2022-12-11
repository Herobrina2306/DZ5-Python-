# 5* Дан список чисел. Найдите все возрастающие последовательности. Порядок элементов менять нельзя.

# *Пример:* 

# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

array = [1, 5, 2, 3, 4, 6, 1, 7]

for l in range(len(array)):  
    for i in range(len(array)):
        arr_n = [1]
        arr_n[0] = array[l]
        for j in range(i, len(array)):
            if array[j] > arr_n[-1]:
                arr_n.append(array[j])

        print(arr_n)