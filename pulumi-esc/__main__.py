import pulumi
import pulumi_aws as aws

# Create IAM role for Lambda
lambda_role = aws.iam.Role("lambdaRole",
    assume_role_policy="""{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": "sts:AssumeRole",
                "Principal": {"Service": "lambda.amazonaws.com"},
                "Effect": "Allow",
                "Sid": ""
            }
        ]
    }""")

# Attach AWS Lambda basic execution role policy
role_policy_attachment = aws.iam.RolePolicyAttachment("lambdaPolicyAttach",
    role=lambda_role.name,
    policy_arn="arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
)

# Lambda function code
lambda_function = aws.lambda_.Function("ssm-store-api",
    runtime="python3.12",
    handler="lambda.handler",
    role=lambda_role.arn,
    code=pulumi.AssetArchive({
        ".": pulumi.FileArchive("./lambda_code") 
    })
)

pulumi.export("lambda_function", lambda_function.name) 
