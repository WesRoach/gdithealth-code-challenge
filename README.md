# Take Home Exercises

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
    - `https://gitpod.io/#https://github.com/WesRoach/hiring-code-challenge-firstName-lastName`
      - If you try to commit, Gitpod will prompt you to fork the repository to your Github account.
    - From a fork within your Github: `https://gitpod.io/#https://github.com/JaneDoe/hiring-code-challenge-jane-doe`

## Dependencies

We will run your code in an environment with the following dependencies.

```bash
python >= 3.8
pyspark >= 3.1.1
java # v11+
pytest

# dendri provides access to a pre-configured Spark Session
# You -must- utilize the Spark Session available within this package
# Exercise prompts explain how to create a Spark Session
dendri
```

## Personal Development Environment

Setting up the development environment yourself depends on your platform. The following are general steps.

1. Use Python 3.8+
1. `pip install pyspark>=3.1.1 black flake8 jupyter jupytext pytest dendri`
1. Install Spark: [https://spark.apache.org/downloads.html](https://spark.apache.org/downloads.html)
1. Verify your `JAVA_HOME` environment variable.
