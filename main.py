import numpy as np # Сначала убедитесь, что python устанавливает пакет numpy

def gauss(a, b):      # Определите функцию самостоятельно, независимые переменные - a, b
    m, n = a.shape    # Количество строк и столбцов матрицы a
    l = np.zeros((n,n))
    for temp in range(n):
        for k in range(n - 1):          # k представляет первый слой цикла,(0，n-1)Строка
            for i in range(k + 1, n):      # i означает цикл второго слоя,(k+1,n)Строка,Рассчитать коэффициент исключения строки
                l[i][k] = a[i][k] / a[k][k]          #Calculationl
                for j in range(m):            # j представляет столбец, выполнять операции с каждым столбцом
                    a[i][j] = a[i][j] - l[i][k] * a[k][j]
                b[i] = b[i] - l[i][k] * b[k]
        x = np.zeros(n)                                              # Сначала установите значение отмены назначения равным нулю, а затем вычислите одно за другим
        x[n - 1] = b[n - 1] / a[n - 1][n - 1]  # Сначала вычислить последнее x решение
    for i in range(n - 2, -1, -1):            # Вернуть и пересчитать каждое решение по очереди
        for j in range(i + 1, n):
            b[i] -= a[i][j] * x[j]              # Поскольку увеличение и уменьшение
            x[i] = b[i] / a[i][i]
    for i in range(n):
        print("x" + str(i + 1) + " = ", x[i])

if __name__ == '__main__':
    a = np.array([[26, 7.5, 2.8, 1.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [7.5, 26, 7.5, 2.8, 1.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [2.8, 7.5, 26, 7.5, 2.8, 1.4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1.4, 2.8, 7.5, 26, 7.5, 2.8, 1.4, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1.4, 2.8, 7.5, 26, 7.5, 2.8, 1.4, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1.4, 2.8, 7.5, 26, 7.5, 2.8, 1.4, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1.4, 2.8, 7.5, 26, 7.5, 2.8, 1.4, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 1.4, 2.8, 7.5, 26, 7.5, 2.8, 1.4, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1.4, 2.8, 7.5, 26, 7.5, 2.8, 1.4, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 1.4, 2.8, 7.5, 26, 7.5, 2.8, 1.4, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1.4, 2.8, 7.5, 26, 7.5, 2.8, 1.4, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1.4, 2.8, 7.5, 26, 7.5, 2.8, 1.4],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1.4, 2.8, 7.5, 26, 7.5, 2.8],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.4, 2.8, 7.5, 26, 7.5],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1.4, 2.8, 7.5, 26]])

    b = np.array([-36, -179.3, 23.8, -77.7, 29.3, 154.7, -126.2, -155.5, 32.5, 35.5, 253.1, 175.6, 138, 25.4, 136.9])
    gauss(a, b)
    invers = np.linalg.inv(a)
    for i in invers:
        for element in i:
            print(element, end='  ')
        print()
    print()

    detA = np.linalg.det(a)
    detInvers = np.linalg.det(invers)
    print("detA = ", detA)
    print("detInvers = ", detInvers)
    print("detA * detInvers = ", detA * detInvers)
    print()
    newMatrix = a.dot(invers)
    for i in newMatrix:
        for element in i:
            print(element, end='  ')
        print()
    print()



