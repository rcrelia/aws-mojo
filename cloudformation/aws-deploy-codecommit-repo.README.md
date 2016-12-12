
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

## Outputs

 * **CloneUrlSsh** - `{u'Fn::GetAtt': [u'Repository', u'CloneUrlSsh']}`
 * **CodeCommitURL** - `{u'Fn::Join': [u'', [u'https://console.aws.amazon.com/codecommit/home?region=', {u'Ref': u'AWS::Region'}, u'#/repository/', {u'Ref': u'RepoName'}, u'/browse/HEAD/--/']]}`
 * **SNSTopic** - `{u'Ref': u'RepoSNSTopic'}`
