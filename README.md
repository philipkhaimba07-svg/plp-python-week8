# Personal Mini-Toolkit

A menu-driven Python program with three tools: a number-guessing game,
a to-do list, and a name formatter.

## How to run
1. Make sure Python 3 is installed.
2. In a terminal, go to this folder and run:
   python toolkit.py
3. Type the number of a tool and press Enter. Choose 4 to quit.

## Reflection

## Reflection

The hardest tool to build was the to-do list, because it uses a list that
changes while the program runs and I had to keep track of adding, showing and
removing tasks inside its own loop. The part that took me longest overall was
not a crash in the code but getting my submission right: I had to retake my
screenshots as proper full-screen captures instead of phone photos, and my
README reflection was left as placeholder text until I replaced it. While
testing, I learned why checking `in` before `.remove()` matters, because typing
a task that wasn't on the list showed "That task is not on your list." instead
of crashing. I'm proudest of the main menu, since it keeps returning after every
tool and handles invalid choices like `9` politely. Planning in toolkit_plan.txt
first made the build easier because I already knew my menu text and which
concepts each tool needed. With one more week, I would add a fourth tool such as
a calculator and save the to-do list to a file so tasks are not lost when the
program closes.
