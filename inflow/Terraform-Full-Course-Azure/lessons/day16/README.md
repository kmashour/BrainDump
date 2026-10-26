## Learn Terraform Azure AD


It contains Terraform conifguration files for you to use to learn how to to manage Azure AD users and groups using
Terraform.

## References:

https://registry.terraform.io/providers/hashicorp/azuread/latest/docs/guides/service_principal_client_secret

https://registry.terraform.io/providers/hashicorp/azuread/latest/docs/guides/microsoft-graph
https://registry.terraform.io/providers/hashicorp/azuread/latest/docs/data-sources/domains

## Task for day16

- Create a csv file for the Active directory users using the below sample data

```csv
first_name,last_name,department,job_title
Michael,Scott,Education,Manager
Jim,Halpert,Education,Engineer
Pam,Beesly,Education,Engineer
```
- Follow the video tutorial and create the AD users, groups and user to group association
- Create more users
- Add one to the existing group
- create another group for customer success and add the new user to that
- do all of these using the service principal
