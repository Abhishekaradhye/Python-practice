def master_func(word,*args,**kwargs):
    print(word)
    print(f'Roll number {yes[0]}, Mr.{yes[1]} have successfully secured CGPA pointer of {yes[2]}. ')
    for key, value in kwargs.items():
        print(key,value)
yes = [92,'Abhishek',8.53]
marklist = {'Akshay':34,'Salman':40,'Shah Rukh':80,'Ajay':60,'Hritik':70,'Amir':50}
master_func('What is it',*yes,**marklist)
