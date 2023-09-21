# qaf-python-helloworld #

This repository contains a simple "Hello, World!" example using the QAF-Python framework.


## Installation
1. Clone this repository to your local machine:
    ```commandline
    git clone https://github.com/qmetry/qaf-python-helloworld.git
    ```
2. Navigate to the project directory:
    ```commandline
    cd qaf-python-helloworld
    python3 -m venv ./venv
    source venv/bin/activate 
    ```
3. Install the required dependencies:
    ```
    pip3 install -r requirements.txt
    ```
   
or to reinstall:
    ```
    pip3 install -r requirements.txt --force-reinstall
    ```

## Running the Test
To run the "Hello, World!" example using QAF-Python, execute the following command:

    pytest [<options>]

This command will execute the test script located in the tests folder. 


## View report
Open dashboard.htm to view current and past execution reports. 
To open as local file in browser refer [browser settings](https://github.com/infostretch/qaf-report#local-report-access). 
Best way is to install maven and view reports by following below steps: 

1. Install maven (One time)
2. In terminal, navigate to Project directory and run 
    ```
    mvn -f repo-editor-runner.xml exec:java

    ```
3. Open http://localhost:2612 in any browser of your choice


## Repo-editor
Refer [documentation](https://qmetry.github.io/qaf/latest/repo_editor.html) for features and usage.
1. Install maven (One time)
2. In terminal, navigate to Project directory and run 
    ```
    mvn -f repo-editor-runner.xml exec:java

    ```
3. Open http://localhost:2612/repo-editor in any browser of your choice



