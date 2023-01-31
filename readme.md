## Module Description

In this module, you'll learn about GitHub Classroom and the tools used for automating software development tasks such as
testing and deployment. These processes are known as Continuous Integration and Continuous Deployment (CI/CD) and are
crucial for DevOps engineers to move code from development to deployment for user use. GitHub Classroom uses DevOps
tools to automatically grade your assignments based on tests located in the "grade" folder.

### [Video Lecture and Demonstration of Completing Assignment](https://youtu.be/HsS0vZngI1E)

## Hands-On Instructions

This exercise aims to demonstrate the functionality of GitHub Classroom and GitHub Actions by setting up automated
tests, building, and pushing a Docker image to Dockerhub. Here are the steps to complete the exercise:

1. Clone the repository using the "Get Started" instructions.
2. Create a repository on Dockerhub and update line 6 in
   the [.github/workflows/master.yml](.github/workflows/master.yml) file to match your repository name.
3. In your project repository on GitHub, navigate to the "Settings" tab, then the "Secrets and Variables" option on the
   left menu. Add your Dockerhub username and password as repository secrets under the names DOCKER_USERNAME and
   DOCKER_PASSWORD, respectively.

## Get started:

Each module in this course will follow the same process, unless otherwise noted on the assignment.

1. Click the "Start Assignment" button below to accept this assignment. The assignment will be duplicated on the NJIT
   WIS GitHub organization, and then you will be added to the repository along with the professor and the graders.
2. Clone the repository to your local computer using Pycharm.
3. Add your information to this file: [here](myinfo.json)  - Replace change with your information.
4. Type "python -m pip install -r .\requirements.txt" to install the dependencies or just pip/pip3 install -r
   requirements.txt
5. When you complete the assignment, you must push the code back and then go to the "Actions" tab on your repositories'
   homepage to see it autograde the assignment. If the autograder turns green then you got 100, if it is red then you
   will need to click on the autograder link on that page to find your errors to fix them. You should test if your code
   passes the grader locally before pushing by following the tip below. Two workflows will run each time you push. One
   workflow is the grading and the other workflow is the deployment.
6. Once you are satisfied, you need to submit the link to your repo to Canvas.

[![Click to Start Assignment](module_content/images/start.png)](https://classroom.github.com/a/KvHfpLwn)

## Tips - IMPORTANT 

### If everything works these should work.

1. If you type "pytest -c pytest_grade.ini" the code will run the grader tests.
2. If you type "pytest" the code will run your own automated tests that you put in the "tests" folder.
3. If you type "pytest -s" you will be able to see your print statements your code output when you run the
   tests
4. If you type "pytest tests/test_testfile.py it" will run a specific test file you specify.
5. pip install -r requirements.txt <-install dependencies

### If you have command not found with PIP or Pytest try python or python3 for these (The problem is the python path)

1. If you type "python -m pytest -c pytest_grade.ini" the code will run the grader tests.
2. If you type "python -m pytest" the code will run your own automated tests that you put in the "tests" folder.
3. If you type "python -m pytest -s" you will be able to see your print statements your code output when you run the
   tests
4. If you type "python -m pytest yourtestfile.py
5. "python -m pip install -r requirements.txt" <-install dependencies

## Licence

Copyright (c) 2012-2022 Scott Chacon and others

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
