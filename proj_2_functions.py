def receive_nums_func(num_array, index):
    while index is None or index < 49:
        if index is None:
            try:
                num_array[0] = int(input('please enter your number: '))
                index = 0
                continue
            except ValueError:
                continue
        else:
            try:
                num_array[index + 1] = int(
                    input('please enter your number (if you want break this operation enter a letter): '))
                index += 1
            except ValueError:
                break
    return num_array, index


def sort_number_func(num_array, index):
    for i in range(0, index):
        for checker in range(0, index):
            if num_array[checker] < num_array[checker + 1]:
                num_array[checker] += num_array[checker + 1]
                num_array[checker + 1] = num_array[checker] - num_array[checker + 1]
                num_array[checker] -= num_array[checker + 1]
    print('list sorted')
    return num_array, index


def search_num(num_array, index):
    while 0 < 1:
        try:
            item = int(input('enter your number: '))
            break
        except ValueError:
            continue
    ub = index
    m = int(ub / 2)
    lb = 0
    while num_array[m] != item and ub >= lb:
        if item > num_array[m]:
            ub = m - 1
        else:
            lb = m + 1
        m = int((ub + lb) / 2)
    if item == num_array[m]:
        print(f'{item} in {m} index')
    else:
        print('item not found!')
