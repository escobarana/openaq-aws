# Process current Air Quality in Belgium

## Data Source:
https://registry.opendata.aws/openaq/

## Results:
Real-time view of the current air quality in various cities. 

*Current air quality*: Average of the measurements over the last 3 hours

AWS Resources used: SNS, SQS, Lambda, DynamoDB

Visualisation of final results on a map using Streamlit and Pydeck

## Environment variables:

| Variable                  | Description                                  |
|---------------------------|----------------------------------------------|
| `AWS_REGION_NAME`         | Name of AWS region where DynamoDB is located |
| `AWS_ACCESS_KEY_ID`       | AWS Account access key id                    |
| `AWS_SECRET_ACCESS_KEY`   | AWS Account secret access key                |
