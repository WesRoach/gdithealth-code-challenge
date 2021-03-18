FROM gitpod/workspace-full:latest

USER gitpod

RUN pip3 install pyspark>=3.0.0 pytest jupyter jupytext black flake8 dendri
