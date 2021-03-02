# GDIT Health Take Home Exercises

GDIT keeps your submissions private.

These exercises are MIT Licensed. There is no harm in redistribution or in making a copy of this repository publicly accessible. Please do not distribute your solution.

## Instructions

1. Create a fork of this repository.
1. Complete your selected coding challenge within the `exercises` directory.
1. Submit a Pull Request with your completed solution.

## Development Environment

Only the code submitted through the Pull Request is reviewed.

You are free to solve the programming challenges in any environment, but your solution is graded using the dependencies listed in the next section.

We've provided a basic Gitpod based environment if you're not comfortable setting up a Spark deployment. You are not required to utilize Gitpod.

Example Development Environments:

- Setup the dependencies on your own machine.
- Setup the dependencies within a virtual machine.
- Use Gitpod
  - Using the Gitpod development environment while the repository is Private will utilize a 30-day free trial. If you prefer to avoid activating this free trial you may clone the repository and re-upload to your Github as a public repository.
  - Add `https://gitpod.io/#` to the start of this repository url.
  - Examples:
    - From GDITHealth: `https://gitpod.io/#https://github.com/GDITHealth/gdithealth-code-challenge-firstName-lastName`
      - If you try to commit, Gitpod will prompt you to fork the repository to your Github account.
    - From a fork within your Github: `https://gitpod.io/#https://github.com/JaneDoe/gdithealth-code-challenge-jane-doe`

## Dependencies

We will run your code in an environment with the following dependencies.

```bash
python >= 3.8
pyspark >= 3.0.0
java # v11+
pytest

# pysoma provides access to a pre-configured Spark Session
# You -must- utilize the Spark Session available within this package
# Exercise prompts explain how to create a Spark Session
git+https://github.com/GDITHealth/pysoma
# Note this is NOT pysoma from pypi.org
# If you're installing in your own dev environment use:
# pip install git+https://github.com/GDITHealth/pysoma
```

## Personal Development Environment

Setting up the development environment yourself depends on your platform. The following are general steps.

1. Use Python 3.8+
1. `pip install pyspark>=3.0.0 black flake8 jupyter jupytext pytest git+https://github.com/GDITHealth/pysoma`
1. Install Spark: [https://spark.apache.org/downloads.html](https://spark.apache.org/downloads.html)
1. Verify your `JAVA_HOME` environment variable.
