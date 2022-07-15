def print_list(one_list):
    for value in one_list:
        print(value)

def print_reverse(one_list):
    for i in range(len(one_list) -1 , -1 , -1):
        print(one_list[i])

def reverse_list(one_list):
    output = []
    for i in range(len(one_list) -1 , -1 , -1):
        output.append(one_list[i])
    return output
def main():
    one_list = [1,2,3,4]
    output = reverse_list(one_list)
    print(output)

if __name__ == '__main__':
    main()
