# AWS Compute Services

1. Elastic Compute Cloud
    - Uses pre-configured AWS Machine Images(AMIs)
    - Uses Elastic Block Store for persistence
    - Allows increasing or decreasing capacity within minutes instead of hours or days
    - provides complete control of instances
    - includes various linux and windows server OS
    - Pay a relatively low rate for the compute capacity consumed
2. Virtual Private Cloud
    - ISa dedicated customer network on the AWS infra
    - Logically separated from other AWS virtual networks
    - Can be used to launch EC2 instances
3. Elastic Load Balancing
    - Critical AWS service for automatically distributing incoming app traffics across many target groups of EC2 instances, containers, and IP addresses
    - Handle various loads of your apps in a single or multiple Availability Zones
    - Are of 3 types
        - Network ELB
        - Application ELB
        - Classic ELB
4. AWS EC2 Auto Scaling
    - for fleet management
    - dynamic scaling
    - decrease capacity during downtime
5. Lambda compute services
    - Costs only when code is running
