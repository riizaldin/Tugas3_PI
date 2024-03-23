def read_numbers_from_file(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                numbers.append(int(line))
            except ValueError:
                print(f"Ignoring non-integer value: {line}")
    return numbers

def format_number_with_commas(number):
    return '{:.2f}'.format(number)

def main():
    filename = "indata.txt"
    numbers = read_numbers_from_file(filename)
    total = sum(numbers)
    formatted_total = format_number_with_commas(total)
    print(formatted_total)

if __name__ == "__main__":
    main()
