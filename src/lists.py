def main():
    my_list = [1, 2, 3]
    print(my_list)
    my_list = ['sai', 222, 1.4]
    print(my_list)
    print(len(my_list))
    print(my_list[0])
    print(my_list[:2])
    my_list = my_list + ['1', "Sai"]
    print(my_list * 2)


def lists():
    l = [1, 2, 3];
    l.append('Sai')
    l.reverse()
    l.pop()
    print(l)
    l = [1, 2, 3];
    l.reverse()
    l.sort()
    print(l)


def lists2():
    l_1 = [1, 2, 3]
    l_2 = [4, 5, 6]
    l_3 = [7, 8, 9]
    matrix = [l_1, l_2, l_3]
    print(matrix)
    print(matrix[0])
    print(matrix[0][1])
    print(matrix[1][1])


def list_comprehension():
    l_1 = [1, 2, 3]
    l_2 = [4, 5, 6]
    l_3 = [7, 8, 9]
    matrix = [l_1, l_2, l_3]
    # for every row in the matrix grab the 0th index
    first_col = [row[0] for row in matrix]
    print(first_col)


if __name__ == "__main__":
    list_comprehension()
