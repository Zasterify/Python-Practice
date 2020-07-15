# Damiete's Python Practice

This is where I will be typing instructions for things you should get done. As always make sure you read it
all before you start.

## Notes

##### When you are done doing your work, always make sure to merge it with the master. I will only push and pull from the master branch. You are to make the branch, do your work in the branch, and merge it back when you are ready for me to view.

##### Do not use the GitKraken to view this file. You have two options to view this file.

1. Go to your github accounts, enter the `Python Practice` then click on README.md
2. Open the `Python Practice` on your VSCode Software, click on `Extensions` and install "Markdown Preview Enhanced". Then open the README.md and click on the button to view it. - Ask me if this is confusing. I can explain since i am here for this part.

Remember to commit and push. Do NOT use generic names and numbers. Make sure the commit message makes sense about what you did. I should be able to read your commit message and understand in general what went on before you saved without ever opening the code.

## Time Limit: _1 hours_

This time limit is strict. You HAVE TO finish this under 1 hour.

## Instructions

In a file caught_speeding.py create a function caught_speeding that takes in two parameters speed, and birthday, and solves the following problem.

You are driving a little too fast, and a police officer stops you. Write code to compute the result, saved as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 points higher in all cases.

## Example

caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0
