import { user_validate} from './sign_up.mjs';
import { create_user } from './user_controller.mjs';


document.addEventListener("DOMContentLoaded", () => {
    const inputs = document.querySelectorAll('input');
    const form = document.querySelector('#form_signup')
    const submit =  document.querySelector('#submit_login')

    const campaignSelect = document.getElementById('campaign');
    
    const roleSelect = document.getElementById('role');

    const user_data = {};

    inputs.forEach((input) => {
        user_validate(input);
    });



    inputs.forEach((input) => {
    if (input.classList.contains('is-invalid')) {
        console.log('Hay campos invalidos')
    }else{
        submit.removeAttribute('disabled')
    }
    });

    form.addEventListener('submit', (e) => {
      e.preventDefault();
        const campaignValue = campaignSelect.options[campaignSelect.selectedIndex].value;
        const roleValue = roleSelect.options[roleSelect.selectedIndex].value;
        inputs.forEach((input) => {
          if(input.type != 'radio'){
            user_data[input.id] = input.value;
          }
          if (input.type === 'radio' && input.checked) {
            user_data[input.id] = input.value;
          }
        });

        user_data['role'] = roleValue;
        user_data['campaign'] = campaignValue;

        response = create_user(user_data);
        console.log(response)

    });
      

});
