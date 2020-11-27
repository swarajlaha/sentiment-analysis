#Lambda function to invoke the Step Function, whenever a '.csv' file is uploaded in the S3 bucket, that triggers an S3 event.

import json
import boto3
import pprint

#initialize
pp = pprint.PrettyPrinter(indent=4)

def lambda_handler(event, context):
    '''
    triggers a step function from the S3 landing event, 
    passing along the S3 file info
    '''
    
    #Fallback tests for initializations outside scope
    try:
        pp
    except NameError:
        pp = pprint.PrettyPrinter(indent=4)

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']

    
    input= {
            'bucket_name': 'sentimentanalysiss3',
            'file_key': 'sentimentdata.csv'
        }
        
    stepFunction = boto3.client('stepfunctions')
    response = stepFunction.start_execution(
        stateMachineArn='arn:aws:states:xx-xxxxx:xxxxxxxxxxx:execution:SentimentAnalysis-SM:c583d60d-1315-953a-db0b-xxxxxxxx',
        input = json.dumps(input, indent=4)
    )
    
    return pp.pprint(response)