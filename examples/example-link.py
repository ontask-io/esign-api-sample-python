# Get your free API Key at: https://www.ontask.io/solutions/ontask-api/
# Full OnTask API Documentation: https://docs.ontask.io/#overview

import requests
import json

apiKey = 'INSERT-API-KEY'
emailFinalized = 'completed@example.com'

print('\n##### Example Starting #####')

# Upload the file and get a documentid to pass to create a signature endpoint
# https://docs.ontask.io/#upload
url = "https://app.ontask.io/api/v2/documents"
data = open('sample-files/sample.pdf', 'rb').read()

requestHeadersDocument = {
  'Authorization' : apiKey,
  'Content-Type' : 'application/pdf'
}

response = requests.post(url=url, headers=requestHeadersDocument, data=data)
documentid = response.json()['documentId']

print('\nUploaded sample file and received a documentId of ' + documentid)

# Call signature to and create and start signature process
# https://docs.ontask.io/#signature-api
url = 'https://app.ontask.io/api/v2/signatures'

requestBody = {
                "documents": [ { "documentId": documentid } ] ,
                "testMode": True,
                "signers": [
                    {
                    "label": "John Smith",
                    "contactMethod": [
                        {
                        "type": "link"
                        }
                    ]
                    }
                ],
                "onSignaturesFinalized": [
                    {
                    "type": "email",
                    "email": emailFinalized
                    }
                ]
            }

requestHeadersSignature = {
  'Authorization' : apiKey,
  'Content-Type' : 'application/json'
}

response = requests.post(url=url, headers=requestHeadersSignature, json=requestBody)

print('\nURL for signer John Smith: (Follow URL to complete signature process)')
print(response.json()['signers'][0]['contactMethod'][0]['taskUrl'] + '\n')
print('Once signed the final document will be sent to: ' + emailFinalized + '\n')
print('##### Example Complete #####\n')