# Integration Test Instructions - Unit 1

## Purpose
Ensure out-of-band transfers and infrastructure endpoints act correctly once files are materialized locally by the simulator.

## Test Scenarios
### Scenario 1: [Simulator Output] -> [AWS CLI] Integration
- **Description**: Validate that files produced by `main.py` successfully interact with terminal S3 syncs.
- **Setup**: Execute the unit locally to produce `<1.3mb` data files. Ensure Terraform keys match CLI profile.
- **Test Steps**: Run `aws s3 sync src/simulator/data/staged/ s3://[terraform-raw-bucket-name]/ --dryrun`
- **Expected Results**: Boto3 core parses file streams gracefully without access-denied warnings over IAM constraints.
- **Cleanup**: Purge remote test objects if `dryrun` is disabled.

## Run Integration Tests
As this unit explicitly decoupled `boto3` out of the simulator, the "integration" strictly occurs across the network boundary executed via human or pipeline orchestration tooling.
