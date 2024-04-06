# Door mat design 

def door_mat_design(rows, columns):
    pattern = [('.|.' * (2 * i + 1)).center(columns, '-') for i in range(rows // 2)]
    welcome_line = 'WELCOME'.center(columns, '-')
    bottom_pattern = pattern[::-1]

    door_mat = '\n'.join(pattern + [welcome_line] + bottom_pattern)
    return door_mat

# Example: Door mat with size 7x21
mat_size = 7         # Numbet of lines 
mat_columns = 21     # Number of chars in one row 

result = door_mat_design(mat_size, mat_columns)
print(result)



