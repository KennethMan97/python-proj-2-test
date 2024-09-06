from python_proj_1_test import greet
from python_proj_1_test.moduleA import sum
from python_proj_1_test.moduleB import div
from python_proj_1_test.utils.moduleC import mult

def main():
	greet("Lorem Smith")
	print('\n')
	sum(2,2)
	print('\n')
	div(6,2)
	print('\n')
	mult(12,12)
	print('\n')

if __name__ == "__main__":
    main()
