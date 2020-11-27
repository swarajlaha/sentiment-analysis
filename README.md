# sentiment-analysis
A Product Review Analysis App to Determine the Sentiment of Reviews, using AWS.

### Description
The application processes user/customer reviews, taken from a _.csv_ file and categorises the review sentiment as- 'Positive', 'Negative' or 'Neutral', based on certain keywords, that can be found in the review, using AWS Comprehend, which is a service that uses machine learning to find insights and relationships in text and returns the sentiment accordingly.

Further, an email notification is triggered using AWS SNS, to a specified mail id, when the sentiment happens to be 'Negative' and all the sentiment data is stored in AWS DynamoDB, for reference.

The entire process is managed by an AWS Step Function, which consists of Lambda functions, that trigger various other AWS Services like- Comprehend, SNS, DynamoDB. The State Function is in turn triggered by a Lambda function, which occurs when an S3 PUT Event takes place, i.e., when a _.csv_ file, consisting of customer sentiment data is uploaded to S3. 

Once the file is uploaded to S3, the Step Function runs and generates the sentiment of the review, which then carries out the task depending on the sentiment result.


![workflow](https://user-images.githubusercontent.com/26769575/100451924-32e9fb00-30de-11eb-98f6-8f4b32c129fd.JPG)
_Workflow Diagram of the App_


![step-function](https://user-images.githubusercontent.com/26769575/100452055-6f1d5b80-30de-11eb-80f5-97d36985ff4a.JPG)

_Step Function depicting the Process_


![csv-file](https://user-images.githubusercontent.com/26769575/100453039-4f873280-30e0-11eb-968b-aec21411e2dd.JPG)

_CSV file uploaded in S3_


![dynamodb-review](https://user-images.githubusercontent.com/26769575/100452403-13070700-30df-11eb-874c-a72e0e6ebaf9.JPG)
_DyanmoDB Table showing Customer Review and Sentiment_


![sns-email](https://user-images.githubusercontent.com/26769575/100453909-dbe62500-30e1-11eb-94f3-163e74fa4c06.JPG)
_Email received for Negative Reviews_



