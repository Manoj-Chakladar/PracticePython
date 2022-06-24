import json

print('Loading Function')

def lambda_handler(event, context):
    #1. Parse out query string parameters
    transactionId = event['queryStringParameters']['transactionId']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['amount']

    print(f"transactionId: {transactionId}")
    print(f"transactionType: {transactionType}")
    print(f"transactionAmount: {transactionAmount}")

    #2. Construct the body of response object
    transactionresponse = {}
    transactionresponse['transactionId'] = transactionId
    transactionresponse['type'] = transactionType
    transactionresponse['amount'] = transactionAmount
    transactionresponse['message'] = "This response is from the lambda"

    #3. Construct HTTP response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = "application/json"
    responseObject['body'] = json.dumps(transactionresponse)

    return responseObject

