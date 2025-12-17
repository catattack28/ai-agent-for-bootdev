
from functions.run_python_file import run_python_file

result1=run_python_file("calculator", "main.py")
print("Running test for main.py")
print("should print the calculator's usage instructions")
print(result1)

result2=run_python_file("calculator", "main.py", ["3 + 5"])
print("Result for main.py and [\"3 + 5 \"]:")
print("(should run the calculator, which gives a kinda nasty rendered result)")
print(result2)

result3=run_python_file("calculator", "tests.py")
print("Result for tests.py:")
print("(should run the calculator's tests successfully)")
print(result3)


result4=run_python_file("calculator", "../main.py")
print("Result for ../main.py:")
print(" (this should return an error)")
print(result4)


result5=run_python_file("calculator", "nonexistent.py")
print("Running test for nonexistent.py")
print(" (this should return an error)")
print(result5)

result6=run_python_file("calculator", "lorem.txt")
print("Result for lorem.txt:")
print("(should return error)")
print(result6)
