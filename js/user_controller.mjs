import { showResponse } from "./sign_up.mjs";

export async function createUser(newUser) {
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

export async function editUser(editedUser, id){
    const response = await fetch(`/user/edit/${id}`,{
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(editedUser)
    })

    const responseJSON = await response.json();
}

export async function deleteUser(id){
    const response = await fetch(`/user/delete/${id}`,{
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(id)
    })

    const responseJSON = await response.json();
}