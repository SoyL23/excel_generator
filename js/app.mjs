import { getData, showPassword } from './sign_up.mjs';
import { create_user } from './user_controller.mjs';
import {passwordValidate, inputValidate} from './validations.mjs'

const inputs = document.querySelectorAll('input');
const form = document.querySelector('#form_signup')
const password_inputs = document.querySelectorAll("input[type='password']");

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const user_data = getData(inputs)
  create_user(user_data);
  form.reset()
});

document.addEventListener('DOMContentLoaded', () => {

  inputs.forEach((input) => {
      inputValidate(input)
  });

  password_inputs.forEach((password_input) => {
    passwordValidate(password_input)
  });
  showPassword()
});