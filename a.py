from pyspark.sql import SparkSession
from pyspark.sql.functions import col, desc
import findspark

# findspark.init()
spark = SparkSession.builder.appName("sparksql").getOrCreate()
print( dir( spark))



print("DONE")