# Application Design Plan

## Phase 1: Planning and Verification
- [ ] Review answers to application design questions.
- [ ] Resolve any ambiguities from the user's answers.

## Phase 2: Design Artifact Generation
- [ ] Generate `components.md` with system components and their responsibilities (e.g., Data Simulator, ETL Pipeline, Security/IaC).
- [ ] Generate `component-methods.md` outlining the high-level inputs/outputs of Python scripts and PySpark transformations.
- [ ] Generate `services.md` detailing how AWS services (S3, Glue, Lake Formation, Athena) interface.
- [ ] Generate `component-dependency.md` displaying the flow of data from Raw -> Curated and the associated IaC provisioning sequence.
- [ ] Generate a master `application-design.md` that consolidates these artifacts.

---

# Clarification Questions

Please answer the following questions to guide the Application Design generation using the [Answer]: tag.

## Question 1: Data Simulator Execution Component
Where will the Python Data Simulator component run? This affects its interface and deployment strategy.

A) Executed locally by developers prior to infrastructure deployment to generate the initial seed data.
B) Executed via a GitHub Actions CI/CD pipeline step that uploads directly to the S3 Raw Zone.
C) Deployed as an AWS Lambda function triggered on a schedule.
X) Other (please specify)

[Answer]: A 

## Question 2: ETL Pipeline Trigger Mechanism
How should the PySpark Glue Job (ETL Component) be orchestrated?

A) Event-Driven: Triggered automatically by S3 Event Notifications when the Data Simulator drops new files into the raw-zone.
B) Data Pipeline: Orchestrated via an AWS Step Functions state machine or Glue Workflow.
C) Manual / On-Demand: Triggered manually or via the AWS CLI for the purposes of this architectural demonstration.
X) Other (please specify)

[Answer]: B

## Question 3: Lake Formation Tag Binding Strategy
Lake Formation uses LF-Tags for ontology-based security. At what lifecycle component should these tags be associated with the Glue database and Iceberg tables?

A) Pure IaC: Terraform creates the LF-Tags and associates them with the database, but since tables are created later by Glue, a post-deployment boto3/Terraform script must bind tags to the tables.
B) Glue Job Self-Tagging: The PySpark Glue Job self-assigns the LF-Tags to the Iceberg tables it creates via AWS API (boto3) calls at the end of its run.
C) Native Lakehouse: Terraform grants LF-Tag permissions to the database and relies on schema inheritance, relying on standard tags where possible.
X) Other (please specify)

[Answer]: B
