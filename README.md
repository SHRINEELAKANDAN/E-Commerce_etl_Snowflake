# E-Commerce_etl_Snowflake

A batch and incremental sales-data pipeline built with Snowflake and Python.

## Workflow
1. CSV sales files are placed in a Snowflake stage.
2. Snowpipe loads data into the RAW.SALES table.
3. A Snowflake stream identifies newly inserted rows.
4. Tasks process and merge incremental records into processed tables.
5. An analytics table calculates sales amount and supports revenue analysis.
6. Python/Pandas scripts perform basic data cleaning and transformations.

## Tech Stack
- Snowflake
- Snowpipe
- Streams and Tasks
- SQL
- Python
- Pandas

## Data Quality Checks
- Duplicate order detection
- Invalid price detection
- Missing customer ID detection