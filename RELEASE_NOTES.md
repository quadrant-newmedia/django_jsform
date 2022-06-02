# 5.0.0
Ensure that non-GET forms are never empty (send a "__hack_ensure_body_not_empty__" key, with no value).
This is to work-around browsers/firewalls/proxies that have issues with empty multipart/form-data POST requests.

For most projects, this will be backward compatible with v4. 
It's only an issue if your code has an issue with this extra value
(ie. it checks for an "empty" data set, or does something with all keys in the data set).

## 4.3.0

Updated get-error-message-id, so that output can more easily be replicated if all you know is the html input's name attribute.

This _may_ break some things if you were previously manually recreating the format of our error message containers.

## 4.2.1
Officially support Django 3.2

# 4.2.0
Set `X-Requested-With` HTTP header to `jsform`

# 4.1.0
Support `formtarget` on submit buttons, so you can opt-in or opt-out of jsform per-button.

# 4.0.1
elementmerge IE bug work-around. Never merge textarea children (because that changes the element's value in IE).

# 4.0.0
jsform update - change default actions of `jsformsuccess`, `jsformerror`, `jsformnetworkerror`  - unblock form when it's deemed "safe". `jsformerror` always unblocks form, `jsformsuccess` and `jsformnetworkerror` only unblock on GET.

Technically, this is a breaking change, but most users should be happy with the change, and won't require any code changes.

### 3.11.1
jsform bug fix

## 3.11.0
Added `ignoreattrs` option to elementmerge

## 3.10.0
`js_response.set_form_errors()` now focuses the first "error element" in the form. 

This was always the intended behaviour (at least, when using jsform_focus_error_element.js), but since `set_form_errors` was updated to use status code of 400 by default, jsform_focus_error_element.js has no effect.

## 3.9.0
elementmerge - add `elementmerge-replace` option

## 3.8.0
elementmerge - fire `elementmergecomplete` event when done.

## 3.7
Give event handlers and execresponse access to `submitting_button`.

### 3.6.2
`js_response.reset_form()` bug fix (and default `unblock_form` to True)

### 3.6.1
Changed `.block` css -> setting left/right margin to 'auto' has no effect on any layout _we_ create, but can cause problems if users are using this class for other layouts on their sites. No longer set left/right margin at all.

## 3.6.0
Add means of passing custom selectors to elementmerge.

### 3.5.2
elementmerge - don't `setAttribute()` if unchanged - was causing stylesheets to unapplied/reapplied, causing FOUC

### 3.5.1
broken update - forgot to commit submodule

## 3.5.0
js_response module now generates responses which can be added together

## 3.4.0
Added new template ("inline_field.html") for rendering fields in one line

## 3.3.0
Updated jsform.js - add more properties to `jsformsuccess` and `jsformerror` events.

## 3.2.0
Better template generation for single checkboxes

### 3.1.3
Bug fix - handle the case where form controls have names that clash with js form attributes. Still don't properly handle the case where a control has name "elements", but at least throw a meaningful error.

### 3.1.2
Bug fix in elementmerge - ensure that multiple consecutive nodes will be deleted if not present in new DOM (previously it would only delete the first removed node).

### 3.1.1
`elementmerge.reload()` bug fix - keep query string

## 3.1.0
`jsform_elementmerge.js` enhancements - `[elementmerge-whitelist]` directive, and global `elementmerge` object for usage without `jsform.js`. See README for jsform for details.

# 3.0.0
`elementmerge.js` now merges the `head`, as well as the `body`. Set `elementmerge-nomerge` on the `head` if you want to retain old behaviour.

## 2.3.0
Templates now set `aria-invalid="true"` when rendering invalid form inputs (`set_form_errors.js` always did this, and `django_jsform.css` depends on it for styling).

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