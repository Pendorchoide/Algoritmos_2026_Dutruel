def fibonachi(num):
    if num == 1 or num == 0:
        return num
    else:
        return fibonachi(num - 1) + fibonachi(num - 2) 
    
print(fibonachi(35))