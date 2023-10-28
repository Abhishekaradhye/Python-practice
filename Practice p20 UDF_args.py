def function(*args):
    if len(args) == 3:
        print(f'Name {args[0]}, age {args[1]} and roll number {args[2]}')
function('Abhi',23,92)

def print_marks(**kwargs):
    for k,v in kwargs.items():
        print(k,v)
mark_list = {'Amit':92, 'Kumar':87, 'Suresh':90}

print_marks(**mark_list)