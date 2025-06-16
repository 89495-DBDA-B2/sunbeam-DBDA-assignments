# Q.1 Wordcount using Spark Dataframes and find top 10 words (except stopwords). Take file from HDFS/S3. Hint: Use explode() function.



from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, lower, col, regexp_replace
from pyspark.sql.types import StringType

# 1. Create Spark session
spark = SparkSession.builder \
    .appName("WordCountDF") \
    .getOrCreate()

# 2. Load file from HDFS (or replace with S3 path)
df = spark.read.text("hdfs://localhost:9000/user/text1.txt")

# local dir
# df = spark.read.text("/home/sunbeam/BigDataAssignments/apache_spark_assignment/text1.txt")

# 3. Preprocess text:
#    - Remove punctuations
#    - Convert to lowercase
#    - Split into words
words_df = df.select(
    explode(
        split(
            lower(
                regexp_replace(col("value"), r"[^a-zA-Z\s]", "")
            ),
            "\s+"
        )
    ).alias("word")
)

# 4. Remove empty strings
words_df = words_df.filter(col("word") != "")

# 5. Define stopwords
stopwords = ["the", "is", "and", "a", "an", "of", "in", "to", "with", "that", "for", "on", "by", "it", "as", "are", "was", "were", "be", "this", "from", "at", "or", "but"]

# 6. Remove stopwords
filtered_df = words_df.filter(~col("word").isin(stopwords))

# 7. Count and sort
top_words = filtered_df.groupBy("word") \
    .count() \
    .orderBy(col("count").desc()) \
    .limit(10)

# 8. Show result
top_words.show()
