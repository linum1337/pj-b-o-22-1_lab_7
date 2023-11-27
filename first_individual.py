def main():
    numbers_seq = [int(input("Введите число: \n")) for i in range(10)]
    print(sum_finder(numbers_seq))


def sum_finder(numbers_list: list) -> int:
    summary = 0
    for num in numbers_list:
        if num < 0 and num % 7 == 0:
            summary += num

    return summary


if __name__ == '__main__':
    main()
