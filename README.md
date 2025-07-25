# etl-pipeline-cicd

This CICD demo contains source code for a AWS severless ETL pipeline including a Lambda function and a Glue ETL job. A Step Function orchestrates the Lambda Function and Glue ETL job. The ETL pipeline is automatically redeployed when any change is pushed to the main branch.

The business logic is to move data from raw (Bronze layer) to rawplus (Silver layer), and then conduct Spark transformation on rawplus and load the transformed data to a Glue table (Gold layer) for interactive analytics using Athena, Redshift Spectrum or Dremio.

