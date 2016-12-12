
## Description

Create a VPC with public/private subnets in two AZs using NAT gateways in each public zone for private instance outbound Internet connectivity.

#### Metadata

 * **AWS::CloudFormation::Interface**: {ParameterGroups': [{Parameters': [Environment', RemoteCIDR', ConfigS3Endpoint', S3Bucket', TemplatePath', VpcCIDR', AvZone1', AvZone2', PublicSubnetAZ1', PublicSubnetAZ2', PrivateSubnetAZ1', PrivateSubnetAZ2'], Label': {default': VPC Configuration'}}], ParameterLabels': {Environment': {default': Which environment will use this VPC? (used in various tags and resource names)'}, VpcCIDR': {default': What is the CIDR block for this VPC?'}}}

## Parameters

 * **AvZone1** - First AZ to use for subnets, etc.
  * Default: `us-east-1a`
  * Constraint: `Must be a valid AZ - # aws ec2 describe-availability-zones`
 * **AvZone2** - Second AZ to use for subnets, etc.
  * Default: `us-east-1c`
  * Constraint: `Must be a valid AZ - # aws ec2 describe-availability-zones`
 * **ConfigS3Endpoint** - Select yes to create a VPC endpoint to privatize access to S3 resources. Be sure to review implications first.
  * Default: `no`
 * **Environment** - Used for miscellaneous object names and tags
  * Default: `dev`
 * **PrivateSubnetAZ1** - IP Address range for AZ1 private subnet
  * Default: `10.0.1.0/24`
  * Constraint: `Valid IP CIDR block range - x.x.x.x/x.`
 * **PrivateSubnetAZ2** - IP Address range for AZ2 private subnet
  * Default: `10.0.3.0/24`
  * Constraint: `Valid IP CIDR block range - x.x.x.x/x.`
 * **PublicSubnetAZ1** - IP Address range for AZ1 public subnet
  * Default: `10.0.0.0/24`
  * Constraint: `Valid IP CIDR block range - x.x.x.x/x.`
 * **PublicSubnetAZ2** - IP Address range for AZ2 public subnet
  * Default: `10.0.2.0/24`
  * Constraint: `Valid IP CIDR block range - x.x.x.x/x.`
 * **RemoteCIDR** - CIDR IP range allowed to login remotely to the VPC, ideally your VPN/ISP netblock
  * Constraint: `must be a valid CIDR range of the form x.x.x.x/x.`
 * **S3Bucket** - S3Bucket containing CloudFormation templates, also used for S3 VPC Endpoint policy
  * Default: `myS3bucket`
 * **TemplatePath** - Path to CloudFormation templates (relative to top level of S3Bucket parameter)
  * Default: `/cloudformation_templates/`
 * **VpcCIDR** - IP Address range for the VPC
  * Default: `10.0.0.0/16`
  * Constraint: `Valid IP CIDR range as x.x.x.x/x.`

## Conditions

 * **ConfigureS3Endpoint** - `{Fn::Equals': [{Ref': ConfigS3Endpoint'}, yes']}`

## Mappings

 * **PrefixListId**:
  * `(ap-south-1', {s3': pl-78a54011'})`
  * `(us-east-1', {s3': pl-63a5400a'})`
  * `(us-east-2', {s3': pl-7ba54012'})`
  * `(ap-southeast-2', {s3': pl-6ca54005'})`
  * `(ap-northeast-1', {s3': pl-61a54008'})`
  * `(sa-east-1', {s3': pl-6aa54003'})`
  * `(ap-southeast-1', {s3': pl-6fa54006'})`
  * `(ap-northeast-2', {s3': pl-78a54011'})`
  * `(us-west-2', {s3': pl-68a54001'})`
  * `(us-west-1', {s3': pl-6ba54002'})`
  * `(eu-central-1', {s3': pl-6ea54007'})`
  * `(eu-west-1', {s3': pl-6da54004'})`

## Resources

 * **IgwAttachment** - `AWS::EC2::VPCGatewayAttachment`
 * **InetGw** - `AWS::EC2::InternetGateway`
 * **InstanceSecurityGroupStack** - `AWS::CloudFormation::Stack`
 * **NatGatewayAZ1** - `AWS::EC2::NatGateway`
 * **NatGatewayAZ2** - `AWS::EC2::NatGateway`
 * **NatGatewayEipAZ1** - `AWS::EC2::EIP`
 * **NatGatewayEipAZ2** - `AWS::EC2::EIP`
 * **NetworkAclStack** - `AWS::CloudFormation::Stack`
 * **PrivRouteTableAssocAZ1** - `AWS::EC2::SubnetRouteTableAssociation`
 * **PrivRouteTableAssocAZ2** - `AWS::EC2::SubnetRouteTableAssociation`
 * **PrivSubnetAZ1** - `AWS::EC2::Subnet`
 * **PrivSubnetAZ2** - `AWS::EC2::Subnet`
 * **PrivateRouteAZ1** - `AWS::EC2::Route`
 * **PrivateRouteAZ2** - `AWS::EC2::Route`
 * **PrivateRouteTableAZ1** - `AWS::EC2::RouteTable`
 * **PrivateRouteTableAZ2** - `AWS::EC2::RouteTable`
 * **PubRouteTableAssocAZ1** - `AWS::EC2::SubnetRouteTableAssociation`
 * **PubRouteTableAssocAZ2** - `AWS::EC2::SubnetRouteTableAssociation`
 * **PubSubnetAZ1** - `AWS::EC2::Subnet`
 * **PubSubnetAZ2** - `AWS::EC2::Subnet`
 * **PublicRoute** - `AWS::EC2::Route`
 * **PublicRouteTable** - `AWS::EC2::RouteTable`
 * **RdsPrivateSubnetGroup** - `AWS::RDS::DBSubnetGroup`
 * **S3EndpointStack** - `AWS::CloudFormation::Stack`
 * **VPC** - `AWS::EC2::VPC`

