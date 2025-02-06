'''Write a Python program to calculate a dog's age in dog years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
Expected Output:

Input a dog's age in human years: 15                                    
The dog's age in dog's years is 73'''


def calculate_dog_age(human_years):
    if 0 < human_years <= 2 :
        print("The dog's age in dog's years is", human_years*10.5)

    if human_years > 2 :
        print("The dog's age in dog's years is", 21 + (human_years -2 )*4)

calculate_dog_age(15)
