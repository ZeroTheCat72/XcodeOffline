import sys
import math


class Problem:
	def __init__(self, name: str, description: str, ID: any, difficulty: str, Rtests, Stests):
		self.name = name
		self.description = description
		self.id = ID        # IDs should be the index in their respective list.
		self.difficulty = difficulty
		self.stests = Stests
		self.rtests = Rtests

	def get_problem_detailed(self):
		return f"{self.id}. {self.name}\n{self.description})"

	def get_problem(self):
		return f"{self.id}. {self.name}"




	def run_test(self, func_ref):
		passed = 0
		
		for i in self.rtests:
			if [func_ref(*i[0])] == i[1]:
				passed += 1
				print(f"Test case Number {passed} passed! Input: {i[0]}, Output: {i[1]}")
			else:
				print(f"!TEST CASE FAILED!\nPassed {passed} tests, Test case number {passed + 1} Failed!\nInput: {i[0]}, Expected Output: {i[1]}\nActual Output: {func_ref(*i[0])}")
				return
		print(f"Passed All {passed} Tests! You May be ready to submit!")



	def submit_test(self, func_ref):
		passed = 0
		
		for i in self.stests:
			if [func_ref(*i[0])] == i[1]:
				passed += 1
				print(f"Test case Number {passed} passed! Input: {i[0]}, Output: {i[1]}")
			else:
				print(f"!TEST CASE FAILED!\nPassed {passed} tests, Test case number {passed + 1} Failed!\nInput: {i[0]}, Expected Output: {i[1]}\nActual Output: {func_ref(*i[0])}")
				return
		print(f"Passed All {passed} Tests! You solved this Problem!!")



# Variables


list_of_problems = [
	Problem("binary search algorithm", "Its in the name Bro. Now DO IT.", '0', 'Easy', (
	[[[-7, -5, 1, 3],-7], [True]],
	[[[-6, -2, 11, 13],12], [False]],
	[[[800, 900, 1000, 1100],1000], [True]]
), {}),
	Problem("sans undertale", "Absolute Lamp", "Sans", 'Easy', {}, {})

]


difficulties = ["Easy", "Medium", "Hard", "Extreme"]


#Functions

def get_available_problems(n = 25, difficulty = None, query: str = ''):
	if n <= 0: return
	if difficulty != None:
		try:
			if len(list(filter(lambda x: x.difficulty == difficulty, list_of_problems))) == 0: 
				return f"No Existing Problems in {difficulty} difficulty."
			found_problems = list(filter(lambda x: x.difficulty == difficulty and query.lower() in x.name.lower(), list_of_problems))

		except:
			return "Difficulty Type Not Found. Available Difficulties: Easy, Medium, Hard, and Extreme."
	else:
		found_problems = list(filter(lambda x: query.lower() in x.name.lower(), list_of_problems))

	while len(found_problems) > n:
		found_problems.remove(found_problems[-1])
		

	for problem in found_problems:
		found_problems[found_problems.index(problem)] = problem.get_problem()
	return '\n'.join(found_problems)		



def fetch_problem(id: str, LOP):
	low = 0
	high = len(LOP) - 1
	while high >= low:
		median = math.floor((low + high) / 2)
		if LOP[median].id == id:
			return LOP[median]
		elif LOP[median].id < id:
			low = median + 1
		else: high = median - 1
	sys.exit(1)



# Main Work

try:
	from extra_problems import new_problems
	for problem in new_problems:
		list_of_problems.append(problem)
except:
	pass


list_of_problems = sorted(list_of_problems, key=lambda x: x.id)


if sys.argv[1] == '--search':
	print(get_available_problems(int(sys.argv[3]) if len(sys.argv) >= 4 else 25, sys.argv[4] if len(sys.argv) >= 5 else None, sys.argv[2]))
elif sys.argv[1] == '--run':
	import script
	Challenge_problem = fetch_problem(sys.argv[2], list_of_problems)
	print(Challenge_problem.run_test(script.xcodescript))
elif sys.argv[1] == '--submit':
	import script
	Challenge_problem = fetch_problem(sys.argv[2], list_of_problems)
	print(Challenge_problem.submit_test(script.xcodescript))

