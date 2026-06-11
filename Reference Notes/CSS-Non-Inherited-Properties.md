---
tags:
  - CSS
Type: Reference Note
source: udemy.com/course/web-developer-bootcamp-flask-python
page:
links:
Folgezettel:
---
## Layout properties
A broad category of non-inherited properties can be thought of as "layout properties": properties which change the size of the element in some way, or how it interacts with the elements around it.
These properties include things like `margin`, `padding`, `height`, `width`, `box-sizing`, `position`, and `display`.

> [!NOTE]
> `display` is another case where we could run into major problems. `<p>` elements have a display style of `block`, which means they fill the width of their container. We often put things like `<span>` and `<a>` elements inside `<p>` elements, and usually we want them to fit into the normal flow of the text content. We generally don't want these elements forced onto their own lines.
> If these properties were inherited, we'd inevitably end up writing far more code just to correct the issues being caused by inheritance

## Borders and outlines

Border and outline properties — much like layout properties — are not inherited by default, and for much the same reason.

Just because we want a border around a `<p>` element, it doesn't mean we want a border around every element inside the `<p>` element as well. Correcting these issues would become a real headache, as we'd have to set `border: none;` on every child of that `<p>` element.

In the very unlikely case that we _do_ want to inherit the border of some parent element, remember we can set `border: inherit;` on the child elements to force the inheritance of non-inherited proper
## Background properties
For simple cases, like setting a matte colour, it's not really obvious why this property wouldn't be inherited. After all, if the background of a given container is `red`, and the child elements don't have a background colour set, then they're going to appear to have a `red` background.
However, we can produce far more elaborate backgrounds for elements than this, and in those cases we'd end up in hot water.
For example, say we decide to use an image as a background for a given element. If the child elements inherited this property value, then we'd get a new version of the image for each of these elements, each placed in a different element's space. This is almost certainly not what we want.
We can end up in a similar situation when setting a gradient as the background for an element. We don't want all of the child elements to have their own gradient background, as they won't match the overall background.
There are also problematic cases with a matte background as well. For example, what if we set a `position` property on a child element which places it outside of its parent element somehow. In those cases, it's not clear that we'd want this background to extend beyond the parent element, so it's better left for the developer to specify this explicitly