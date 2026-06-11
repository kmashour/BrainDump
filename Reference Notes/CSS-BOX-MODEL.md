---
tags:
  - CSS
Type: Reference Note
source: udemy.com/course/web-developer-bootcamp-flask-python
page:
links:
Folgezettel:
---


The borders and the padding are added to the box main content area size 
```
.box-example {
    padding-left: 10px;
    padding-right: 20px;
    border: 1px solid #000;
}
```
so the actual size is = 300 - ( 2 * 1px ) - 10px - 20px

so we use 

In the alternative box model, the `height` and `width` properties determine the dimensions of the box to the outside of the border. This means the value we set for the `width` and `height` determine the overall width and height of an element, barring the margins.

We can tell CSS to use the alternative box model for a given element by setting the `box-sizing` property for that element, giving it a value of `border-box`.

I recommend you use `border-box` sizing for _all_ of your elements, but unfortunately it's not an inherited property, so we need to be a little clever about how we do this. We don't want to have to manually specify `box-sizing` for every single element on the page, after all!

What we can do instead, is this:

```
*,
*::before,
*::after {
    box-sizing: inherit;
}

body {
    box-sizing: border-box;
}
```

Why use inherit?

Some of you may be wondering, why not just do something like this:

```
*,
*::before,
*::after {
    box-sizing: border-box;
}
```

There are two main reasons.

1. Setting an explicit `box-sizing` value means we can't use inheritance later on in cases where we want to switch back to the standard box model.
    
2. Using `*` to set `box-sizing` to `border-box` universally has a wider reaching effect than inheriting from the `<body>` element. For example, the `<html>` element and everything in the `<head>` would have their `box-sizing` set.
    


## Block vs inline boxes

The picture we've been painting so far isn't entirely complete, as we've only really discussed the box model for elements being displayed as _blocks_. For inline elements, the story is a little different.

For example, when working with an inline element, we can't set an explicit height and width. The size of the content determines the size of the content box. Any `height` and `width` properties will be ignored.

We also can't create space above and below an element by applying vertical padding and margins. Only horizontal padding and margins will move the content around the element. The same is true of borders.

While vertical padding has no effect on the layout of an inline element in relation to those around it, the padding value is still being applied. This is important to note, as vertical padding will change the position of borders around an inline element. The background will also stretch to fill the space specified by the vertical padding.

## Beyond sizing

It's worth spending the time to get familiar with the components of the box model, even if you plan to always set the `box-sizing` to `border-box`, as these components are used to determine the effect of other properties.

For example, the `background-origin` property allows us to determine where the background ends. We can set values like `border-box`, `padding-box`, and `content-box`, which directly map onto the components of the box model we saw before.

You can find more information on the `background-origin` property