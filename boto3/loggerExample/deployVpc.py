#!/usr/bin/env python
"""
Create a VPC and InternetGateway attachment, along with demonstrating
Python's logging() framework as a debugging aide
"""

import sys
import os
import logging
import logging.config
import boto3
import loggerSetup

loggerSetup.configure()
logger = logging.getLogger(__name__)

# toggle to false for post-run inspection, otherwise remove created objects
Cleanup = True

def session_setup():
    """Setup boto3 session"""
    try:
        session = boto3.session.Session(profile_name='aws-mojo')
        ec2 = session.resource('ec2')
    except Exception as e:
        logger.debug('Error creating EC2 session object:')
        logger.error(e, exc_info=True)
        sys.exit(1)
    else:
        logger.info('EC2 Session object created')
    return ec2

def create_vpc(ec2, vpcCIDR, vpcName):
    """Create the VPC"""
    try:
        vpc = ec2.create_vpc(CidrBlock=vpcCIDR)
        vpc.create_tags(Tags=[{'Key': 'Name', 'Value': vpcName}])
    except Exception as e:
        logger.debug('Error during VPC creation:')
        logger.error(e, exc_info=True)
        sys.exit(1)
    else:
        logger.info('VPC created: %s', vpc.vpc_id)
    return vpc

def delete_vpc(vpc):
    """Delete VPC and contents"""
    try:
        vpc.delete(vpc.vpc_id)
    except Exception as e:
        logger.debug('Error deleting VPC:')
        logger.error(e, exc_info=True)
        sys.exit(1)
    else:
        logger.info('VPC removed: %s', vpc.vpc_id)

def create_igw(ec2, vpc):
    """Create the Internet gateway for the VPC"""
    try:
        igw = ec2.create_internet_gateway()
        igw.attach_to_vpc(VpcId=vpc.vpc_id)
    except Exception as e:
        logger.debug('Error during IGW creation:')
        logger.error(e, exc_info=True)
        if Cleanup:
            delete_vpc(vpc)
        sys.exit(1)
    else:
        logger.info('Internet gateway created: %s', igw.internet_gateway_id)
    return igw

def delete_igw(vpc, igw):
    """Delete Internet Gateway"""
    try:
        igw.detach_from_vpc(VpcId=vpc.vpc_id)
        igw.delete()
    except Exception as e:
        logger.debug('Error deleting IGW:')
        logger.error(e, exc_info=True)
        sys.exit(1)
    else:
        logger.info("Internet gateway %s has been deleted!", igw.internet_gateway_id)

def main():
    """Create a VPC with Internet Gateway"""

    scriptName = str(os.path.basename(sys.argv[0]))
    logger.info("Starting script: %s", scriptName)

    vpcName = 'vpc01'
    vpcCIDR = '10.4.0.0/16'
    ec2 = session_setup()
    vpc = create_vpc(ec2, vpcCIDR, vpcName)
    igw = create_igw(ec2, vpc)

    if Cleanup:
        try:
            delete_igw(vpc, igw)
            delete_vpc(vpc)
        except Exception as e:
            logger.debug('Error during cleanup:')
            logger.error(e, exc_info=True)
        else:
            logger.info("VPC %s and IGW %s removed", vpc.vpc_id, igw.internet_gateway_id)

    logger.info("End of script: %s", scriptName)
if __name__ == "__main__":
    main()
