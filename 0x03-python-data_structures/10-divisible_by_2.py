cat > 10-divisible_by_2.py
#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = []
    for integer in my_list:
        list_result.append(integer % 2 == 0)
    return (list_result)
