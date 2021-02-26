FROM gitpod/workspace-full:latest

USER gitpod

RUN pip3 install pyspark pytest jupyter jupytext black flake8
