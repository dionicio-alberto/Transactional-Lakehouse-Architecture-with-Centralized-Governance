# Component Dependencies

## Data Flow
```text
[Local Machine] --(Sync AWS CLI)--> [S3 Raw Zone]
                                         |
                                  [Step Functions] --(Triggers)--> [Glue PySpark ETL]
                                                                         |
                                    <Boto3 tag binding> + <Iceberg partition writes>
                                                                         |
                                                [S3 Curated Zone & Glue Data Catalog]
                                                                         |
                                              <Lake Formation RBAC & Prefix interception>
                                                                         |
                                                                 [Amazon Athena]
```

## Infrastructure Provisioning Sequence (Terraform)
The infrastructure MUST be provisioned adhering to the following strict dependency chain:
1. **IAM Roles**: Establish the execution roles (Glue) and the persona roles (DataAdmin, Analysts).
2. **S3 Buckets**: Storage must exist before processing or cataloging.
3. **Lake Formation Settings**: Establish the DataAdmin role as the Data Lake Administrator and completely REVOKE the `IAMAllowedPrincipals` default grant.
4. **Lake Formation Tags**: Define the ontology keys and values.
5. **Glue Data Catalog**: Provision the initial database structure and apply LF-Tag sharing policies per persona attached via IAM.
6. **Glue Job / Step Functions**: Provision the PySpark script, associating it with the IAM Execution Role.
