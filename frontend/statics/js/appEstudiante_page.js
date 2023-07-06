document.querySelector("#btnConsulta").addEventListener("click", consult_est)

function consult_est() {
    var id = document.getElementById("id_estudiante").value
    
    const obj = {
        "id": id,
    }

    fetch("/consult_est", {
        "method": "POST",
        "headers": {"Content-Type": "application/json"},
        "body": JSON.stringify(obj)
    })
    .then(response => response.json())
    .then(data => alert(data[1]))
}