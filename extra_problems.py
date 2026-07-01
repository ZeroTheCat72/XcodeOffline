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
                print(f"Test case Number {passed} passed! Input: {i[0]}, Output: {i[1]}\n")
            else:
                print(f"------\n!TEST CASE FAILED!\nPassed {passed} tests, Test case number {passed + 1} Failed!\nInput: {i[0]}, Expected Output: {i[1]}\nActual Output: {func_ref(*i[0])}")
                return
        print(f"Passed All {passed} Tests! You May be ready to submit!")

    def submit_test(self, func_ref):
        passed = 0

        for i in self.stests:
            if [func_ref(*i[0])] == i[1]:
                passed += 1
                print(f"Test case Number {passed} passed! Input: {i[0]}, Output: {i[1]}\n")
            else:
                print(f"------\n!TEST CASE FAILED!\nPassed {passed} tests, Test case number {passed + 1} Failed!\nInput: {i[0]}, Expected Output: {i[1]}\nActual Output: {func_ref(*i[0])}")
                return
        print(f"Passed All {passed} Tests! You solved this Problem!!")

new_problems = [
	Problem('return sum', 'return the sum of 2 nums.', 'Microsoft Interview Question 1', 'easy', [
	[[1, 2], [3]]
], [])
]
