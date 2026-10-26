## Task for Day05

- Using the files created in the previous task (day04), update them to use variables below
- Add an input variable named "environment" and set the default value to "staging"
- Create the terraform.tfvars file and set the environment value to demo
- Test the variable precedence by passing the variables in different ways: tfvars file, environment variables, default, etc.
- Create a local variable with a tag called common_tags with values as env=dev, lob=banking, stage=alpha, and use the local variable in the tags section of main.tf
- Create an output variable to print the storage account name
