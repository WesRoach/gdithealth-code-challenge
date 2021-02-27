# CSV ETL to Parquet

- No additional packaging should be installed.
- Utilize `spark_getOrCreate` for a PySpark Session. An example is provided in `starter_file.py`
- Develop any Python / PySpark code which accomplishes the objectives listed below.
  - You may develop a local module such as the provided `mod.py` if necessary.
  - You're free to develop any number of scripts and modules and address the problem to the best of your judgement.
- Include instructions detailing how to run your code.
- Only commit your code.

## Goal

- Create four `parquet` outputs within the `parquet` directory.
   1. `claims.bronze.parquet`
   2. `claims.gold.parquet`
   3. `beneficiary_demographics.bronze.parquet`
   4. `beneficiary_demographics.gold.parquet`
- `bronze` tables seek to maintain as close to source formatting as possible, but stored in the `parquet` format.
- `gold` tables contain the final version of the data ready for downstream analysts.

## Bronze Tables

1. Read CSV data from `./csv/` into `parquet` files within `./parquet/`.
    - The `parquet` files should maintain the same base name as their CSV counterparts, but with the word "bronze" inserted.
        - Example: `./csv/claims.csv` will be read into `./parquet/claims.bronze.parquet`.
    - Maintain the same column names.
    - Maintain as close to the raw data as possbile (don't cast values, etc)

## Gold Tables

1. Transform each column as follows:
    - `TimestampType` should be convered to `DateType`.
    - Numeric columns should be encoded in the smallest primitive type appropriate for the column (Short, Long, Double, etc). Reference the tables below for hints.
    - Transcode the `gender_cd` column containing values 1, 2, and 3 to "M", "F", and "U" representing Male, Female, and Unknown, respectively. The value 1 maps to "M", 2 to "F", and 3 to "U".
1. Write the transformed data to `parquet` and insert the word "gold".
    - Example: `./parquet/claims.bronze.parquet` transformed would be written as `./parquet/claims.gold.parquet`.


| Claims Columns | Basic Type | Largest Possible Value |
|-|-|-|
|patient_id|String|N/A|
|claim_id|String|N/A|
|line_num|Numeric|99|
|diagnosis_cd|String|N/A|
|procedure_cd|String|N/A|
|procedure_dt|Date|N/A|
|procedure_cost|Numeric|9999999999.99|
|allowed_qty|Numeric|32767|


| Beneficiary Demographics Columns | Basic Type | Largest Possible Value |
|-|-|-|
|patient_id|String|N/A|
|birth_dt|Date|N/A|
|gender_cd|String|N/A|
