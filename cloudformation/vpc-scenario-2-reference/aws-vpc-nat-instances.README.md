
## Description

Create a VPC with public/private subnets in two AZs using HA-NAT instances in each public zone for private instance outbound Internet connectivity. Also, a S3 VPC Endpoint is created and configured so as to provide a more secure S3 connection (internal to the VPC) as well as reduce NAT traffic.

#### Metadata

 * **AWS::CloudFormation::Interface**: {u'ParameterGroups': [{u'Parameters': [u'Environment', u'ConfigS3Endpoint', u'S3Bucket', u'TemplatePath', u'VpcCIDR', u'AvZone1', u'AvZone2', u'PublicSubnetAZ1', u'PublicSubnetAZ2', u'PrivateSubnetAZ1', u'PrivateSubnetAZ2'], u'Label': {u'default': u'VPC Configuration'}}, {u'Parameters': [u'NatKeyPair', u'NatInstanceType', u'RemoteCIDR', u'NumberOfPings', u'PingTimeout', u'WaitBetweenPings', u'WaitForInstanceStop', u'WaitForInstanceStart'], u'Label': {u'default': u'NAT Instance Configuration'}}], u'ParameterLabels': {u'Environment': {u'default': u'Which environment will use this VPC? (used in various tags and resource names)'}, u'VpcCIDR': {u'default': u'What is the CIDR block for this VPC?'}}}

## Parameters

 * **AvZone1** - First AZ to use for subnets, etc.
  * Default: `us-east-1a`
  * Constraint: `Must be a valid AZ - # aws ec2 describe-availability-zones`
 * **AvZone2** - Second AZ to use for subnets, etc.
  * Default: `us-east-1c`
  * Constraint: `Must be a valid AZ - # aws ec2 describe-availability-zones`
 * **ConfigS3Endpoint** - Select yes to create a VPC endpoint to privatize access to S3 resources
  * Default: `no`
 * **Environment** - Used for miscellaneous object names and tags
  * Default: `dev`
 * **NatInstanceType** - EC2 instance type for NAT
  * Default: `t2.micro`
 * **NatKeyPair** - Existing EC2 key pair for NAT instance
 * **NumberOfPings** - The number of times the health check will ping the alternate NAT Node
  * Default: `3`
 * **PingTimeout** - The number of seconds to wait for each ping response before determining that the ping has failed
  * Default: `2`
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
 * **RemoteCIDR** - CIDR IP range allowed to login to the NAT instance, ideally your VPN/ISP netblock
  * Constraint: `must be a valid CIDR range of the form x.x.x.x/x.`
 * **S3Bucket** - S3Bucket containing CloudFormation templates, also used for S3 VPC Endpoint policy
  * Default: `myS3bucket`
 * **TemplatePath** - Path to CloudFormation templates (relative to top level of S3Bucket parameter)
  * Default: `/cloudformation_templates/`
 * **VpcCIDR** - IP Address range for the VPC
  * Default: `10.0.0.0/16`
  * Constraint: `Valid IP CIDR range as x.x.x.x/x.`
 * **WaitBetweenPings** - The number of seconds to wait between health checks
  * Default: `5`
 * **WaitForInstanceStart** - The number of seconds to wait for alternate NAT Node to restart before resuming health checks again
  * Default: `300`
 * **WaitForInstanceStop** - The number of seconds to wait for alternate NAT Node to stop before attempting to stop it again
  * Default: `60`

## Conditions

 * **ConfigureS3Endpoint** - `{u'Fn::Equals': [{u'Ref': u'ConfigS3Endpoint'}, u'yes']}`

## Mappings

 * **NATRegionAMI**:
  * `(u'us-west-2', {u'AMI': u'ami-a275b1c2'})`
  * `(u'us-east-1', {u'AMI': u'ami-4868ab25'})`
  * `(u'us-east-2', {u'AMI': u'ami-92a6fef7'})`
  * `(u'us-west-1', {u'AMI': u'ami-004b0f60'})`
 * **PrefixListId**:
  * `(u'ap-south-1', {u's3': u'pl-78a54011'})`
  * `(u'us-east-1', {u's3': u'pl-63a5400a'})`
  * `(u'us-east-2', {u's3': u'pl-7ba54012'})`
  * `(u'ap-southeast-2', {u's3': u'pl-6ca54005'})`
  * `(u'ap-northeast-1', {u's3': u'pl-61a54008'})`
  * `(u'sa-east-1', {u's3': u'pl-6aa54003'})`
  * `(u'ap-southeast-1', {u's3': u'pl-6fa54006'})`
  * `(u'ap-northeast-2', {u's3': u'pl-78a54011'})`
  * `(u'us-west-2', {u's3': u'pl-68a54001'})`
  * `(u'us-west-1', {u's3': u'pl-6ba54002'})`
  * `(u'eu-central-1', {u's3': u'pl-6ea54007'})`
  * `(u'eu-west-1', {u's3': u'pl-6da54004'})`

## Resources

 * **IgwAttachment** - `AWS::EC2::VPCGatewayAttachment`
 * **InetGw** - `AWS::EC2::InternetGateway`
 * **InstanceSecurityGroupStack** - `AWS::CloudFormation::Stack`
 * **NatEipAZ1** - `AWS::EC2::EIP`
 * **NatEipAZ2** - `AWS::EC2::EIP`
 * **NatInstanceAZ1** - `AWS::EC2::Instance`
 * **NatInstanceAZ2** - `AWS::EC2::Instance`
 * **NatRole** - `AWS::IAM::Role`
 * **NatRoleProfile** - `AWS::IAM::InstanceProfile`
 * **NatSGEgressGlobalHttp** - `AWS::EC2::SecurityGroupEgress`
 * **NatSGEgressGlobalHttps** - `AWS::EC2::SecurityGroupEgress`
 * **NatSGEgressGlobalIcmp** - `AWS::EC2::SecurityGroupEgress`
 * **NatSGEgressGlobalTcpRemote** - `AWS::EC2::SecurityGroupEgress`
 * **NatSGEgressS3endpoint** - `AWS::EC2::SecurityGroupEgress`
 * **NatSGEgressSsh** - `AWS::EC2::SecurityGroupEgress`
 * **NatSGIngressHttp** - `AWS::EC2::SecurityGroupIngress`
 * **NatSGIngressHttps** - `AWS::EC2::SecurityGroupIngress`
 * **NatSGIngressIcmp** - `AWS::EC2::SecurityGroupIngress`
 * **NatSGIngressSsh** - `AWS::EC2::SecurityGroupIngress`
 * **NatSGIngressSshRemote** - `AWS::EC2::SecurityGroupIngress`
 * **NatSecurityGroup** - `AWS::EC2::SecurityGroup`
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

