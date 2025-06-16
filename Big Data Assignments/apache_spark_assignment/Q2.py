# Q.2 Find max sal, min sal, avg sal, total sal per dept per job in emp.csv file.


from pyspark.sql import SparkSession
from pyspark.sql.functions import max, min, avg, sum

# Create Spark session
spark = SparkSession.builder.appName("EmpSalaryStats").getOrCreate()

# Read the emp.csv file
emp_df = spark.read.csv("emp.csv", header=False, inferSchema=True)

# Rename columns for clarity
columns = ["EMPNO", "ENAME", "JOB", "MGR", "HIREDATE", "SAL", "COMM", "DEPTNO"]
emp_df = emp_df.toDF(*columns)

# Perform group by DEPTNO and JOB, and calculate max, min, avg, total salary
result_df = emp_df.groupBy("DEPTNO", "JOB").agg(
    max("SAL").alias("MAX_SAL"),
    min("SAL").alias("MIN_SAL"),
    avg("SAL").alias("AVG_SAL"),
    sum("SAL").alias("TOTAL_SAL")
)

# Show the result
result_df.orderBy("DEPTNO", "JOB").show()
