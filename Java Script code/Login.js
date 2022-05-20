async function getlogin() {
    const username = document.getElementById("username").value
    const password = document.getElementById("password").value

    const url = `http://localhost:5000/login/${username}/${password}`;

    const httpResponse = await fetch(url);
    const body = await httpResponse.json();
    console.log(body);

    if (body.LoginStatus == 'true'){
        var level = body.Level
        var employee = body.employee

        window.location.href = "file:///F:/Projects/Java%20Script%20code/Employee_page.html?employee="+ JSON.stringify(employee) +"&level=" + level
    }
}