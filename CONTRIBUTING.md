# Welcome to Skareds Contributing Guide
Thank you for taking an interest in contributing to our project!

The contribution types we're looking for are either new retro game additions made in python using the pygame library or enchancements to games already made. 
Our vision for this project is to collect a wide range of retro style games made in pygame.  
In this guide you will get an overview on the contribution workflow and how to file a bug report.


## Work flow
1. First create a new issue. The issue should be descriptive and contain an intial checklist of steps to fufil the issue. Use label "game addition" or "enchancement" depending on your intention. 

2. Fork and clone the main project repository

3. Branch from master with your new feature branch. Name should describe the feature. 

4. Start working in on your feature. Use feature flags for large features.

5. Make sure to regularly fetch from origin master (and rebase) to keep up to date with main repository. 

6. Run the test suite in your local clone. Only after passing all tests can you create a pull request.

7. Create a new feature branch in the main repository and pull request to it.
8. Pull request title and description should be descriptive, reference and link to the issue. 
9. You will require someone to review and approve your pull request before merge. 
10. If you pass sonarCloud tests your reviewer will merge your code. Squash commits. 
11. Make a new issue for merging this new branch with main. This is when your game will be added to the main menu.
12. Work on this new branch
13. Pull request after passing test suite and sonarCloud tests. 
14. Once reviewed, the reviewer will merge your feature branch with main branch.

Thank you for contributing to Skared!

## Main Menu Additions
In order to add things to the main menu, you can simply create a screen item using an image that you have imported to be the button. By looking at how the other "ScreenItem" objects work, you can see and recreate one for your own additions to the code! This is the easiest way to add something to the main menu and we highly recommend placing things on through this method

## Test file
In the main game folder, you should find a file called unit_tests.py. When making any commits, please add any other appropriate imported files and run the test file, making sure that all tests pass before making a commit or push. These unit tests check if the file is able to be imported, and then will also run through the top initialization of the file and check no errors occur there

## Bug report
If you wish to file a bug report, create an issue with the label "bug". If you wish to fix the bug apply the steps in workflow. 

## Suggestions
You can suggest a new feature at any time by creating an issue that accurately describes your idea and using labels as described in workflow.




