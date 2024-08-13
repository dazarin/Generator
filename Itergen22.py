import types

def flat_generator(list_of_lists):
    i = 0
    j = 0
    while i < len(list_of_lists):
        while j < len(list_of_lists[i]):
            item = list_of_lists[i][j]
            j += 1
            yield item
        j = 0
        i += 1

test_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

result_list = list(flat_generator(test_list))
print(result_list)

result_gen = (item for row in test_list for item in row)
result_list2 = list(result_gen)
print(result_list2)

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()