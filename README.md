# Data Migration Using AWS-Cloud-Development-Kit


![Architecture](image/architecture.webp)

## Requirements
- AWS CLI:
    - curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
    - sudo installer -pkg ./AWSCLIV2.pkg -target /
    - [Link](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- Node.js: 
    - [Link](https://radixweb.com/blog/installing-npm-and-nodejs-on-windows-and-mac#homebrew)
- AWS CDK:
    - [Link](https://towardsthecloud.com/install-aws-cdk)


python3 -m venv venv
source venv/bin/activate


## set environment variables


## To run the code
- Clone this repository
- `cd currency/cdk`
- `source .venv/bin/activate`
- `pip install -r requirements.txt`
- `pip install aws-cdk.aws-glue-alpha`
- `cdk deploy`
- `cd ..`
- `cd currencies_generator`
- `python currencies_generator.py`
- Check your s3 bucket
- Connect to your s3 bucket to your Athena
- run the queries in the `athena_queries`
- cdk destroy

## In case the cdk is drifting, run the following command
`aws cloudformation delete-stack --stack-name CDKToolkit`

`cdk bootstrap`
- [Link](https://stackoverflow.com/questions/71280758/aws-cdk-bootstrap-itself-broken/71283964#71283964)
