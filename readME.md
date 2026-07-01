# XcodeOffline

## What is XcodeOffline?
XcodeOffline is a script that allows you to practice Problem Solving without an Internet Connection, unlike websites like Leetcode or Codewars.
The Main goal of this is to make it offline, as you don't have to hand over data to Leetcode or whatnot (even though I have an account on it... if this matures I can leave leetcode).  

## Features:

* Search for problems in your respective database!


## "I can't find my problems here, Im returning to Leetcode!"
Stop worrying, amigo. This script can mature with contributions from the community, and I plan on adding an "Import Problems" thingy. How it'd go is you use the Class built in the main script, and create an array of Problems. Then simply import it here!  

This is just a project, but I hope it matures!

## Planned Features:

* Add custom tests.

## How do I use this script?

Let me break it down for you:

* Searching for a problem: run the script with the `--search` parameter. If you wanted to, say, look for the Binary Search Algorithm, go: `python3 XcodeOffline.py --search query n diff`, where `n` is the number of results you'd prefer (default is 25),and `diff` being difficulty, if you're looking for a certain difficulty. Options include `easy`, `medium`, `hard`, and `extreme`. The result would be:

# An Important lil note here
instead of writing `python3 XcodeOffline.py` in your terminal, download the executable for your OS and replace that long line with `XcodeOffline`. Convenient, Right?

  `ID. problem name`

This is the block that represents a found solution. Every problem has a unique ID, which is used to identify which problem you're solving when you run/submit the tests.

* Running a test: run `script --run ID`, where --run is the name of the command (in this case, running), and ID is the identifier of the problem. This assumes that the file where you wrote your function is named script.py and the function's  name is `xcodescript`.

> [!TIP]
> This script only supports Python functions sadly. Maybe I'll add support for JS/TS, potentially other languages... Maybe.

* Submitting a solution: same thing as running, `--submit` instead of `--run`.


## How to Compile?

Use pyinstaller, like this:

`pyinstaller script_path -F --onefile`

You can also use `-n NAME` if you like convenience.
