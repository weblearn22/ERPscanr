#!/bin/sh

# Check how many lines there are in module - excludes blank lines
printf "\n\n\n\n CHECK MODULE SIZE:"
printf "\nNumber of lines of code & comments in ERP-SCANR: "
find ./erpsc -name "*.py" -type f -exec grep . {} \; | wc -l

# Check number of files using cloc
printf "\n\n\n CLOC OUTPUT: \n"
cloc erpsc

# Run Tests & Check Coverage
printf "\n\n\n RUN TESTS & TEST COVERAGE: \n"
coverage run --source erpsc -m py.test
coverage report
#py.test

# Find a way to get summary from pylint?

# Print out some new lines
printf "\n\n\n\n"