def calc_task():
   num1 = int(input("Type first total time task please : "))
   task1 = int(input("Type Total tasks please : "))
   num2 = int(input("Type Other total time task please : "))
   task2 = int(input("type other total tasks please : "))
   print("Your Salary is", ((num1 + num2) / 60) * 14.71, "$", " and Your total tasks is :", task1 + task2,)

calc_task()