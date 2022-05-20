
//onload
window.onload = function () {
    var url = document.location.href,
        params = url.split('?')[1].split('&'),
        data = {}, tmp;
    for (var i = 0, l = params.length; i < l; i++) {
         tmp = params[i].split('=');
         data[tmp[0]] = tmp[1];
    }
    let employee = data["employee"]
    employee = employee.replaceAll('%22','"')
    employee = JSON.parse(employee)
    level =data["level"]
    console.log(level)
    console.log(employee)
    const id = employee.employeeId
    const aprover = {
        departmentId: employee.departmentId,
        employeeId: employee.employeeId,
        firstName: employee.firstName,
        lastName: employee.lastName,
        password: employee.password,
        position: employee.position,
        superviserCode: employee.superviserCode,
        username: employee.username
    }
    console.log(id)
    employeeInfoGet(aprover) 
    if (level != "E")
    {
        document.getElementById("approval-section").style.display= "block"
        // needs a try catch block to test admin request.
        adminRequest(aprover)
        document.getElementById("storedpos").innerText = level
    }
    else if(level = "E"){
        document.getElementById("employee-request").style.display= "block"
        // needs a try catch block to test admin request.
        yourRequest(id)
        document.getElementById("storedpos").innerText = level 

    }



}

// ui setup start
 function employeeInfoGet(aprover){
   document.getElementById("display-name").innerText = `Firstname: ${aprover.firstName} LastName: ${aprover.lastName} EmployeeID: ${aprover.employeeId} Department: ${aprover.departmentId}`
   document.getElementById("storedid").innerText = aprover.employeeId
   document.getElementById("storedde").innerText = aprover.departmentId   
}
async function  yourRequest(id){
    const tbody = document.getElementById("your-request-body")

    const url = `http://localhost:5000/employee/${id}/request`

    const httpResponse = await fetch(url)

    const rows = await httpResponse.json()

    console.log(rows)
    tbody.innerHTML= ""
    for (const row of rows) {
        console.log(row)
        console.log(typeof row)
        const rowElement= document.createElement("tr")
        // request id
        const celElement0= document.createElement("td")
        celElement0.innerText= row.RequestId
        rowElement.appendChild(celElement0)
        // EmployeeId
        const celElement1= document.createElement("td")
        celElement1.innerText= row.EmployeeId
        rowElement.appendChild(celElement1)
        // EmployType
        const celElement2= document.createElement("td")
        celElement2.innerText= row.EventType
        rowElement.appendChild(celElement2)
        //EventCost
        const celElement3= document.createElement("td")
        celElement3.innerText= row.EventCost
        rowElement.appendChild(celElement3)
        //Event Reimbursment
        const celElement4= document.createElement("td")
        celElement4.innerText= row.CoveredAmount
        rowElement.appendChild(celElement4)        
        //Event grade
        const celElement5= document.createElement("td")
        celElement5.innerText= row.EmployeeGrade
        rowElement.appendChild(celElement5)
        //Event RequestStatus
        const celElement6= document.createElement("td")
        celElement6.innerText= row.RequestStatus
        rowElement.appendChild(celElement6)
        // EventDate
        const celElement7= document.createElement("td")
        celElement7.innerText= row.EventDate
        rowElement.appendChild(celElement7)
        //EventTime      
        const celElement8= document.createElement("td")
        celElement8.innerText= row.EventTime
        rowElement.appendChild(celElement8)
        //EventLocal      
        const celElement9= document.createElement("td")
        celElement9.innerText= row.EventLocal
        rowElement.appendChild(celElement9)        
        tbody.appendChild(rowElement)
        //EventDescription      
        const celElement10= document.createElement("td")
        celElement10.innerText= row.EventDescription
        rowElement.appendChild(celElement10)
        //GradeType
        const celElement11= document.createElement("td")
        celElement11.innerText= row.GradeType
        rowElement.appendChild(celElement11)

        tbody.appendChild(rowElement)        
    }
}
async function adminRequest(aprover){
    const tbody = document.getElementById("admin-request")
    
    const url = `http://localhost:5000/employee/request/${aprover.employeeId}/${aprover.position}/${aprover.departmentId}`
    const httpResponse = await fetch(url);

    const rows = await httpResponse.json()

    console.log(rows)
    tbody.innerHTML= ""
    for (const row of rows) {
        console.log(row)
        console.log(typeof row)
        const rowElement= document.createElement("tr")
        // request id
        const celElement0= document.createElement("td")
        celElement0.innerText= row.RequestId
        rowElement.appendChild(celElement0)
        // EmployeeId
        const celElement1= document.createElement("td")
        celElement1.innerText= row.EmployeeId
        rowElement.appendChild(celElement1)
        // EmployType
        const celElement2= document.createElement("td")
        celElement2.innerText= row.EventType
        rowElement.appendChild(celElement2)
        //EventCost
        const celElement3= document.createElement("td")
        celElement3.innerText= row.EventCost
        rowElement.appendChild(celElement3)
        //Event Reimbursment
        const celElement4= document.createElement("td")
        celElement4.innerText= row.CoveredAmount
        rowElement.appendChild(celElement4)        
        //Event grade
        const celElement5= document.createElement("td")
        celElement5.innerText= row.EmployeeGrade
        rowElement.appendChild(celElement5)
        //Event RequestStatus
        const celElement6= document.createElement("td")
        celElement6.innerText= row.RequestStatus
        rowElement.appendChild(celElement6)
        // EventDate
        const celElement7= document.createElement("td")
        celElement7.innerText= row.EventDate
        rowElement.appendChild(celElement7)
        //EventTime      
        const celElement8= document.createElement("td")
        celElement8.innerText= row.EventTime
        rowElement.appendChild(celElement8)
        //EventLocal      
        const celElement9= document.createElement("td")
        celElement9.innerText= row.EventLocal
        rowElement.appendChild(celElement9)        
        tbody.appendChild(rowElement)
        //EventDescription      
        const celElement10= document.createElement("td")
        celElement10.innerText= row.EventDescription
        rowElement.appendChild(celElement10)
        //GradeType
        const celElement11= document.createElement("td")
        celElement11.innerText= row.GradeType
        rowElement.appendChild(celElement11)

        tbody.appendChild(rowElement)        
    }
}

