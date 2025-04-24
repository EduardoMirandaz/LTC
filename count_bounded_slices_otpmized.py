# you can write to stdout for debugging purposes, e.g.
# print( "this is a debug message")

# still need to make it faster

def solution(K, A):

    n = len(A)
    checked_pairs = {}
    answer_count = 0
    for i in range(n):
        for j in range(n):
            if (i, j) not in checked_pairs and i <= j:
                higher_value = None 
                min_value = None
                for k in A[i:j+1]:
                    if(higher_value == None or min_value == None):
                        higher_value = k
                        min_value = k
                else:
                        # The only case where the pair (i, j) isn't on the map is 
                        # when we update i. Therefore, at this point, I'm sure that
                        # i is equal to j, and line 15 prevents the code from
                        # entering this branch without (i, j) being in the checked_pairs map,
                        # which would otherwise lead to an "index not found" error.

                        previous_minor = checked_pairs[(i, j-1)][0]
                        previous_higher = checked_pairs[(i, j-1)][1]

                        if k > previous_higher:
                            higher_value = k
                        else:
                            higher_value = previous_higher
                        
                        if k < previous_minor:
                            min_value = k
                        else:
                            min_value = previous_minor
                checked_pairs[(i, j)] = (min_value, higher_value)
                print(f'Adding the pair {i, j}: {min_value, higher_value}')
                if(higher_value - min_value <= K):
                    answer_count+=1
    return (answer_count)


if __name__ == '__main__':
    print(solution(6, [2,3,5,0,2,1,12]))