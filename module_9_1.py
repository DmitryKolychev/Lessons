def apply_all_func(int_list, *functions):
    results = {}
    int_list_new = []
    for i in int_list:
        int_list_new.append(int(i))
    for func in functions:
        results[func.__name__] = func(int_list_new)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func(['6', 20, 15, 9], len, sum, sorted))

