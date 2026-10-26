## Task for Day07

### Using the files from previous task(day06) , understand the use the below type constraints

- Name: environment, type=string
- Name: storage-disk, type=number
- Name: is_delete, type=boolean
- Name: Allowed_locations, type=list(string)
- Name: resource_tags , type=map(string)
- Name: network_config , type=tuple([string, string, number])
- Name: allowed_vm_sizes, type=list(string)
- Name: vm_config,
```
  type = object({
    size         = string
    publisher    = string
    offer        = string
    sku          = string
    version      = string
  })
```
