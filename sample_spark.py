from pyspark.sql import SparkSession
import debugpy

# Enable remote debugging
debugpy.listen(("0.0.0.0", 5678))
print("Waiting for debugger attach...")
debugpy.wait_for_client()

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Azure Blob Storage Example") \
    .getOrCreate()

# Create some test data
test_data = [
    (1, "John Doe", 30),
    (2, "Jane Smith", 25),
    (3, "Bob Johnson", 35)
]
columns = ["id", "name", "age"]

# Create a DataFrame
df = spark.createDataFrame(test_data, columns)

# Set a breakpoint here in VS Code
print("About to show the DataFrame...")
# This is a good place to set a breakpoint
df.show()

# Do some transformations
print("Performing transformations...")
# Another good place for a breakpoint
filtered_df = df.filter(df.age > 28)
filtered_df.show()

# Example: Reading from Azure Blob Storage
# Note: Replace these with your actual Azure Storage credentials
storage_account_name = "YOUR_STORAGE_ACCOUNT"
container_name = "YOUR_CONTAINER"
storage_account_key = "YOUR_STORAGE_KEY"

# Configure Spark to use Azure Blob Storage
spark.conf.set(
    f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net",
    storage_account_key
)

# Example path to a file in Azure Blob Storage
azure_path = f"wasbs://{container_name}@{storage_account_name}.blob.core.windows.net/path/to/your/file"

# Set a breakpoint here in VS Code
print("Ready to read data...")

# Example: Read data from Azure Blob Storage
# df = spark.read.csv(azure_path)
# df.show()

df.count()
df.columns

spark.stop() 