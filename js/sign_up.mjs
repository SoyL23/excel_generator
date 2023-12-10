export function getData(inputs) {
    const campaignSelect = document.getElementById('campaign');
    const roleSelect = document.getElementById('role');
    const campaignValue = campaignSelect.options[campaignSelect.selectedIndex].value;
    const roleValue = roleSelect.options[roleSelect.selectedIndex].value;
    const user_data = {};
    inputs.forEach((input) => {
        if (input.type != 'radio') {
            user_data[input.name] = input.value;
        }
        if (input.type === 'radio' && input.checked) {
            user_data[input.id] = input.value;
        }
    });
    user_data['role'] = roleValue;
    user_data['campaign'] = campaignValue;
    return user_data
}

export function showPassword(){
    const password_inputs = document.querySelectorAll("input[type='password']");
    const spans = document.querySelectorAll('.visibility');
    spans.forEach((span) => {
        span.addEventListener('click', (e) => {
            console.log(e)
            password_inputs.forEach((password_input) => {
                if(password_input.type == 'text'){
                    password_input.type = 'password'
                } else if (password_input.type = 'password'){
                    password_input.type = 'text'
                }
            });
        });
    });    
}

export function showResponse(response) {
    const span = document.querySelector('.response')
    addClass(span, 'response alert alert-success')
    span.innerHTML = response
}

export function addClass(element, className) {
    const classes = className.split(' ');
    for (const class_name of classes) {
        element.classList.add(class_name);
    }
}

export const errors= {
    type_employee: {
        valueMissing: 'Este campo no puede estar vacío',
    },
    numemployee: {
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
    },
    email: {
        valueMissing: 'Este campo no puede estar vacío',
        patternMismatch: 'Use un email válido ejemplo: email@dominio.com',
        typeMismatch: 'Use un email válido ejemplo: email@dominio.com',
    },
    campaign: {
        valueMissing: 'Este campo no puede estar vacío',
    },
    role: {
        valueMissing: 'Este campo no puede estar vacío',
    }
}

export const typeErrors = [
    'valueMissing',
    'typeMismatch',
    'patternMismatch',
];