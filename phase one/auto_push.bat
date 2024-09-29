@echo off

REM Navigate to the directory (Adjust the path if needed)
cd "c:\Users\tusha\Desktop\Basic-150\phase one"

REM Stage all changes
git add .

REM Prompt the user for a commit message
set /p commit_message="Enter the commit message: "

REM Commit changes with the provided message
git commit -m "%commit_message%"

REM Push changes to the main branch
git push origin main
