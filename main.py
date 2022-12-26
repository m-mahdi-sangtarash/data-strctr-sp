import numpy as np
import proj_2_functions as p2f

num_array = np.array([0 for _ in range(50)])
index = None

# receive numbers Function
num_array, index = p2f.receive_nums_func(num_array, index)
# sort numbers Function
num_array, index = p2f.sort_number_func(num_array, index)
# find item - binary
p2f.search_num(num_array, index)
