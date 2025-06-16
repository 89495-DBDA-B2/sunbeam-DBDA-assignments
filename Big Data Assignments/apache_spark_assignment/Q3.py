# Q.3 Find deptwise total sal from emp.csv and dept.csv. Print dname and total sal. Hint: use join()


from pyspark.sql import SparkSession
from pyspark.sql.functions import sum  # Import the sum function

# Create Spark session
spark = SparkSession.builder.appName("third").getOrCreate()

# Load emp.csv
emp_df = spark.read.csv("emp.csv", header=False, inferSchema=True)
emp_columns = ["EMPNO", "ENAME", "JOB", "MGR", "HIREDATE", "SAL", "COMM", "DEPTNO"]
emp_df = emp_df.toDF(*emp_columns)

# Load dept.csv
dept_df = spark.read.csv("dept.csv", header=False, inferSchema=True)
dept_columns = ["DEPTNO", "DNAME", "LOC"]
dept_df = dept_df.toDF(*dept_columns)

# Join on DEPTNO
joined_df = emp_df.join(dept_df, on="DEPTNO", how="inner")

# Group by DNAME and calculate total salary
result_df = joined_df.groupBy("DNAME").agg(sum("SAL").alias("TOTAL_SAL"))

# Show result sorted by DNAME
result_df.orderBy("DNAME").show(truncate=False)
