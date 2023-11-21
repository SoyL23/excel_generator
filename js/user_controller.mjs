export async function create_user(newUser) {
    const response = await fetch('/user/create', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(newUser)
    });
    const responseJSON = await response.json();
    if (!response.ok) {
        return "Error: ", response;
    }
    console.log(responseJSON);
    return responseJSON;
}
