

def capturing_rainwater(list_1):
    first_bound = 0
    first_val = list[0]
    length = len(list_1)
    for i in range (1, length):
        second_val = list_1[i]
        if second_val > first_val:
            second_bound = i
            if list_1[second_bound] > list_1[first_bound]:
                lower_value = list_1[first_bound]
            else:
                lower_value = list_1[second_bound]
            total_ground_height = 0
            for i in range (first_bound + 1, second_bound):
