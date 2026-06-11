---
tags:
  - HTML
Type: Reference Note
Date:
deadline:
status: true
---
This is not an easy question to answer, because different elements within a given content category permit wildly different content. For example, the `<a>` element and the `<select>` element are both [phrasing content](https://python-web.teclado.com/section04/lectures/04_html_categories/#phrasing-content); however, the `<a>` element is permitted to contain any non-interactive [flow content](https://python-web.teclado.com/section04/lectures/04_html_categories/#flow-content), 
**while `<select>` is limited to zero or more `<option>` or `<optgroup>` element ??**


If you're unsure whether or not something is valid markup, **you should double check the permitted content and permitted parent elements for the elements you're trying to use.** Over time you'll have to reference the documentation less and less as you get familiar with the rules surrounding many of the core elements.
