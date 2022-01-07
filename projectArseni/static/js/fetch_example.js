

function getUsers(){
    let id = document.getElementById("js").value;
    console.log(id);

    fetch('https://reqres.in/api/users/'+id).then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(response_obj_data) {

    const curr_main = document.querySelector("div");
    curr_main.innerHTML = `
    <img src="${response_obj_data.avatar}" alt="Profile Picture"/>
    <div>
        <span>ID: ${response_obj_data.id}</span><br>
        <span>Email: ${response_obj_data.email}</span><br>
        <span>${response_obj_data.first_name} ${response_obj_data.last_name}</span><br>
        <span>Url: ${response_obj_data.support}</span><br>

        <br>
        <a href="mailto:${response_obj_data.email}">Send Email</a>
    </div>
    `;

}


