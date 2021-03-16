def index(array):
    zero_index = 0
    for i in array:
        if i == '0':
            return zero_index
        zero_index += 1


if __name__ == "__main__":
    array = "11100000000"
    print(index(array)) # 3