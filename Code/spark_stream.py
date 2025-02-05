from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, LongType
import logging 


def create_spark_session() -> SparkSession:
    spark = (
        SparkSession.builder.appName("PostgreSQL Connection with PySpark")
        .config(
            "spark.jars.packages",
            "org.postgresql:postgresql:42.7.5,org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.4,kafka-clients-3.0.0,commons-pool2-2.12.0,spark-streaming-kafka-0-10-assembly_2.12-3.5.4",

        )
        .getOrCreate()
    )

    logging.info("Spark session created successfully")
    return spark



def create_initial_dataframe(spark_session):
    """
    Reads the streaming data and creates the initial dataframe accordingly.
    """
    try:
        # Gets the streaming data from topic random_names
        df = (
            spark_session.readStream.format("kafka") \
            .option("kafka.bootstrap.servers", "localhost:9092") \
            .option("subscribe", "crypto")   \
            .option("startingOffsets", "earliest") \
            .load()
        )
        logging.info("Initial dataframe created successfully")
    except Exception as e:
        logging.warning(f"Initial dataframe couldn't be created due to exception: {e}")
        raise

    return df



def create_final_dataframe(df):
    """
    Modifies the initial dataframe, and creates the final dataframe.
    """
    # Define the schema
    schema = StructType([
        StructField("id", IntegerType(), False),
        StructField("Timestamp", StringType(), False),
        StructField("Symbol", StringType(), False),
        StructField("Open", FloatType(), True),
        StructField("High", FloatType(), True),
        StructField("Low", FloatType(), True),
        StructField("Close", FloatType(), True),
        StructField("Volume", FloatType(), True)
    ])
    df_out = (
        df.selectExpr("CAST(value AS STRING)")
        .select(from_json(col("value"), schema).alias("data"))
        .select("data.*")
    )
    return df_out


if __name__ == "__main__":
    spark_conn = create_spark_session()
    #spark_df = connect_to_kafka(spark_conn)
    if spark_conn is not None:
        spark_df1 = create_initial_dataframe(spark_conn)
        selection_df = create_final_dataframe(spark_df1)
        def process_batches(df, epoch_id):
            df.write \
                .format("jdbc") \
                .mode('overwrite') \
                .option("url", "jdbc:postgresql://localhost:5432/crypto") \
                .option("dbtable", "bitcoin") \
                .option("user", "postgres") \
                .option("password", "postgres123") \
                .option("driver", "org.postgresql.Driver")\
                .save()
            print("data loaded")

            # Define a query to postgre table: employees
        query = selection_df.writeStream \
                                .foreachBatch(process_batches) \
                                .trigger(once=True) \
                                .start()
        query.awaitTermination()
