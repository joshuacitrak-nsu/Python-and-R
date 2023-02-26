# The Fizzbuzz program

# Print the numbers from 1 to 100
# Substitute the number with "fizz" if it is divisible by 3
# Substitute the number with "buzz" if it is divisible by 5
# Substitute with "FIZZBUZZ!" if it is divisible by both 3 and 5
#

count = range(1,101)
for each in count:
	if each % 3 == 0 and each % 5 == 0:
		print("FIZZBUZZ!")
	elif each % 3 == 0:
		print("fizz") 
	elif each % 5 == 0:
		print("buzz")
	else:
		print(each)

