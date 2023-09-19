## Implementing CI/CD with GitHub Actions ##
<p>
In this section, we'll explore how to set up Continuous Integration (CI) and Continuous Deployment (CD) using GitHub Actions for our is_palindrome project. CI/CD is a crucial practice in modern software development that helps automate testing and deployment processes, ensuring code quality and streamlining development workflows.
</p>

## Section 1: Introduction to CI/CD and GitHub Actions

### What is CI/CD?

<p>
Continuous Integration and Continuous Deployment (CI/CD) is a set of practices and tools used in software development to automate the building, testing, and deployment of code changes. The primary goal of CI/CD is to streamline the development process, increase code quality, and ensure that software changes can be delivered to users reliably and efficiently.
</p>

### Why CI/CD?

* **Faster Development:** CI/CD automates repetitive tasks, such as testing and deployment, which can significantly speed up the development process.

* **Consistency:** It ensures that each code change is tested and deployed consistently, reducing the chances of human error.

* **Early Detection of Issues:** CI/CD runs tests automatically, allowing developers to identify and fix issues early in the development cycle.

* **Continuous Delivery:** It enables the continuous delivery of new features and bug fixes to end-users, promoting agility and responsiveness.

### GitHub Actions: What's Under the Hood?
<p>
GitHub Actions is a platform provided by GitHub to automate various tasks in your software development workflow. It allows you to define custom workflows as code, which are triggered by events such as code pushes, pull requests, or other GitHub activities.
</p>

### How GitHub Actions Works:

* **Virtual Environments:** When you define a GitHub Actions workflow, it runs in a virtual environment provided by GitHub. This environment is isolated, meaning it doesn't affect your local development environment.

* **Runner Machines:** GitHub Actions uses runner machines that execute your workflow. These runners can be hosted by GitHub (GitHub-hosted runners) or self-hosted on your infrastructure (self-hosted runners).

* **Workflow Configuration:** You define your workflow in a **.yml** configuration file. This file specifies the steps and actions to be taken in response to specific events.

* **Automation:** GitHub Actions automates tasks like building, testing, and deploying your code. It's like having a virtual machine running on GitHub's infrastructure that executes your instructions.

* **Feedback and Status Checks:** GitHub Actions provides feedback on the status of each workflow run, including success or failure. You can use this feedback to make informed decisions about merging code changes.

### GitHub Actions in Practice
<p>
In this lesson, we'll dive into using GitHub Actions to set up a CI/CD pipeline for your Python project. We'll leverage GitHub-hosted runners, define workflows to automate testing, generate code coverage reports, and prevent code pushes if tests fail. You'll gain hands-on experience with the practical implementation of CI/CD using GitHub Actions.
</p>

## Section 2: Understanding GitHub Actions Components

