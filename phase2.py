from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator

def initialize_spark():
    """Initialize Spark session."""
    return SparkSession.builder \
        .appName("MusicRecommendation") \
        .config("spark.mongodb.input.uri", "mongodb://localhost:27017/db.collection") \
        .getOrCreate()

def load_data(spark):
    """Load data from MongoDB into Spark DataFrame."""
    return spark.read.format("mongo").load()

def convert_to_numerical(df):
    """Convert categorical variables to numerical values."""
    indexer = StringIndexer(inputCol="genre", outputCol="genreIndex")
    return indexer.fit(df).transform(df)

def split_data(df):
    """Split data into training and testing sets."""
    return df.randomSplit([0.6, 0.4])

def train_model(training_data):
    """Train ALS model."""
    als = ALS(maxIter=10, regParam=0.01, userCol="user_id", itemCol="song_id", ratingCol="rating",
              coldStartStrategy="drop")
    return als.fit(training_data)

def evaluate_model(model, testing_data):
    """Make predictions and evaluate model."""
    predictions = model.transform(testing_data)
    evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
    rmse = evaluator.evaluate(predictions)
    print("Root Mean Squared Error (RMSE) = " + str(rmse))

def main():
    """Main function."""
    # Initialize Spark session
    spark = initialize_spark()
    
    # Load data
    df = load_data(spark)
    
    # Convert categorical variables to numerical values
    indexed_df = convert_to_numerical(df)
    
    # Split data into training and testing sets
    training_data, testing_data = split_data(indexed_df)
    
    # Train ALS model
    model = train_model(training_data)
    
    # Evaluate model
    evaluate_model(model, testing_data)

if __name__ == "__main__":
    main()
