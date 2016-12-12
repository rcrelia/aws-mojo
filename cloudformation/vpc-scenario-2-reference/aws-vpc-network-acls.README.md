
## Description

Create network ACLs and NACL entries for NAT/NAT Gateway multiAZ public/private VPC

## Parameters

 * **AvZone1** - First AZ to use for subnets, etc.
  * Constraint: `Must be a valid AZ - # aws ec2 describe-availability-zones`
 * **AvZone2** - Second AZ to use for subnets, etc.
  * Constraint: `Must be a valid AZ - # aws ec2 describe-availability-zones`
 * **Environment** - Used for miscellaneous object names and tags
 * **PrivSubnetAZ1** - Object ID for AZ1 private subnet
 * **PrivSubnetAZ2** - Object ID for AZ2 private subnet
 * **PrivateSubnetAZ1** - IP Address range for AZ1 private subnet
  * Constraint: `Valid IP CIDR block range - x.x.x.x/x.`
 * **PrivateSubnetAZ2** - IP Address range for AZ2 private subnet
  * Constraint: `Valid IP CIDR block range - x.x.x.x/x.`
 * **PubSubnetAZ1** - Object ID for AZ1 public subnet
 * **PubSubnetAZ2** - Object ID for AZ2 public subnet
 * **RemoteCIDR** - CIDR IP range allowed to remotely connect to the VPC, ideally your VPN/ISP netblock
  * Constraint: `Valid IP CIDR block range - x.x.x.x/x.`
 * **VPC** - Object ID of VPC
 * **VpcCIDR** - IP Address range for the VPC

## Resources

 * **PrivNetAclInboundEntry100** - `AWS::EC2::NetworkAclEntry`
 * **PrivNetAclInboundEntry110** - `AWS::EC2::NetworkAclEntry`
 * **PrivNetAclInboundEntry120** - `AWS::EC2::NetworkAclEntry`
 * **PrivNetAclInboundEntry140** - `AWS::EC2::NetworkAclEntry`
 * **PrivNetAclInboundEntry150** - `AWS::EC2::NetworkAclEntry`
 * **PrivNetAclOutboundEntry100** - `AWS::EC2::NetworkAclEntry`
 * **PrivNetAclOutboundEntry110** - `AWS::EC2::NetworkAclEntry`
 * **PrivNetAclOutboundEntry120** - `AWS::EC2::NetworkAclEntry`
 * **PrivNetAclOutboundEntry150** - `AWS::EC2::NetworkAclEntry`
 * **PrivNetAclOutboundEntry151** - `AWS::EC2::NetworkAclEntry`
 * **PrivNetAclOutboundEntry160** - `AWS::EC2::NetworkAclEntry`
 * **PrivSubnetNetAclAssocAZ1** - `AWS::EC2::SubnetNetworkAclAssociation`
 * **PrivSubnetNetAclAssocAZ2** - `AWS::EC2::SubnetNetworkAclAssociation`
 * **PrivateNetworkAcl** - `AWS::EC2::NetworkAcl`
 * **PubNetAclInboundEntry100** - `AWS::EC2::NetworkAclEntry`
 * **PubNetAclInboundEntry110** - `AWS::EC2::NetworkAclEntry`
 * **PubNetAclInboundEntry120** - `AWS::EC2::NetworkAclEntry`
 * **PubNetAclInboundEntry140** - `AWS::EC2::NetworkAclEntry`
 * **PubNetAclInboundEntry150** - `AWS::EC2::NetworkAclEntry`
 * **PubNetAclOutboundEntry100** - `AWS::EC2::NetworkAclEntry`
 * **PubNetAclOutboundEntry110** - `AWS::EC2::NetworkAclEntry`
 * **PubNetAclOutboundEntry130** - `AWS::EC2::NetworkAclEntry`
 * **PubNetAclOutboundEntry131** - `AWS::EC2::NetworkAclEntry`
 * **PubNetAclOutboundEntry140** - `AWS::EC2::NetworkAclEntry`
 * **PubNetAclOutboundEntry150** - `AWS::EC2::NetworkAclEntry`
 * **PubNetAclOutboundEntry151** - `AWS::EC2::NetworkAclEntry`
 * **PubNetAclOutboundEntry160** - `AWS::EC2::NetworkAclEntry`
 * **PubSubnetNetAclAssocAZ1** - `AWS::EC2::SubnetNetworkAclAssociation`
 * **PubSubnetNetAclAssocAZ2** - `AWS::EC2::SubnetNetworkAclAssociation`
 * **PublicNetworkAcl** - `AWS::EC2::NetworkAcl`

