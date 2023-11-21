export function user_validate(input) {

    const input_type = input.dataset.tipo;
    const container = input.parentElement;
    const span = container.querySelector('.error-false');

    input.addEventListener('focusout', (e) => {

        if (input.validity.valid){
            input.classList.remove('is-invalid');
            input.classList.add('is-valid');
            return true;
        } 
        else{
            input.classList.remove('is-valid');
            input.classList.add('is-invalid');
            addClass(span, 'text-danger align-self-center p-2');
            span.innerHTML = show_error(input_type, input);
            return false;
        }
    });

    input.addEventListener('focusin', (e) => {
       span.innerHTML='';
    });
}

function show_error(input_type, input) {
    let message = "";
    type_errors.forEach((error) => {
        if (input.validity[error]) {
            message = error_messages[input_type][error];
        }
    })
    return (message)
}

export function addClass(element, className) {
    const classes = className.split(' ');
    for (const class_name of classes) {
        element.classList.add(class_name);
    }
}

const error_messages = {
    type_employee: {
        valueMissing: 'Este campo no puede estar vacío',
    },
    num_employee: {
        valueMissing: 'Este campo no puede estar vacío',
        patternMismatch: 'El número de empleado debe tener entre 5 y 6 dígitos.',
        typeMismatch: 'Este campo solo admite numeros',
    },
    first_name: {
        valueMissing: 'Este campo no puede estar vacío',
        patternMismatch: 'Use un nombre válido',
        typeMismatch: 'Este nombre no es válido',
    },
    last_name: {
        valueMissing: 'Este campo no puede estar vacío',
        patternMismatch: 'Use un apellido válido',
        typeMismatch: 'Este apellido no es válido',
    },
    password: {
        valueMissing: 'Este campo no puede estar vacío',
        patternMismatch: 'Min 8, Max 15, mayúsculas, minúsculas, números y un caracter especial',
        typeMismatch: 'Este password no es válido',
    },
    email: {
        valueMissing: 'Este campo no puede estar vacío',
        patternMismatch: 'Use un email válido ejemplo: email@dominio.com',
        typeMismatch: 'Use un email válido ejemplo: email@dominio.com',
    },
    campaign: {
        valueMissing: 'Este campo no puede estar vacío',
        patternMismatch: '',
        typeMismatch: '',
    },
    role: {
        valueMissing: 'Este campo no puede estar vacío',
        patternMismatch: 'Prueba Pattern',
        typeMismatch: ' Prueba type',
    }
}

const type_errors = [
    'valueMissing',
    'typeMismatch',
    'patternMismatch',
];