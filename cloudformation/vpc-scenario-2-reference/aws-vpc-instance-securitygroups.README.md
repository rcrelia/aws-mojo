
## Description

Create security groups for instances in public/private VPC

## Parameters

 * **Environment** - Used for miscellaneous object names and tags
 * **RemoteCIDR** - CIDR IP range allowed to remotely connect to the VPC, ideally your VPN/ISP netblock
  * Constraint: `Valid IP CIDR block range - x.x.x.x/x.`
 * **VPC** - Object ID of VPC
 * **VpcCIDR** - IP Address range for the VPC

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

 * **PrivInstSGEgressGlobalHttp** - `AWS::EC2::SecurityGroupEgress`
 * **PrivInstSGEgressGlobalHttps** - `AWS::EC2::SecurityGroupEgress`
 * **PrivInstSGEgressS3endpoint** - `AWS::EC2::SecurityGroupEgress`
 * **PrivInstSGEgressSsh** - `AWS::EC2::SecurityGroupEgress`
 * **PrivInstSGIngressHttp** - `AWS::EC2::SecurityGroupIngress`
 * **PrivInstSGIngressHttps** - `AWS::EC2::SecurityGroupIngress`
 * **PrivInstSGIngressMysql** - `AWS::EC2::SecurityGroupIngress`
 * **PrivInstSGIngressSsh** - `AWS::EC2::SecurityGroupIngress`
 * **PrivInstSecurityGroup** - `AWS::EC2::SecurityGroup`
 * **PubInstSGEgressGlobalHttp** - `AWS::EC2::SecurityGroupEgress`
 * **PubInstSGEgressGlobalHttps** - `AWS::EC2::SecurityGroupEgress`
 * **PubInstSGEgressMysql** - `AWS::EC2::SecurityGroupEgress`
 * **PubInstSGEgressS3endpoint** - `AWS::EC2::SecurityGroupEgress`
 * **PubInstSGEgressSsh** - `AWS::EC2::SecurityGroupEgress`
 * **PubInstSGIngressHttp** - `AWS::EC2::SecurityGroupIngress`
 * **PubInstSGIngressHttps** - `AWS::EC2::SecurityGroupIngress`
 * **PubInstSGIngressMysql** - `AWS::EC2::SecurityGroupIngress`
 * **PubInstSGIngressSsh** - `AWS::EC2::SecurityGroupIngress`
 * **PubInstSecurityGroup** - `AWS::EC2::SecurityGroup`