### YAML Configuration Files
<p>
In GitHub Actions, workflows are defined using YAML (YAML Ain't Markup Language) configuration files with a .yml extension. YAML is a human-readable data serialization format commonly used for configuration files. In the context of GitHub Actions, a YAML configuration file defines the steps and actions that make up a workflow.
</p>

### Why YAML?
* YAML is easy to read and write, making it accessible to both developers and non-developers.

* It's a structured format that allows you to define complex workflows in a concise and organized manner.

* YAML's simplicity makes it a popular choice for configuration files across various tools and platforms.

## Bash Actions and Scripting
<p>
GitHub Actions workflows often include Bash scripting. Bash (Bourne Again SHell) is a command-line shell and scripting language widely used in Unix-based operating systems. In the context of GitHub Actions, Bash scripting is used to define custom actions, run commands, and perform various tasks within a workflow.
</p>

**Key Points:**

* **Custom Actions**: You can create custom Bash scripts (or use existing ones) to define specific actions within your workflow. These actions can include building code, running tests, or deploying applications.

* **Running Commands:** Bash is used to run shell commands or scripts in the virtual environment provided by GitHub Actions. For example, you might use Bash to install dependencies, execute tests, or generate reports.

* **Conditionals and Logic:** Bash scripting allows you to add logic and conditionals to your workflows. You can make decisions based on the outcome of previous steps or external factors.

## Anatomy of a GitHub Actions Workflow
A typical GitHub Actions workflow configuration consists of the following components:

* **Name:** A user-defined name for the workflow.

* **Trigger:** Specifies the event(s) that trigger the workflow (e.g., push, pull_request).

* **Jobs:** One or more jobs that define the tasks to be executed. Each job runs in a separate virtual environment.

* **Steps:** Within each job, you define a sequence of steps. Each step is an individual task or action.

* **Actions:** Actions are reusable, shareable, and self-contained units of work. You can use built-in actions or create custom actions to perform specific tasks.

### Putting It All Together
<p>

In this lesson, we're using a **.yml** configuration file to define a GitHub Actions workflow. This workflow specifies when to trigger the CI/CD pipeline, sets up Python, installs dependencies, runs tests, generates coverage reports, and checks for test success. We'll use Bash scripting within the workflow to execute commands and make decisions based on the outcome of each step.

</P>

1. **Create A Github Actions Workflow**

* create a new branch called testing we will use this branch to send a pull request to our main branch.

you can do so by running the command:
```python3
git checkout -b testing
```

* In your GitHub repository, create a new directory named **.github/workflows**.

make a directory using the command:
```python3
mkdir .github/workflows
```

* Inside the .github/workflows directory, create a YAML file (e.g., main.yml) for defining your GitHub Actions workflow.

run the command in your terminal:
```python3
touch .github/workflows/main.yml
```

Here's a basic example of a GitHub Actions workflow for Python:
```python3
name: Python CI/CD

on:
  pull_request:
    branches:
      - main

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2

    - name: Run tests
      run: python -m unittest unittest_test.py

    - name: Install Coverage Package
      run: pip install coverage

    - name: Run tests and generate coverage report
      run: |
        python -m unittest unittest_test.py
        coverage run -m unittest unittest_test.py
        coverage report -m

    - name: Check test results and prevent push on failure
      run: |
        if [ ${{ job.status }} == "failure" ]; then
          echo "Tests failed. Preventing code push."
          exit 1
        fi
```

### Explanation in detail
<p>
This GitHub Actions workflow is designed for Continuous Integration and Continuous Deployment (CI/CD) of a Python project. It runs on every pull request to the main branch. The primary job, named "build," is executed on an Ubuntu virtual machine, specifically "ubuntu-latest." The workflow consists of several steps, each with a specific purpose:
</p>

* **Checkout code:** This step fetches the code from the repository.
* **Set up Python:** It sets up the Python environment using the actions/setup-python@v2 action.
* **Run tests:** This step executes Python unit tests using python -m unittest unittest_test.py.
* **Install Coverage Package:** It installs the coverage package required for code coverage analysis.
* **Run tests and generate coverage report:** This multi-line script runs the tests again with coverage analysis and generates a coverage report using the coverage tool.
* **Check test results and prevent push on failure:** Finally, this step checks the job status. If the tests fail (status is "failure"), it prints an error message and prevents code push.

### Key Components:

* **name:** The name of the GitHub Actions workflow, "Python CI/CD" in this case.
* **on:** Specifies the trigger event for the workflow, which is "pull_request" to the "main" branch.
* **jobs:** Defines one or more jobs to be executed within the workflow.
* **build:** The name of the job defined within the "jobs" section.
* **runs-on:** Specifies the type of runner environment, which is "ubuntu-latest" (an Ubuntu-based virtual machine) in this case.
* **steps:** Lists the individual steps to be executed within the job.
* **uses:** Specifies the GitHub Action to be used for a particular step, like "actions/checkout@v2" for code checkout.
* **run:** Contains the command(s) or script to be executed within a step.



## Adding Branch Protection Rules

<p>
To ensure that code is only merged into the main branch after passing tests, you can set up branch protection rules in your GitHub repository. This ensures that pull requests are reviewed and that required status checks pass before merging. Here are the steps to add branch protection rules:
</p>

Navigate to your repository on GitHub.

* Click on the "Settings" tab at the top-right corner of your repository.

![branches](https://user-images.githubusercontent.com/24584526/268679475-8c003068-5dcd-4d90-b90a-ea099c5f5b7c.png)


* In the left sidebar, click on "Branches."

* In the "Branch name pattern" field, enter the name of the branch you want to protect, typically "main."

* Scroll down to the "Protected branches" section.

* Check the box next to "Require pull request before merging." This ensures that pull requests must be reviewed and approved before merging.

* Check the box next to "Require status checks to pass before merging" This is crucial for ensuring that tests pass before code can be merged into the branch.

![branch_protection](https://user-images.githubusercontent.com/24584526/268853361-21b41c01-bfbd-400d-b990-4f8d60c54f41.png)


* After configuring the desired settings, click the "Save changes" button to apply the branch protection rules.

With these branch protection rules in place, pull requests to the main branch will only be mergeable if they meet the specified criteria, including passing the required status checks (tests).

2. **Create a pull request**

* First, make sure your local code changes are committed using Git.
* Commit your changes to the testing branch:
```python3
git add .
git commit -m "Your commit message here"
```
* Push the branch to the remote repository on GitHub:

 **Open GitHub Repository:**
 * **Open GitHub Repository:** Go to your GitHub repository's page in a web browser.
 * **Create a New Pull Request:** Click on the "Pull Requests" tab in the repository's menu.
 * **Click on "New Pull Request":** You'll find a green button labeled "New Pull Request." Click on it.


![pull_request](https://user-images.githubusercontent.com/24584526/268854097-0ce27934-6997-4502-9ca2-c3cb753f8625.png)

* **Compare Base and Compare Branch:** In the "Open a pull request" page, you'll see two drop-down menus:
* **Base repository:** This is usually the repository you forked or cloned.
* **Base:** Select "main" from the list.
* **Compare repository:** This is your repository.
* **Compare:** Select "testing" from the list.
* This setup means you want to merge the changes from the "testing" branch (your changes) into the "main" branch (the base branch).

![testing_pull](https://user-images.githubusercontent.com/24584526/268854215-18ed6a18-045d-489d-b2db-32947bda5c73.png)

* **Review Changes:** GitHub will automatically compare the changes between the two branches.
Review the changes to ensure they are correct.
* **Create Pull Request:** Click the "Create pull request" button.
* **Provide Pull Request Details:** Give your pull request a meaningful title and description to explain the changes you made.
* **Create Pull Request:**
Click the "Create pull request" button again.

![create_pull](https://user-images.githubusercontent.com/24584526/268854363-d7fc9996-c871-4075-a132-279136eaee96.png)

* **Review and Merge (CI/CD Testing):**
* When you create the pull request, GitHub will automatically trigger your CI/CD workflow (in this case, named "Python CI/CD") to run tests on the changes you made. You'll see a status like "Python CI/CD build (pull request) in progress" indicating that the CI/CD check has started.

* Wait for the CI/CD checks to complete. Your automated tests will run to verify that the changes do not introduce errors or break existing functionality.

![test_pending](https://user-images.githubusercontent.com/24584526/268854695-53cc404b-9e16-49c5-8648-4482d472dffc.png)

* If the CI/CD check passes successfully, you'll see a notification that says "All checks have passed." This means your code changes have passed the automated tests, and it's safe to proceed with the merge.

* You can then click the "Merge pull request" button with confidence, knowing that your code changes have been thoroughly tested and validated.

![test_passed](https://user-images.githubusercontent.com/24584526/268855121-288cbee2-e674-4b46-b7d6-686faffcb21d.png)

![merge_success](https://user-images.githubusercontent.com/24584526/268855592-cb643d21-97a1-4567-9653-ef288b3ed3e5.png)

* **Observe CI/CD Workflow**

* Go to the "Actions" tab in your GitHub repository to view the status of your CI/CD workflow.


![review_action](https://user-images.githubusercontent.com/24584526/268896575-783ddfd2-0c72-4c0b-acb1-9aefc7157d86.png)

![action](https://user-images.githubusercontent.com/24584526/268897035-0e66deb5-3032-4252-a99f-ae7f3e463c15.png)

* GitHub Actions will automatically run your tests whenever there's a pull request to the main branch. ensuring that any changes do not introduce regressions.

![jobs_review](https://user-images.githubusercontent.com/24584526/268897630-8996019d-4fc9-4705-81b9-9acdd19b0cd0.png)

![rerun_jobs](https://user-images.githubusercontent.com/24584526/268897960-d321de85-2455-4d62-ac71-37cac138f2a6.png)

![queued](https://user-images.githubusercontent.com/24584526/268898182-77328b37-aa52-49db-8f06-8862763420d0.png)

![in_progress](https://user-images.githubusercontent.com/24584526/268898520-e04754c2-5069-4c27-b621-cde44e58b7f3.png)

![success](https://user-images.githubusercontent.com/24584526/268898704-afeb89bd-cb3a-4c6b-826c-e161122dee30.png)

![first_review](https://user-images.githubusercontent.com/24584526/268898932-c2ccf36c-43f1-4ef3-af7e-1be7a931fb21.png)

![second_review](https://user-images.githubusercontent.com/24584526/268899089-42d6c0da-59a0-4fcf-b9e8-bff8c2dfe2cb.png)

![third_review](https://user-images.githubusercontent.com/24584526/268899234-73b6ad6c-6b23-4593-b283-de2fe13637fc.png)

![coverage_report](https://user-images.githubusercontent.com/24584526/268899904-caaa1591-718d-4bd2-9303-5007aec86711.png)


![fourth_review](https://user-images.githubusercontent.com/24584526/268900062-bdfcc787-334b-4e58-862c-f6484f2f3487.png)

Let's go ahead and see what happens when a test fails.

![failing_test](https://user-images.githubusercontent.com/24584526/268900485-b926e7a6-a9d7-427f-8e10-4e77e205cbcf.png)

![fail_review](https://user-images.githubusercontent.com/24584526/268900658-6b2784b4-6036-404d-ac0e-c086944b4977.png)

![fix_fail](https://user-images.githubusercontent.com/24584526/268900804-428ef039-ce68-45b4-803e-301355fee8b5.png)

![fail_pass](https://user-images.githubusercontent.com/24584526/268900954-97fafc1a-13c2-441a-b7de-5fc4bf045876.png)


![fix_merged](https://user-images.githubusercontent.com/24584526/268901122-b2ea4907-ac2d-4c3e-bf9f-87240fc03b2a.png)

![review_actions](https://user-images.githubusercontent.com/24584526/268901385-fb48fd12-5193-473c-9e25-f870d7c37519.png)


* You can easily collaborate with others on your project while maintaining code quality.
* Successful CI/CD workflows can be extended to include deployment steps, such as deploying to a production server or publishing packages.

<p>
By implementing CI/CD with GitHub Actions, you enhance your development process by automating repetitive tasks and promoting code quality, making your project more robust and reliable.
</p>

- [Link Github Actions Documentation](https://docs.github.com/en/actions)
