
## Description

Create S3 VPC endpoint for NAT/NAT Gateway multiAZ public/private VPC

## Parameters

 * **PrivateRouteTableAZ1** - Route table for private subnet in AZ1
 * **PrivateRouteTableAZ2** - Route table for private subnet in AZ2
 * **PublicRouteTable** - Route table for public subnets
 * **S3Bucket** - S3Bucket containing CloudFormation templates, also used for S3 VPC Endpoint policy
 * **VPC** - Object ID of VPC

## Resources

 * **S3Endpoint** - `AWS::EC2::VPCEndpoint`

