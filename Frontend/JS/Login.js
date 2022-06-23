async function getlogin() {
    const username = document.getElementById("username").value
    const password = document.getElementById("password").value

    const url = `http://localhost:5000/login/${username}/${password}`;

    const httpResponse = await fetch(url);
    const body = await httpResponse.json();
    console.log(body);

    if (body.LoginStatus == 'true'){
        sessionStorage.setItem('userdata', JSON.stringify(body))


        window.location.href = "file:///F:/Projects/Java%20Script%20code/Employee_page.html"
}
}