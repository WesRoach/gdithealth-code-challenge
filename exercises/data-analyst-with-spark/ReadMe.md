# Overview

## PySpark Useful Links

[https://spark.apache.org/docs/latest/sql-getting-started.html](https://spark.apache.org/docs/latest/sql-getting-started.html)

[http://spark.apache.org/docs/latest/api/python/pyspark.sql.html](http://spark.apache.org/docs/latest/api/python/pyspark.sql.html)

## PySpark Session

You must use the spark session returned from `spark_getOrCreate()` as follows:

```python
from pysoma.utils import spark_getOrCreate

spark = spark_getOrCreate()
```

## Jupyter

The Gitpod based environment comes with a running Jupyter server if you would like to use that system.

We utilize a Jupyter extension, `jupytext`, which renders plain `.py` files as Jupyer notebooks. Your final submission should avoid committing JSON files (the native storage format for Jupyter).
