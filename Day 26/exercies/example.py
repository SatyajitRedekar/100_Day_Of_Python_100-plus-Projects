
file1_data = [int(num.rstrip()) for num in open("file1.txt")]
file2_data = [int(num.rstrip()) for num in open("file2.txt")]

result = []
numbers = [result.append(num1) for num1 in file1_data for num2 in file2_data if num1 == num2 and num1 not in result]

print(result)