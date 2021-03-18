from datetime import date

from dendri.utils import spark_getOrCreate

# You can add any module code to mod.py and import
from mod import hello_world

# This creates a running Spark Session and is provided as an example.
# Your code must utilize the spark session returned from this function.
spark = spark_getOrCreate()

# Example data created with `spark` held in variable sdf and displayed using sdf.show()
# You're free to remove this file and solve the problem as you see fit
sdf = spark.createDataFrame(
    data=[("001", 1, date.fromisoformat("2020-12-31"))], schema=["id", "num", "dt"]
)
sdf.show()

# This is included as an example of using a local/relative module
hello_world()
