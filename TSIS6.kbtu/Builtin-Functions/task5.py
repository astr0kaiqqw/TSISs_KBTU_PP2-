def all_true(t):
    return all(t)  


t1 = (True, True, True)
t2 = (True, False, True)

print("Все элементы в t1 True?", all_true(t1))  
print("Все элементы в t2 True?", all_true(t2))  
