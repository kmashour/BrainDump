## Task details for Day 21 - Azure policy and Governance

### Create three policies as below:

- Location restriction (limit resource creation to specific regions such as eastus, westus)
- VM size control (restrict to cost-effective sizes)
    Only the below VM types should be allowed
    - "Standard_B2s"
    - "Standard_B2ms"
- Mandatory tagging (enforce department and project tags)

### Policy Assignment

- Assign policies to subscription
- Use Data source to fetch the subscription details
- Apply configurations


### Attempting non-compliant resource creation

- Verifying policy enforcement
- Creating compliant resources
- Creating non-compliant resources
