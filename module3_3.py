def print_params(a=1, b='str', c=True):
    print(a, b, c)

print_params()
values_list = ('5', 10, [True, False])
values_dict = {'a': 10, 'b': 'Urban', 'c': False}
print_params(*values_list)
print_params(**values_dict)
values_list2 = ('Mary', 17)
print_params(*values_list2, 42)