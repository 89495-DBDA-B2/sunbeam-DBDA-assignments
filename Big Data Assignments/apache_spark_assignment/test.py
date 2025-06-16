from pyspark.sql import SparkSession
from pyspark.sql.functions import max, min, avg, sum

# Create Spark session
spark = SparkSession.builder \
    .appName("EmpDeptJobStats") \
    .master("local[*]") \
    .getOrCreate()

# Define schema matching your data
schema = "id int, name string, job string, mgr int, hire_date date, salary double, comm double, dept_id int"

# Read CSV file (no header) with the schema you gave
df = spark.read \
    .option("header", "false") \
    .schema(schema) \
    .csv(r"/home/sunbeam/BigDataAssignments/apache_spark_assignment/emp.csv")

# Print schema to verify
df.printSchema()

# Group by dept_id and job; compute max, min, avg, and sum of salary
result = df.groupBy("dept_id"
                    ).agg(
    sum("salary").alias("total_salary")
)

# Show the result
result.show(truncate=False)

# Stop Spark session
spark.stop()
