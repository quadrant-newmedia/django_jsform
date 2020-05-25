function set_form_errors(form, form_errors, error_map) {
    /*
        form: a form element
        forms_errors: an ERROR_LIST of form-level errors
        error_map:
            maps an id to an ERROR_LIST
            error messages should be concatenated and put into element with that id
            any input(s) with aria-errormessage equal to that id should have aria-invalid set appropriately (true if error list is non-empty, false otherwise)

        ERROR_LIST: either a string, or array of strings

        Note - if you do not specify all error message containers in error_map, then we will not clear error messages that are not specified. You must call clear_form_errors() first, if you want to clear them.
    */

    function make_error_string(error_list) {
        if (Array.isArray(error_list)) return error_list.join('. ');
        return error_list
    }

    // Form-level errors
    var fe = form.querySelector('[data-form-errors]');
    if (fe) fe.innerText = make_error_string(form_errors);

    // Element-level errors
    for (var id in error_map) {
        if (!error_map.hasOwnProperty(id)) continue

        var errors = error_map[id];
        var e = document.getElementById(id);
        if (e) e.innerText = make_error_string(errors);

        var form_elements = document.querySelectorAll('[aria-errormessage="'+id+'"]');
        for (var i = form_elements.length - 1; i >= 0; i--) {
            form_elements[i].setAttribute('aria-invalid', errors.length ? 'true' : 'false');
        }
    }
}