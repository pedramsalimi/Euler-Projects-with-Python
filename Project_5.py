# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import fractions

def project_5():
	min = 1
	for i in range(1, 21):
		min *= i // fractions.gcd(i, min)
	return min
print(project_5())
