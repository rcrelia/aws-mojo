
## Description

CloudFormation template for creating an EC2 instance consumed by a Lambda-based AMI generator

## Parameters

 * **InstanceName** - Name of EC2 instance for AMI creation
 * **InstanceType** - EC2 instance type (Default: t2.micro)

## Resources

 * **AMI** - `Custom::AMI`
 * **AMICreate** - `AWS::CloudFormation::WaitCondition`
 * **AMIFunction** - `AWS::Lambda::Function`
 * **Ec2Function** - `AWS::EC2::Instance`
 * **LambdaExecutionRole** - `AWS::IAM::Role`
