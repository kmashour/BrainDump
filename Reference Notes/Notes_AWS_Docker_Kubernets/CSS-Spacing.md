---
tags:
  - CSS
Type: Reference Note
source: udemy.com/course/web-developer-bootcamp-flask-python
page:
links:
Folgezettel:
---
## Centering the content

After using the box-model as the main style for handling boxes 

``` CSS
*,
*::before,
*::after {
  box-sizing: inherit;
}

body {
  box-sizing: border-box;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Ubuntu, sans-serif;
  color: #002240;
}
```

We need to put All of our HTML inside the `main` to center the content 
