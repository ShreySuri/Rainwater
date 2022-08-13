

def capturing_rainwater(list_1):
    first_bound = 0
    first_val = list_1[0]
    length = len(list_1)
    vacancy = 0
    for i in range (1, length):
        print("check")
        second_val = list_1[i]
        if second_val > first_val:
            second_bound = i
            if list_1[second_bound] > list_1[first_bound]:
                lower_value = list_1[first_bound]
            else:
                lower_value = list_1[second_bound]
            total_ground_height = 0
            columns = 0
            for j in range (first_bound + 1, second_bound):
                total_ground_heigth = total_ground_height + list_1[j]
                columns = coulumns + 1

            vacancy = vacancy + lower_value * columns - total_ground_height
            first_val = second_val
            first_bound = second_bound
        else:
            toggle = True

    return(vacancy)

test_array = [4, 2, 3]
print(capturing_rainwater(test_array))
