import { showResponse } from "./sign_up.mjs";

export async function create_user(newUser) {
    console.log(newUser)
    const response = await fetch('/user/new', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newUser)
    });

    const responseJSON = await response.json();
    showResponse(responseJSON);
}