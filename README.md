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

In a file called date_fashion.py create a function date_fashion that solves the following problem.

You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is saved as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish (8 or more), then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe). Print the results.

## Examples

date_fashion(5, 10) → 2
date_fashion(5, 2) → 0
date_fashion(5, 5) → 1
