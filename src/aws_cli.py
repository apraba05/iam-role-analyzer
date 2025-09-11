import boto3

iam=boto3.client('iam')

def get_role_policies(role_name):
    inline_policies = {}
    managed_policies = {}

    for policy_name in iam.list_role_policies(RoleName=role_name)['PolicyNames']:
        policy = iam.get_role_policy(RoleName=role_name, PolicyName=policy_name)
        inline_policies[policy_name] = policy['PolicyDocument']

    for policy_name_managed in iam.list_attached_role_policies(RoleName=role_name)['AttachedPolicies']:
        policy_arn = policy_name_managed['PolicyArn']
        policy_version = iam.get_policy(PolicyArn=policy_arn)['Policy']['DefaultVersionId']
        policy = iam.get_policy_version(PolicyArn=policy_arn, VersionId=policy_version)
        managed_policies[policy_name_managed['PolicyName']] = policy['PolicyVersion']['Document']

    return {**inline_policies, **managed_policies}

