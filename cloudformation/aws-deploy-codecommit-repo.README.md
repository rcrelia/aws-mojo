
## Description

CloudFormation template for creating a CodeCommit repository along with a SNS topic for repo activity trigger notifications

## Parameters

 * **Email** - Email address for SNS notifications on repo processing
  * Constraint: `Must be a valid email address`
 * **Environment** - Environment type (can be used for tagging)
  * Default: `Dev`
 * **RepoDescription** - A description of the CodeCommit repository
 * **RepoName** - A unique name for the CodeCommit repository

## Resources

 * **RepoSNSTopic** - `AWS::SNS::Topic`
 * **Repository** - `AWS::CodeCommit::Repository`

