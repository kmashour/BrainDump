---
tags:
  - CSS
Type: Reference Note
source: udemy.com/course/web-developer-bootcamp-flask-python
page:
links:
DeeperDive:
---
Inheritance is an important concept and a powerful tool which we can leverage when writing CSS code. Inheritance allows us to write less code, reduce repetition, and make our stylesheets easier to maintain.

so basically some properties are inherited by default from parent elements if we have nested elements and the nested element doesn't have the property defined 

some properties are not inherited by default even if they are the are child elements like `<a <\a>` , we can work around it by just using the inherit value to the property `color="inherit"`
```HTML
<div class="#">
<a href="##" > hell yeah!! <\a>
<\div>
```

```css
.#{
color: orange 
}
```
The anchor text will not be changed unless we use inherit 


> [!NOTE] Title
> Its easier to track Non-Inherited properties rather than the inherited ones 

