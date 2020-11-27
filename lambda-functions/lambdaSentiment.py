#Lambda function that performs analysis on the input, i.e. the feedback on the product, using AWS Comprehend and returns the sentiment of the review.

def lambda_handler(event, context):
    '''
    perform sentiment analysis on the input feedback
    '''
    
    #use comprehend to perform sentiment analysis
    feedback = event['feedback']
    sentiment = client.detect_sentiment(Text=feedback,LanguageCode='en')['Sentiment']
    
    #pass through values
    return {
        'sentiment': sentiment,
        'reviewType': event['reviewType'],
        'reviewID': event['reviewID'],
        'customerID': event['customerID'],
        'productID': event['productID'],
        'feedback': event['feedback'],
    }