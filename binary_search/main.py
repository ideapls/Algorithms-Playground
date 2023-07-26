my_list = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]


def binary_search(your_list, item):
    less = 0
    high = len(your_list) - 1
    step = 0

    while less <= high:
        step += 1
        print("Steps: " + str(step))
        middle = (less + high) // 2
        choice = your_list[middle]

        if choice == item:
            return middle
        if choice > item:
            high = middle - 1
        else:
            less = middle + 1
    return None


print(binary_search(my_list, 3))
