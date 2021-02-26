# GDIT Health Homework

GDIT Health take home exercises.

Your submissions are kept private and deleted after the interview process. These exercises are MIT Licensed. You are free to make a copy of your submission public.

## Instructions

1. Create a fork of this repository.
1. Solve the coding challenges within the `exercises` directory.
1. Commit your changes.
1. Submit a Pull Request to the original repository your were granted access to under the `GDITHealth` organization.

## Development Environment

We will only be reviewing your completed submission, not your development environment.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/GDITHealth/gdithealth-homework)

- Using the Gitpod development environment while the repository is Private will utilize a 30-day free trial. 
- If you prefer to avoid activating this free trial you may clone the repository and re-upload within your Public Github.
- Feel free to solve the programming challenges in any environment with which you are comfortable. We've provided some basic setup using Gitpod, but it is not required.

Example:

- Setup the dependencies on your own machine.
- Setup the dependencies within a virtual machine.


## Default Packaging

```bash
python # 3.8
black
flake8
jupyter
jupytext
pyspark>=3.0.0
java # v11+
git+https://github.com/GDITHealth/pysoma # Basic Spark functionality included
```

## Setting up pyspark

Setting up the development environment yourself depends on your platform. The following are general steps.

1. Use Python 3.8+
1. `pip install pyspark>=3.0.0 black flake8 jupyter jupytext`
1. Install Spark: [https://spark.apache.org/downloads.html](https://spark.apache.org/downloads.html)
1. Verify your `JAVA_HOME` environment variable. 
