# Softeng Grade Calculator

**Name:** Jhon Zinoel N. Buado
**Section:** IT3r10

## Description
A small command-line program written in Python that calculates the average of the grades you enter.

## How to run
1. Install [Python 3](https://www.python.org/downloads/).
2. Clone the repository:
   ```
   git clone https://github.com/ZinZin360/Softeng-grade-calculator.git
   cd Softeng-grade-calculator
   ```
3. Run the program:
   ```
   python grade_calculator.py
   ```
4. Enter each grade and press Enter. Type `done` to see the result.

## Reflection
While working on this project, the problem I ran into was a Git warning on every commit: "LF will be replaced by CRLF the next time Git touches it." I was on Windows, and I worried that Git was changing my files in a way that would show up as messy differences or break the code on other computers. At first I ignored the warning, but it kept appearing for every file, so I looked it up. I learned that Windows uses CRLF line endings while Linux and macOS use LF, and Git can convert between them depending on the core.autocrlf setting. To fix it cleanly, I added a .gitattributes file containing "* text=auto" so Git normalizes line endings the same way for everyone who works on the repository, no matter their operating system. I committed that file with its own message so the change was easy to find in the history. Another small thing I noticed was that my local main branch said its upstream was gone, which reminded me to check the remote with git remote -v before pushing. This taught me to read Git warnings carefully instead of dismissing them, and that a tiny configuration file can prevent confusing problems later.