//ui setup end

//form toggle start 
function ToggleRequestOn(){
document.querySelector('.mobel-bg').style.display = 'flex';
document.querySelector('#request_form').style.display = 'block';
}

function ToggleOff(){
    document.querySelector('.mobel-bg').style.display = 'none';
    document.querySelector('#request_form').style.display = 'none';
    document.querySelector('#update_form').style.display = 'none';
    document.querySelector('#close_form').style.display = 'none';
    document.querySelector('#Adjuster').style.display = 'none';
    document.querySelector('#Approver').style.display = 'none';
}

function ToggleUpdateOn(){
    document.querySelector('.mobel-bg').style.display = 'flex';
    document.querySelector('#update_form').style.display = 'block';
    }

function ToggleCloseRequest(){
    document.querySelector('.mobel-bg').style.display = 'flex';
    document.querySelector('#close_form').style.display = 'block';
    }

function ToggleAdjuster(){
        document.querySelector('.mobel-bg').style.display = 'flex';
        document.querySelector('#Adjuster').style.display = 'block';
    }

function ToggleApproverOn(){
            document.querySelector('.mobel-bg').style.display = 'flex';
            document.querySelector('#Approver').style.display = 'block';
    }
//form toggle end

//-----database requests----
async function PostRequest(){
const id = document.getElementById("storedid").innerText
console.log(id)
const type = document.getElementById("R_event_type").value
const Cost = document.getElementById("R_event_cost").value
const date = document.getElementById("R_event_date").value
const time = document.getElementById("R_event_time").value
const location = document.getElementById("R_event_location").value
const description = document.getElementById("R_event_description").value
const GradeType = document.getElementById("R_event_grading_type").value
const data = {
    "requestid": 0,
    "eventType": type,
    "eventDate": date,
    "eventTime": time,
    "eventLocation": location,
    "eventCost": Cost,
    "eventReimbersment": 0,
    "eventGradingType": GradeType,
    "requestStatus": "pending super",
    "eventDescription": description
}

const url = `http://localhost:5000/employee/${id}/request/`
const httpResponse = await fetch(url, {method: "POST",
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
});

const responce = await httpResponse.json()
console.log(responce)
if(responce){
    alert("Request Successfully submitted!")
    ToggleOff()
    yourRequest(id)
} else {
    alert("Request Failed to be submitted.")
}

}

