function clear_form_errors(form) {
    // form-level errors
    var fe = form.querySelector('data-form-errors');
    if (fe) fe.innerText = '';

    // element-level errors
    // Note - we don't use querySelectorAll, in case the page is using [form="form_id"] on inputs that are outside of the form in the DOM
    for (var i = form.elements.length - 1; i >= 0; i--) {
        var e = form.elements[i];
        e.setAttribute('aria-invalid', 'false');

        var error_container_id = e.getAttribute('aria-errormessage');
        if (!error_container_id) continue
        var error_container = document.getElementById(error_container_id);
        if (!error_container) continue
        error_container.innerText = ''; 
    }
}
