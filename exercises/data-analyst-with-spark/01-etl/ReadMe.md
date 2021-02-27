# CSV ETL to Parquet

Update the `.py` files in this directory with any necessary updates.

- Include a local module if you need to share functionality between scripts.

## 01_bronze_tables.py

1. Read CSV data from `./csv` into `parquet` files within `./parquet`.
    - The `parquet` files should maintain the same base name as their CSV counterparts, but with the word "bronze" inserted.
        - Example: `./csv/claims.csv` will be read into `./parquet/claims.bronze.parquet`.
    - Maintain the same column names.
    - Maintain as close to the raw data as possbile (don't cast values, etc)

## 02_gold_tables.py

1. Read the `<filename>.bronze.parquet` files from disk.
1. Transform each column as follows:
    - `TimestampType` should be convered to `DateType`
    - Numeric columns should be encoded in the smallest primitive type appropriate for the column (Short, Long, Double, etc). Reference the tables below for hints.
    - The `gender_cd` column should be transcoded using the following mapping: {1: "M", 2: "F"} mapping the value 1 to "M" for Male and likewise for Female.
1. Write the transformed tables to `parquet`, but replace the word "bronze" with "gold".
    - Example: `claims.bronze.parquet` transformed will be written as `claims.gold.parquet`.
    - Four `parquet` outputs should exist in the end.
        1. `claims.bronze.parquet`
        2. `claims.gold.parquet`
        3. `beneficiary_demographics.bronze.parquet`
        4. `beneficiary_demographics.gold.parquet`


| Claims Columns | Basic Type | Largest Possible Value |
|-|-|-|
|patient_id|String|N/A|
|claim_id|String|N/A|
|line_num|Numeric|99|
|diagnosis_cd|String|N/A|
|procedure_cd|String|N/A|
|procedure_dt|Date|N/A|
|procedure_cost|Numeric|9223372036854775807|
|allowed_amt|Numeric|32767|


| Beneficiary Demographics Columns | Basic Type | Largest Possible Value |
|-|-|-|
|patient_id|String|N/A|
|birth_dt|Date|N/A|
|gender_cd|String|N/A|

## Submitting

- Only commit your code. Do not commit parquet data.

We should be able to run your code by executing:

```bash
python3 01_bronze_tables.py
python3 02_gold_tables.py
```
