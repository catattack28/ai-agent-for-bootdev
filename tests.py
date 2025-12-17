from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

result4=get_file_content("calculator", "main.py")
print("Result for 'main.oy':")
print(result4)

result3=get_file_content("calculator", "pkg/calculator.py")
print("Result for 'pkg/calculator.py':")
print(result3)

result2=get_file_content("calculator", "/bin/cat")
print("Result for /bin/cat (expecting error):")
print(result2)

result1=get_file_content("calculator", "pkg/does_no_exist.py")
print("Result for pkg/bullshit (expecting error):")
print(result1)
