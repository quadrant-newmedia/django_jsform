/*
    Adapted from jsform_focus_error_element.js

    That script, if used, will focus error elements automatically on jsformsuccess (ie. 200 level responses). It's intended to be used jsform_elementmerge.

    js_response.set_form_errors returns status code 400 by default, so jsform_focus_error_element doesn't work. We don't want to change it to blindly focus error elements on any response (even unsuccessful ones), so this gives us the ability to invoke that behavior explicitly. 
*/
function focus_form_errors(form) {
    'use strict';
    function get_item_to_focus() {
        if (!form.ownerDocument) {
            // The form has been removed from the DOM
            return null
        }
        if (document.activeElement && document.activeElement.form == form && document.activeElement.getAttribute('aria-invalid') == 'true') {
            // An invalid input already has focus
            return null;
        }

        var form_error_container = form.querySelector('[data-form-errors]');
        // Notice - if you want form-level errors to be focused after submit, you should set tabindex attribute
        // (you can set tabindex="-1" to prevent keyboard focus but still allow programmatic focus)
        if (form_error_container && form_error_container.getAttribute('tabindex') && form_error_container.innerText.trim() != '') return form_error_container;
        
        for (var i = 0; i < form.elements.length; i++) {
            if (form.elements[i].getAttribute('aria-invalid') == 'true') return form.elements[i];
        }

        return null
    }

    var ft = get_item_to_focus();
    ft && ft.focus();
}