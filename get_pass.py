# This function gets the database password (.txt file)
def get_pass(boto3, base64, ClientError):
    secret_name = "arn:aws:secretsmanager:us-east-1:715503964473:secret:db-pass.txt-z2OmqT"
    region_name = "us-east-1"

    print("Hola 1")

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    print("Hola 2")

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
        print("Hola 3")
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager cannot decrypt the protected secret using the provided KMS key.
            print("e1")
            raise "Decryption Error. Secrets Manager cannot decrypt the protected secret using the provided KMS key."
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            print("e2")
            raise "Internal Service Error. There is an error on the server side. Please try again later."
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            print("e3")
            raise "Invalid Parameter. You provided an invalid value for a parameter."
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            print("e4")
            raise "Invalid Request. You provided a parameter value that is not valid for the current state of the resource."
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # The resource requested cannot be found.
            print("e5")
            raise "Resource Not Found. The resource that you requested could not be found."
    else:
        # Decrypts secret using the associated KMS key.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            print("Hola 4")
            return secret
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            print("Hola 5")
            return decoded_binary_secret