# Designing a Function to Operate on PySpark DataFrames

Your task is to update the stub `.py` file in this directory with your submission.

## 02_functional_analysis.py

Using the provided DataFrames, complete the `agg_age_by_cond` function. For a given diagnosis and visit type, `agg_age_by_cond` should return a new DataFrame that counts the number of unique patients and claims per age and claim status. Age should be calculated as of the date of service on the claim. Below are two examples of the desired output:

### Example 1

| diagnosis | visit_type | age | claim_status | patients | claims |
| --------- | ---------- | --- | ------------ | -------- | ------ |
| Asthma    | IP         | 18  | P            | 1        | 1      |

### Example 2

| diagnosis | visit_type | age | claim_status | patients | claims |
| --------- | ---------- | --- | ------------ | -------- | ------ |
| URI       | ED         | 17  | P            | 1        | 1      |
| URI       | ED         | 18  | P            | 1        | 1      |
