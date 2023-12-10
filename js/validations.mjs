import { typeErrors, errors, addClass } from './sign_up.mjs'
export function inputValidate(input) {
    const ERROR_SHOW_TIME = 2500;
    let errorTimer;
    const container = input.parentElement;
    const span = container.querySelector('.error-false');
    if (input.type !== 'radio') {
        input.addEventListener('focusout', (e) => {
            if (input.validity.valid) {
                input.classList.toggle('is-valid', true);
                input.classList.toggle('is-invalid', false);
            }
            else {
                showError(input)
            }
            errorTimer = setTimeout(() => {
                span.innerHTML = "";
                input.classList.remove('is-valid', 'is-invalid');
            }, ERROR_SHOW_TIME);
        })

        input.addEventListener('focusin', (e) => {
            clearTimeout(errorTimer);
            span.innerHTML = "";
            input.classList.remove('is-valid', 'is-invalid');
        });
    }
}

function showError(input) {
    const inputType = input.dataset.tipo;
    const container = input.parentElement;
    const span = container.querySelector('.error-false');
    const error = getError(inputType, input)
    const textError = `${input.id} inválido. ${error}`

    input.classList.toggle('is-valid', false);
    input.classList.toggle('is-invalid', true);
    addClass(span, 'text-error error-false text-danger w-100', true);
    span.innerHTML = textError
}

function getError(inputType, input) {
    let message = "";
    typeErrors.forEach((error) => {
        if (input.validity[error]) {
            message = errors[inputType][error];
        }
    })
    return (message)
}

export function passwordValidate(input) {

    const pattern = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!?@#$%^&*()_+-]).{8,15}$");
    const container = input.parentElement;
    const span = container.querySelector('.error-false');
    const password_inputs = document.querySelectorAll("input[type='password']");
    let mensaje = ''

    input.addEventListener('focusout', (e) => {
        switch (true) {
            case !input.value.match(pattern):
                mensaje = `${input.id} inválido. Longitud: 8-15, 1 mayúscula, 1 minúsculas, 1 número, 1 caracter especial`
                input.classList.toggle("is-valid", false);
                input.classList.toggle("is-invalid", true);
                addClass(span, "error-false text-danger text-error w-100", true);
                span.innerHTML = mensaje;
                break;
            case password_inputs[0].value !== password_inputs[1].value && password_inputs[0].value !== '' && password_inputs[1].value !== '':
                mensaje = "Las contraseñas no coinciden";
                input.classList.toggle("is-valid", false);
                input.classList.toggle("is-invalid", true);
                addClass(span, "error-false text-danger text-error w-100", true);
                span.innerHTML = mensaje;
                return false;
            case password_inputs[0].value === password_inputs[1].value && input.value.match(pattern):
                mensaje = "Las contraseñas coinciden";
                input.classList.toggle("is-valid", true);
                input.classList.toggle("is-invalid", false);
                addClass(span, "text-success w-100", true);
                span.innerHTML = mensaje;
                return true;
            default:
                input.classList.toggle("is-valid", true);
                input.classList.toggle("is-invalid", false);
        }

    });
}