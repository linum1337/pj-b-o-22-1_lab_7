def main():
    list_duration = int(input("Введите кол-во чисел: \n"))
    numbers_list = [float(input("Введите число: \n")) for i in range(list_duration)]
    interval_a = float(input("Введите левую границу интервала:\n"))
    interval_b = float(input("Введите правую границу интервала:\n"))
    maximal_number_index = max_index_finder(numbers_list)
    summary_after_positive = sum_after_positive(numbers_list)
    sorted_by_interval = interval_sorter(numbers_list, interval_a, interval_b)
    print(
        f"Индекс максимального значения в списке: {maximal_number_index}"
        f"\nСумма всех чисел после первого положительного: {summary_after_positive}"
        f"\nОтсортированный список: {sorted_by_interval}")


def max_index_finder(numbers_list: list) -> float:
    max_number = max(numbers_list, key=abs)
    return numbers_list.index(max_number)


def interval_sorter(numbers_list: list, a: float, b: float) -> list:
    sorted_list = sorted(numbers_list, key=lambda x: (a <= int(x) <= b, x))
    return sorted_list


def sum_after_positive(numbers_list: list) -> float:
    flag = False
    summary = 0
    for number in numbers_list:
        if number > 0 and flag:
            summary += number
        elif number > 0 and not flag:
            flag = True
            summary += number
    return summary


if __name__ == '__main__':
    main()
