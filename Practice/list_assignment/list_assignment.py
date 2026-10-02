import random 

random_num = [random.randint(1,20) for _ in range(15)]
print(f"Original List:{random_num}")

sorted_num = sorted(random_num)
print(f"Sorted in Ascending Order:{sorted_num}")

sorted_num_dec = sorted(random_num,reverse=True)
print(f"Sorted in Descending Order:{sorted_num_dec}")

uqinie_number = list(set(random_num))
print(f"List with duplicates removed: {uqinie_number}")
