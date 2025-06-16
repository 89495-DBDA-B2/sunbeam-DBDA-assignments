# Q.4 Count number of movie ratings per year. Hint: convert time column to TIMESTAMP using from_unixtime().


from pyspark.sql import SparkSession
from pyspark.sql.functions import from_unixtime, year

# Initialize Spark session
spark = SparkSession.builder.appName("RatingsPerYear").getOrCreate()

# Load ratings.csv into DataFrame
ratings_df = spark.read.option("header", True).csv("ratings.csv")

# Convert timestamp column from string to integer for processing
ratings_df = ratings_df.withColumn("timestamp", ratings_df["timestamp"].cast("long"))

# Extract year from timestamp and count ratings per year
ratings_per_year = (
    ratings_df
    .withColumn("year", year(from_unixtime("timestamp")))
    .groupBy("year")
    .count()
    .orderBy("year")
)

# Show result
ratings_per_year.show()
