'''
import random

def generate_list():
    max_num = int(input("How many numbers do you want to generate? "))
    return [random.randint(1, max_num) for _ in range(max_num)]

def display_list(lst):
    print("-------------------------------------------------------------------------------------------------------------")
    string = sum(lst)
    for i in lst:
        print("list =", i)
    print("sum =", string)

def switch_numbers(lst, d):
    x = d - 1
    lst[d], lst[x] = lst[x], lst[d]

def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

def sort_list(lst):
    sorted = False
    tryed = 0
    while not sorted:
        sorted = True
        for d in range(len(lst)-1):
            if lst[d] > lst[d+1]:
                switch_numbers(lst, d)
                sorted = False
        tryed += 1
    return tryed

def find_max(lst):
    max_value = max(lst)
    print("Max =", max_value)

def main():
    lst = generate_list()
    display_list(lst)
    choice = int(input("Enter 1 for sorting or 2 for finding the maximum value: "))
    if choice == 1:
        try_count = sort_list(lst)
        print("Sorting completed in", try_count, "tries")
        display_list(lst)
    elif choice == 2:
        find_max(lst)

if __name__ == "__main__":
    main()
'''
def inpput:
    length =int(input())
    print(length)
    print(type(length))
    print()


