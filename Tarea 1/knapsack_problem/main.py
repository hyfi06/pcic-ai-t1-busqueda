
def read_problem(fileName):
    data = []
    with open(fileName, mode = 'r') as file:
        data = file.readLines()
    data = [row.split('\t') for row in data]
    [objects_num, size] = data.pop(0)
    asset(len(data)==objects_num)

    return (objects_num, size, data)



def main():
    pass

if __name__ == "__main__":
    main()
