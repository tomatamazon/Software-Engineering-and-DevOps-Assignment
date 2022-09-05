# This function gets the database keys (.pem file)
def get_keys(boto3, base64, ClientError):
    secret_name = "arn:aws:secretsmanager:us-east-1:715503964473:secret:db-keys.pem-k8P1gV"
    region_name = "us-east-1"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager cannot decrypt the protected secret using the provided KMS key.
            raise "Decryption Error. Secrets Manager cannot decrypt the protected secret using the provided KMS key."
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            raise "Internal Service Error. There is an error on the server side. Please try again later."
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            raise "Invalid Parameter. You provided an invalid value for a parameter."
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            raise "Invalid Request. You provided a parameter value that is not valid for the current state of the resource."
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # The resource requested cannot be found.
            raise "Resource Not Found. The resource that you requested could not be found."
    else:
        # Decrypts secret using the associated KMS key.
        if 'SecretString' in get_secret_value_response:
            return get_secret_value_response['SecretString']
        else:
            return base64.b64decode(get_secret_value_response['SecretBinary'])
