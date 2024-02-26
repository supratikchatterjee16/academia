# AWS Architect Certification details

Important components : 

1. Authentication and Authorization through Identity and Access Management(IAM) & Roles based access
2. Compute via Lambda, Elastic Compute, and Containers
3. Networking 
4. Storage
5. Databases
6. Monitoring, Optimization and Serverless

## Identity and Access Maangement

AWS Identity and Access Management (IAM) is an AWS service that helps you manage access to your AWS account and resources. It also provides a centralized view of who and what are allowed inside your AWS account (authentication), and who and what have permissions to use and work with your AWS resources (authorization).

With IAM, you can share access to an AWS account and resources without sharing your set of access keys or password. You can also provide granular access to those working in your account, so people and services only have permissions to the resources they need. For example, to provide a user of your AWS account with read-only access to a particular AWS service, you can granularly select which actions and which resources in that service they can access.

### IAM features

To help control access and manage identities in your AWS account, IAM offers many features to ensure security.

- IAM is global and not specific to any one Region. You can see and use your IAM configurations from any Region in the AWS Management Console.
- IAM is integrated with many AWS services by default. You can establish password policies in IAM to specify complexity requirements and mandatory rotation periods for users.
- IAM supports MFA. IAM supports identity federation, which allows users who already have passwords elsewhere – for example, in your corporate network or with an internet identity provider – to get temporary access to your AWS account.

Any AWS customer can use IAM; the service is offered at no additional charge.

### IAM user

An IAM user represents a person or service that interacts with AWS. You define the user in your AWS account. Any activity done by that user is billed to your account. Once you create a user, that user can sign in to gain access to the AWS resources inside your account.

You can also add more users to your account as needed. For example, for your cat photo application, you could create individual users in your AWS account that correspond to the people who are working on your application. Each person should have their own login credentials. Providing users with their own login credentials prevents sharing of credentials.

### IAM user credentials

An IAM user consists of a name and a set of credentials. When you create a user, you can provide them with the following types of access:

Access to the AWS Management Console
Programmatic access to the AWS Command Line Interface (AWS CLI) and AWS application programming interface (AWS API)
To access the AWS Management Console, provide the user with a user name and password. For programmatic access, AWS generates a set of access keys that can be used with the AWS CLI and AWS API. IAM user credentials are considered permanent, which means that they stay with the user until there’s a forced rotation by admins.

When you create an IAM user, you can grant permissions directly at the user level. This can seem like a good idea if you have only one or a few users. However, as the number of users increases, keeping up with permissions can become more complicated. For example, if you have 3,000 users in your AWS account, administering access and getting a top-level view of who can perform what actions on which resources can be challenging.

If only there was a way to group IAM users and attach permissions at the group level instead. Guess what. There is!

### IAM groups

An IAM group is a collection of users. All users in the group inherit the permissions assigned to the group. This makes it possible to give permissions to multiple users at once. It’s a more convenient and scalable way of managing permissions for users in your AWS account. This is why using IAM groups is a best practice.

If you have an application that you’re trying to build and you have multiple users in one account working on the application, you might organize the users by job function. For instance, you might organize your IAM groups by developers, security, and admins. You could then place all your IAM users into their respective groups.

This provides a way to see who has what permissions in your organization. It also helps you scale when new people join, leave, and change roles in your organization.

Consider the following examples:

A new developer joins your AWS account to help with your application. You create a new user and add them to the developer group, without thinking about which permissions they need.
A developer changes jobs and becomes a security engineer. Instead of editing the user’s permissions directly, you remove them from the old group and add them to the new group that already has the correct level of access.
Keep in mind the following features of groups:

Groups can have many users.
Users can belong to many groups.
Groups cannot belong to groups.
The root user can perform all actions on all resources inside an AWS account by default. This is in contrast to creating new IAM users, new groups, or new roles. New IAM identities can perform no actions inside your AWS account by default until you explicitly grant them permission.

The way you grant permissions in IAM is by using IAM policies.

### IAM policies

To manage access and provide permissions to AWS services and resources, you create IAM policies and attach them to IAM users, groups, and roles. Whenever a user or role makes a request, AWS evaluates the policies associated with them. For example, if you have a developer inside the developers group who makes a request to an AWS service, AWS evaluates any policies attached to the developers group and any policies attached to the developer user to determine if the request should be allowed or denied.

#### IAM policy examples

Most policies are stored in AWS as JSON documents with several policy elements. The following example provides admin access through an IAM identity-based policy.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```

This policy has four major JSON elements: 

1. Version
2. Effect
3. Action
4. Resource

The Version element defines the version of the policy language. It specifies the language syntax rules that are needed by AWS to process a policy. To use all the available policy features, include "Version": "2012-10-17" before the "Statement" element in your policies.

The Effect element specifies whether the statement will allow or deny access. In this policy, the Effect is "Allow", which means you’re providing access to a particular resource.

The Action element describes the type of action that should be allowed or denied. In the example policy, the action is "\*". This is called a wildcard, and it is used to symbolize every action inside your AWS account.
The Resource element specifies the object or objects that the policy statement covers. In the policy example, the resource is the wildcard "\*". This represents all resources inside your AWS console.

Putting this information together, you have a policy that allows you to perform all actions on all resources in your AWS account. This is what we refer to as an administrator policy.

The next example shows a more granular IAM policy.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam: ChangePassword",
                "iam: GetUser"
            ]
            "Resource": "arn:aws:iam::123456789012:user/${aws:username}"
        }
    ]
}
```

After looking at the JSON, you can see that this policy allows the IAM user to change their own IAM password (iam:ChangePassword) and get information about their own user (iam:GetUser). It only permits the user to access their own credentials because the resource restricts access with the variable substitution ${aws:username}.

## Compute

They're divided into the following types : 

1. On-Demand Instances
2. Reserved Instances
3. Spot Instances

