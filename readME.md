# ScriptDSA

## What is ScriptDSA?
ScriptDSA is a script that allows you to practice Problem Solving without an Internet Connection, unlike websites like Leetcode or Codewars.
The Main goal of this is to make it offline, as you don't have to hand over data to Leetcode or whatnot (even though I have an account on it... if this matures I can leave leetcode).  

This Project is, and always will be, free and open source. If you paid for it, demand a refund!

## Features:
* Solve Problems, completely Offline!
* Search for problems in your respective database!
* Add your Own Problems too! Problem scripts like Microsoft Interview questions, Meta Interview questions, etc, made by you or the community.

## "I can't find my problems here, Im returning to Leetcode!"
Stop worrying, amigo. This script can mature with contributions from the community, you can import your own Problems. How it'd go is you use the Class built in the main script, and create an array of Problems. Then simply import it here!  

This is just a project, but I hope it matures!

## Planned Features:

* add default problems to the main script, currently only 2, with one of them being a Mockup.
* add ability to review a question and its Run Cases.

## How do I use this script?

Let me break it down for you:

* Searching for a problem: If you wanted to, say, look for the Binary Search Algorithm, go: `python3 scriptDSA.py --search query n diff`, where `n` is the number of results you'd prefer (default is 25),and `diff` being difficulty, if you're looking for a certain difficulty. Options include `easy`, `medium`, `hard`, and `extreme`. The result would be:

`ID. problem name`
This is the block that represents a found solution. Every problem has a unique ID, which is used to identify which problem you're solving when you run/submit the tests.

* Running a test: run `script --run ID`, where --run is the name of the command (in this case, running), and ID is the identifier of the problem. This assumes that the file where you wrote your function is named script.py and the function's  name is `scriptdsa`.

* Submitting a solution: same thing as running, `--submit` instead of `--run`.

* Getting Problem Details: Running `script --details ID` will get you the problem name, and description. Examples are planned!

> [!TIP]
> This script only supports Python functions sadly. Maybe I'll add support for JS/TS, potentially other languages... Maybe.

> [!TIP]
> Instead of writing `python3 scriptdsa.py` in your terminal, download/compile the executable for your OS and replace that long line with `XcodeOffline`. Convenient, Right?

## How to create Custom Problems?

An `extra_problems.py` is included within the source code, which the XcodeOffline Executable searches for new Problems. 

To create a new problem, you'll have to use the `Problem` class. It takes multiple inputs: a name, description, ID, difficulty, Run tests, and Submit tests.

In order to add run/submit tests so everything works as expected, we'll need an example:
`
new_problems = [
	Problem('return sum', 'return the sum of 2 nums.', 'Microsoft Interview Question 1', 'easy', [
	[[1, 2], [3]]
], [])
]
`

Lets focus on this first array. It contains a list of `Problem`s. Inside it, if we check out our `run cases` or even `submit cases` (Im just too lazy to write submit cases), we'll see multiple nested arrays.
Each Array is a Test Cases, with [0] being inputs, and [1] being Output. we'll notice that the contents are... Another Array! Thats because there will always be a possibility that a function requires/returns multiple stuff, so an array is used to hold all Is and Os.
If you're passing in or returning an array, you can just nest in *another* list. Its confusing, but you'll get the hang of it!

## How to Compile?

Use pyinstaller, like this:

`pyinstaller script_path -F --onefile`

You can also use `-n NAME` if you like convenience.
