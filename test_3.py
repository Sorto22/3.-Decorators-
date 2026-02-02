from test_1 import logger as logger1
from test_2 import logger as logger2
from Flatgenerator import flat_generator


def test_1(list_of_lists):
    """Тестирование первого декоратора"""

    @logger1
    def flat_generator_wrapper(list_of_lists):
        return list(flat_generator(list_of_lists))

    result = flat_generator_wrapper(list_of_lists)
    print(f"Test 1 result: {result}")


def test_2(list_of_lists):
    """Тестирование второго декоратора"""

    @logger2('logger_2.log')
    def flat_generator_wrapper(list_of_lists):
        return list(flat_generator(list_of_lists))

    result = flat_generator_wrapper(list_of_lists)
    print(f"Test 2 result: {result}")


if __name__ == '__main__':
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    test_1(list_of_lists_1)
    test_2(list_of_lists_1)