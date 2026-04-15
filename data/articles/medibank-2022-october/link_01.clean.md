---
title: Amazon Redshift gets new default settings to prevent data breaches
url: "https://www.bleepingcomputer.com/news/security/amazon-redshift-gets-new-default-settings-to-prevent-data-breaches/"
author: Bill Toulas
published: 2025-02-03
source_type: article
source_domain: www.bleepingcomputer.com
cleanup_method: llm
---

# Amazon Redshift gets new default settings to prevent data breaches


# Amazon Redshift gets new default settings to prevent data breaches

 By 
###### [Bill Toulas](https://www.bleepingcomputer.com/author/bill-toulas/)

*   February 3, 2025
*   04:37 PM


Amazon has announced key security enhancements for Redshift, a popular data warehousing solution, to help prevent data exposures due to misconfigurations and insecure default settings.

Redshift is widely used by enterprises for business intelligence and big data analytics for data warehousing, competing with Google BigQuery, Snowflake, and Azure Synapse Analytics.

It's valued for its petabyte-scale data handling efficiency and performance, scalability, and cost-effectiveness.


However, poor configurations and lax default settings have led to massive data breaches, like the [Medibank ransomware incident](https://www.bleepingcomputer.com/news/security/medibank-now-says-hackers-accessed-all-its-customers-personal-data/) in October 2022, which [reportedly](https://x.com/Jeremy_Kirk/status/1590517192080388096) involved access to the firm's Redshift platform.

## Strengthening Redshift security

Last week, AWS announced that it is implementing three security defaults for newly created provisioned clusters to significantly upgrade the platform's data safety and minimize the likelihood of catastrophic data leaks.

The first measure is to restrict public access for new clusters by default, confining them within the user's Virtual Private Cloud (VPC) and preventing direct external access.

Public access must be explicitly enabled if needed, with security groups and network access control lists (ACLs) recommended to users for restricted access.

The second change is to enable encryption by default for all clusters to guarantee that even unauthorized access will not result in data exposure.

Users will now have to specify an encryption key, or the clusters will be encrypted using an AWS-owned Key Management Service (KMS) key.

Users relying on unencrypted clusters for data sharing must ensure both producer and consumer clusters are encrypted. Failure to adjust these workflows may result in disruptions when the changes go live.

The third change is enforcing secure SSL (TLS) connections by default for all new and restored clusters, preventing data interception and "man-in-the-middle" attacks.

Users with custom parameter groups are encouraged to enable SSL for enhanced security manually.

It is important to note that these changes will impact newly created provisioned clusters, serverless workgroups, and restored clusters, so existing setups will not be immediately affected.

However, AWS recommends that customers review and update their configurations as needed to align with the new security defaults and avoid operational disruptions.

"We recommend that all Amazon Redshift customers review their current configurations for this service and consider implementing the new security measures across their applications," [reads the announcement](https://aws.amazon.com/blogs/security/amazon-redshift-enhances-security-by-changing-default-behavior-in-2025/).

"These security enhancements could impact existing workflows that rely on public access, unencrypted clusters, or non-SSL connections."

Customers seeking guidance and support are directed to read the online '[Management Guide](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-ssl-support.html)' or contact AWS Support.



 Bill Toulas is a tech writer and infosec news reporter with over a decade of experience working on various online publications, covering open-source, Linux, malware, data breach incidents, and hacks. 

![Image 50](https://a.pub.network/core/imgs/1.png?x=2026-04-14T19%3A50%3A45.007)
