from datetime import date

from pysoma.utils import spark_getOrCreate

# This creates a running Spark Session
# There is no need to create a new Spark Session
spark = spark_getOrCreate()

# Create a DataFrame of sample healthcare claims
# Patient ID is a unique patient identifier
# Claim ID is a system assigned number for each claim submitted by a healthcare provider
# Claim Status is "P" for a paid claim or "D" for a denied claim
# Service Date is the date of the service for the claim
# Diagnosis is a text category of the patient's diagnosis
# Visit Type is "IP" for an inpatient stay, "OP" for an outpatient visit, or "ED" for
# an emergency department visit
claims = spark.createDataFrame(
    [
        ("01", "1001", "P", date.fromisoformat("2019-01-01"), "Diabetes", "OP"),
        ("01", "1002", "P", date.fromisoformat("2019-04-06"), "Diabetes", "OP"),
        ("01", "1003", "D", date.fromisoformat("2019-07-09"), "CHF", "IP"),
        ("02", "1004", "P", date.fromisoformat("2017-06-15"), "Pregnant", "OP"),
        ("03", "1005", "P", date.fromisoformat("2018-11-23"), "Asthma", "OP"),
        ("03", "1006", "D", date.fromisoformat("2019-01-08"), "COPD", "ED"),
        ("03", "1007", "P", date.fromisoformat("2019-01-08"), "Asthma", "IP"),
        ("03", "1008", "P", date.fromisoformat("2019-10-23"), "URI", "ED"),
        ("03", "1009", "P", date.fromisoformat("2020-09-29"), "Asthma", "OP"),
        ("04", "1010", "P", date.fromisoformat("2019-02-17"), "Bipolar", "IP"),
        ("04", "1011", "D", date.fromisoformat("2019-03-16"), "Schizophrenia", "OP"),
        ("05", "1012", "P", date.fromisoformat("2017-11-12"), "Diabetes", "OP"),
        ("06", "1013", "P", date.fromisoformat("2018-08-22"), "Bipolar", "OP"),
        ("06", "1014", "D", date.fromisoformat("2019-08-22"), "Bipolar", "ED"),
        ("07", "1015", "P", date.fromisoformat("2016-04-03"), "URI", "ED"),
        ("07", "1016", "P", date.fromisoformat("2016-07-01"), "Asthma", "OP"),
        ("08", "1017", "D", date.fromisoformat("2018-03-09"), "Pregnant", "OP"),
        ("08", "1018", "P", date.fromisoformat("2018-03-09"), "Diabetes", "OP"),
        ("09", "1019", "P", date.fromisoformat("2019-12-05"), "Asthma", "ED"),
        ("10", "1020", "D", date.fromisoformat("2021-01-02"), "CHF", "IP"),
    ],
    ["patient_id", "claim_id", "claim_status", "service_dt", "diagnosis", "visit_type"],
)

# Create a DataFrame of sample patient demographics
# Patient ID is a unique patient identifier
# Birth Date is the patient's date of birth
# Gender is "M" for male or "F" for female
demographic = spark.createDataFrame(
    [
        ("01", date.fromisoformat("1980-02-04"), "M"),
        ("02", date.fromisoformat("1994-08-16"), "F"),
        ("03", date.fromisoformat("2000-12-14"), "F"),
        ("04", date.fromisoformat("2005-06-30"), "M"),
        ("05", date.fromisoformat("2002-04-09"), "F"),
        ("06", date.fromisoformat("1992-09-23"), "M"),
        ("07", date.fromisoformat("1998-10-01"), "F"),
        ("08", date.fromisoformat("1995-03-18"), "F"),
        ("09", date.fromisoformat("2010-10-10"), "F"),
        ("10", date.fromisoformat("2008-07-05"), "M"),
        ("11", date.fromisoformat("2004-03-19"), "F"),
        ("12", date.fromisoformat("2001-07-17"), "M"),
    ],
    ["patient_id", "birth_dt", "gender"],
)


# Complete the following function
# Refer to the ReadMe.md in this folder for more instructions
def agg_age_by_cond():
    pass
