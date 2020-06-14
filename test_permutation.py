x_str = "abc"

print("String = ", x_str) 

result = [] 

def permutation(data, i, length):  

    if i == length:  
        result.append(''.join(data) ) 
    else:  
        for j in range(i, length):  

            # swap 
            data[i], data[j] = data[j], data[i]  
            permutation(data, i + 1, length)  
            data[i], data[j] = data[j], data[i]   
permutation(list(x_str), 0, len(x_str)) 
print("Permutations", str(result))

