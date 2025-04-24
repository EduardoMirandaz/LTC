# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    arr_list_len = 1 # We can do this because N is >= 1
    idx = 0

    while A[idx] != -1:
        arr_list_len += 1
        idx = A[idx]

    return(arr_list_len)


            
    
