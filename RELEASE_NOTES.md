### 2.2.2
Drop usage of NavTricks in `js_response.replace_location()`, since NavTricks's implementation of `replaceCurrentPage` never worked right, and has been dropped in recent versions.

### 2.2.1
Set proper `this` inside inline event handlers.

## 2.2.0
`jsform_execresponse` now handles `jsformerror` events in addition to `jsformsuccess`.

`js_response.set_form_errors()` now returns a 400 status code by default. This means you can use this response to handle form errors, and return a simple HttpResponse() for successful forms (letting a custom inline handler define what to do for successful form submissions).

### 2.1.1
Fixed several IE bugs.

## 2.1.0
Added inline event handler support.

# 2.0.0
Various bug fixes, added tests.

Breaking changes:
- removed \[push-query\]

# 1.0.0