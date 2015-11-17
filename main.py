
weight   = []
input    = [[0,1],[1,1]]

# AND
expected = [0,1]

def sommePondere(inputs_list, weight_list):
    count = 0
    res = 0
    length = len(inputs_list)
    while count < length:
        accumulateur += inputs_list[count] * weight_list[count]
        count += 1
    return res
