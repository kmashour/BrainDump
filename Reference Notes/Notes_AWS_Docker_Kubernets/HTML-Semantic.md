---
tags:
  - HTML
Type: Reference Note
Date:
deadline:
status:
---
When writing HTML we're interested in describing the meaning of the page's content,

### Default styles

It's worth noting that while HTML is not for describing the appearance of a given page, the HTML elements we use will produce visual changes when we load the HTML page in the browser. This is because different HTML elements have default CSS styles applied to them.

For example, the content inside `<b>` and `<strong>` elements will generally be rendered in bold.

Despite this, you should resist the temptation to use HTML to create these visual effects on your websites. If you want some text to be italicized, you shouldn't just wrap that text in an `<em>` element, because this element has special meaning. It means that the content between the opening closing tags of the element is something we want to emphasize.
The correct element to describe these foreign words is `<i>`, but there's no guarantee that this will produce this italicised style.

**In all of these cases, we should be writing CSS to italicise the text, and we should leave the HTML to purely describe the meaning of the document.**