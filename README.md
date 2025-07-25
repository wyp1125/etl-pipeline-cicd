# etl-pipeline-cicd

This CICD demo contains source code for a AWS severless ETL pipeline including a Lambda function and a Glue ETL job. A Step Function orchestrates the Lambda Function and Glue ETL job.

The business logic is to move data from raw to rawplus (Bronze layer), and then conduct Spark transformation on rawplus and load the transformed data to a Glue table (Silver layer) for interactive analytics using Athena, Redshift Spectrum or Dremio.
