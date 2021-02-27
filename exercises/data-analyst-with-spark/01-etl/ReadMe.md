# CSV ETL to Parquet

- Utilize `spark_getOrCreate` for a PySpark Session. Example provided in `starter_file.py`.
- Write Python / PySpark.
  - Develop a local module such as `mod.py` if necessary.
  - Develop any number of scripts and modules to address the problem.
- Include instructions detailing how to run your code.
- Do not commit Parquet data.

## Goal

- Create four Parquet outputs within the `./parquet/` directory.
   1. `claims.bronze.parquet`
   2. `claims.gold.parquet`
   3. `beneficiary_demographics.bronze.parquet`
   4. `beneficiary_demographics.gold.parquet`
- `bronze` tables store source data in Parquet with minimal (ideally zero) modifications.
- `gold` tables store the final version of data ready for downstream analysts.

## Bronze Tables

1. Read CSV data from `./csv/` into Parquet files within the `./parquet/` directory.
    - Parquet files keep the same base name as their CSV source but with the word "bronze" inserted.
        - Example: `./csv/claims.csv` will be read into `./parquet/claims.bronze.parquet`.
    - Modify data as little as possible.
    - Keep original column names.

## Gold Tables

1. Transform each column as follows:
    - Convert `TimestampType` to `DateType`.
    - Cast Numeric columns to the smallest type appropriate for the column (Short, Long, Float, etc). Reference the tables below for hints.
    - Transcode `gender_cd` which contains values 1, 2, and 3 to "M", "F", and "U" representing Male, Female, and Unknown, respectively. The value 1 maps to "M", 2 to "F", and 3 to "U".
1. Write the transformed data to disk using the Parquet format and insert the word "gold" into the name.
    - Example: The gold version of `./parquet/claims.bronze.parquet` will be written to disk as `./parquet/claims.gold.parquet`.


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
