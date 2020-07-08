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

Make a file inside the folder for this one and call it "school.py"

For college kids to go back to school, many things need to happen. There needs to not be COVID, school must be open, and their tuition must be paid.
If any of these three things fail to happen, students cannot go back to school and must follow other instructions.

If covid is true, that means there is covid.
If school is true, that means school is open.
If tuition is true, that means tuition is paid.

Write a function called open_school that takes in three arguments, covid, school, and tuition.

- If there is no Covid and school is open and tuition is paid, then print "SCHOOL IS OPEN FOR IN PERSON INSTRUCTION"
- If there is no Covid and school is open and tuition is not paid, then print "SCHOOL IS OPEN, BUT YOU HAVE NOT PAID"
- If there is Covid or school is closed, and tuition is paid, then print "SCHOOL IS CLOSED FOR IN PERSON INSTRUCTION. PLEASE STAY HOME FOR ONLINE LEARNING"
- If any other situation occurs, print "SEEK FURTHER INSTRUCTIONS BY CONTACTING THE SCHOOL"

## Examples

open_school(true, true, true) = "SCHOOL IS CLOSED FOR IN PERSON INSTRUCTION. PLEASE STAY HOME FOR ONLINE LEARNING"
open_school(false, false, false) = "SEEK FURTHER INSTRUCTIONS BY CONTACTING THE SCHOOL"
