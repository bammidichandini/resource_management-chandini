def my_func():
    return 2

def test_mything(snapshot):

    return_value = my_func()

    # assert return_value == 2
    snapshot.assert_match(return_value, 'gpg_response')


a = 1
b = 2

def sum_func(a, b):
    return a+b

def test_sum(snapshot):

    return_value = sum_func(1, 2)

    snapshot.assert_match(return_value, 'summation')


def test_sum_with_floats(snapshot):

    return_value = sum_func(1.0, 2.5)

    snapshot.assert_match(return_value, 'floats_summation')


def test_sum_with_negative_nums(snapshot):

    return_value = sum_func(1, -2)

    snapshot.assert_match(return_value, 'negative_summation')


def test_sum_with3_possibilities(snapshot):

    return_value = sum_func(1, 2)
    return_value1 = sum_func(1.0, 2.5)
    return_value2 = sum_func(1, -2)

    snapshot.assert_match(return_value, 'summation')
    snapshot.assert_match(return_value1, 'floats_summation')
    snapshot.assert_match(return_value2, 'negative_summation')
