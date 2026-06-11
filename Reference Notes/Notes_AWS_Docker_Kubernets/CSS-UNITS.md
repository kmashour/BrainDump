---
tags:
  - CSS
Type: Reference Note
source: udemy.com/course/web-developer-bootcamp-flask-python
page:
links:
Folgezettel:
---
## Pixels (`px`)
Take an iPhone 11 Pro, for example. An iPhone 11 Pro has a whopping device resoluton of `2436 x 1125`, but in CSS pixels, the device is only `812 x 375`: a third of the device values.

## Percentages (`%`)
Percentages are generally used to set values relative to a parent element. For example, setting a width of `50%` on a valid element will set it to `50%` of the width of its parent.

In some cases, the percentage value is relative to the element itself. For example when using the `transform` property to translate an element to a new position.

## `em` and `rem`

When working with `em` units, the font size of the element where the unit is being used determines the size of `1em`. For example, if we have an element with a font size of `10px`, then `1em` is considered to be `10px`when used to size components of that element.

`rem` stands for _root_ `em`, and is generally a far more useful unit. `rem`uses the global font size to determine its size, which means that `rem` units are consistent across our entire site.

`rem` forms the cornerstone of modern responsive design, as we'll see shortly.



## Viewport units (`vh`, `vw`)

Viewport units are relatively easy to understand, and can be very useful.
`1vh` is equal to 1% of the height of the "viewport", which is essentially the visible area of the website in the browser window.
`1vw` is the corresponding value for the _width_ of the viewport.
We can set values greater than `100` if we like, which will create some amount of horizontal or vertical scrolling.