async function updateSubmit(){
    const id = document.getElementById("storedid").innerText
    console.log(id)
    const rid = document.getElementById("update-Requestid").value
    const type = document.getElementById("Update_event_type").value
    const Cost = document.getElementById("Update_event_cost").value
    const date = document.getElementById("Update_event_date").value
    const time = document.getElementById("Update_event_time").value
    const location = document.getElementById("Update_event_location").value
    const description = document.getElementById("Update_event_description").value
    const GradeType = document.getElementById("Update_event_grading_type").value
    const Grade = document.getElementById("Update_event_grading").value
    const data = {
        "employeeGrade": Grade,
        "eventType": type,
        "eventDate": date,
        "eventTime": time,
        "eventLocation": location,
        "eventCost": Cost,
        "eventReimbersment": 0,
        "eventGradingType": GradeType,
        "requestStatus": "",
        "eventDescription": description
    }
    console.log(data)
    const url = `http://localhost:5000/employee/${id}/request/${rid}`
    const httpResponse = await fetch(url, {method: "PUT",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    });
    
    const responce = await httpResponse.json()
    console.log(responce)
    if(responce){
        alert("Upated Successfully submitted!")
        ToggleOff()
        yourRequest(id)
    } else {
        alert("Update Failed to be submitted.")
    }
    
    }

async function RemoveRequest(){
    const id = document.getElementById("storedid").innerText
const rid = document.getElementById("Close-Requestid").value
console.log(rid)

const url = `http://localhost:5000/employee/${id}/request/${rid}`
const httpResponse = await fetch(url, {method: "DELETE",
    headers: {
        'Content-Type': 'application/json'
    },
});
    yourRequest(id)

}
async function AproveRequest() {
const rid = document.getElementById("Approve-Requestid").value
const id = document.getElementById("storedid").innerText
const level = document.getElementById("storedpos").innerText
const dep = document.getElementById("storedde").innerText

const url = `http://localhost:5000/employee/request/${rid}/${id}/${level}/${dep}`
const httpResponse = await fetch(url, {method: "PUT",
headers: {
    'Content-Type': 'none'
},
});

const responce = await httpResponse.json()
console.log(responce)

if(responce){
    alert(`Aproval of ${level} Successful`)
    const aprover = {
        employeeId : id,
        departmentId : dep,
        position : level
    }
    ToggleOff()
    adminRequest(aprover)
} else {
    alert("Update Failed to be submitted.")
}
}

async function adjusting(){
    const rid = document.getElementById("Adjust-Requestid").value
    const comp = document.getElementById("Adjust-reimbursment").value
    const level = document.getElementById("storedpos").innerText
    const dep = document.getElementById("storedde").innerText
    const id = document.getElementById("storedid").innerText
    
    const aprover = {
        employeeId : id,
        departmentId : dep,
        position : level
    }

    const url = `http://localhost:5000/employee/request/adjust/${rid}/${comp}`
const httpResponse = await fetch(url, {method: "PUT",
headers: {
    'Content-Type': 'none'
},
});

const responce = await httpResponse.json()
console.log(responce)

if(responce){
    alert(`Adjustment submited`)
    ToggleOff()
    adminRequest(aprover)
} else {
    alert("Update Failed to be submitted.")
}
}


//
//Event Listeners start
addrequest = document.getElementById("addrequest")
addrequest.addEventListener('click', ToggleRequestOn);

updateRequest = document.getElementById("updaterequest")
updateRequest.addEventListener('click', ToggleUpdateOn);

CloseRequest = document.getElementById("requestCloser")
CloseRequest.addEventListener('click', ToggleCloseRequest);

Adjuster = document.getElementById("Adjust")
Adjuster.addEventListener('click', ToggleAdjuster);


closer = document.querySelectorAll(".close");
closer.forEach(element => {
    element.addEventListener('click', ToggleOff);   
});

Approve = document.getElementById("aprove")
Approve.addEventListener('click', ToggleApproverOn);


CloseAdmin = document.getElementById("requestCloser")
CloseAdmin.addEventListener('click', ToggleCloseRequest);

addbutton = document.getElementById("NewRequest")
addbutton.addEventListener('click', PostRequest)

RemoveEm = document.getElementById("deleteEm")
RemoveEm.addEventListener('click', RemoveRequest)

UpdateEM = document.getElementById("UpdateBUT")
UpdateEM.addEventListener('click', updateSubmit)

AproveSubmit = document.getElementById("AproveSub")
AproveSubmit.addEventListener('click', AproveRequest)

adjustSub = document.getElementById("adjustz")
adjustSub.addEventListener('click', adjusting)
//Event Listeners end
