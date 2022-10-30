class Mathematician:
    pass

    def square_nums(self, num: list):
        return list(map(lambda x: x**2, num))

    def remove_positives(self, num: list):
        return list(filter(lambda x: x > 0, num))

    def filter_leaps(self, num: list):
        return list(filter(lambda x: x % 4 == 0 and x % 100 != 0 or x % 400 == 0, num))


nums = [1, -23, 3, 100, -2, 0, 23, 54, -232]
nums_1 = [2028, 1938, 2024, 2020, 2016, 2012, 2042, 2011, 2008, 2007, 2004]

m = Mathematician()

print(m.square_nums(nums))
print(m.remove_positives(nums))
print(m.filter_leaps(nums_1))


