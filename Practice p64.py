'''Write a Python program to create a list by concatenating a given list with a range from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']'''

input_list = input('Enter sample list : ').strip("[]").replace("'", "").split(",")  # Parsing the list input
print('list given ', input_list)

n = int(input('Enter the number : '))

numbers = range(1, n+1)  # Correct range to include 'n'
sample_output = []

for nums in numbers:
    for sample in input_list:
        sample_output.append(f"{sample}{nums}")

print(sample_output)
