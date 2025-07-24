import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import *
from pyspark.sql.types import *

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
args = getResolvedOptions(sys.argv, ['JOB_NAME','input_path','output_path','glue_database','glue_table'])
job.init(args['JOB_NAME'], args)

#Define input and output S3 paths
input_path=args['input_path']
output_path=args['output_path']
database_name = args['glue_database']
table_name = args['glue_table']

# Read data from S3 (assuming CSV format)
df = spark.read.csv(input_path, header=True, inferSchema=True)

# sql transformation
df.createOrReplaceTempView("Superstore_data")
sql='''
    select Category, 
           Sub_Category,
           sum(Sales) as Sales_total,
           sum(Profit) as Profit_total
    from Superstore_data
    group by Category, Sub_Category
    order by Profit_total desc
    '''
df1=spark.sql(sql)
# Write data to S3 as parquet and a glue table
df1.write.option("path", output_path).mode("overwrite").saveAsTable(f"{database_name}.{table_name}")

job.commit()