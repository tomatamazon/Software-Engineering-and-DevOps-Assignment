# This function gets the database password (.txt file)
def get_pass(boto3, base64, ClientError):
    secret_name = "db-pass.txt"
    region_name = "us-east-1"

    session = boto3.session.Session()
    client = session.client (
        service_name='secretsmanager',
        region_name=region_name
    )

    print("Reaches here: 1")

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager cannot decrypt the protected secret using the provided KMS key.
            print("Decryption Error. Secrets Manager cannot decrypt the protected secret using the provided KMS key.")
            raise "Decryption Error. Secrets Manager cannot decrypt the protected secret using the provided KMS key."
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            print("Internal Service Error. There is an error on the server side. Please try again later.")
            raise "Internal Service Error. There is an error on the server side. Please try again later."
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            print("Invalid Parameter. You provided an invalid value for a parameter.")
            raise "Invalid Parameter. You provided an invalid value for a parameter."
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            print("Invalid Request. You provided a parameter value that is not valid for the current state of the resource.")
            raise "Invalid Request. You provided a parameter value that is not valid for the current state of the resource."
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # The resource requested cannot be found.
            print("Resource Not Found. The resource that you requested could not be found.")
            raise "Resource Not Found. The resource that you requested could not be found."
    else:
        # Decrypts secret using the associated KMS key.
        if 'SecretString' in get_secret_value_response:
            print("Success here: 2")
            secret = get_secret_value_response['SecretString']
            return secret
        else:
            print("Success here: 3")
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            return decoded_binary_secret