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
    .then(data => notas_est(data))
}

function notas_est(dato)    {
    let txtWeb = dato[2]
    let txtMovil = dato[3]
    let txtDesktop = dato[4]

    document.getElementById("web").value = txtWeb
    document.getElementById("movil").value = txtMovil
    document.getElementById("desktop").value = txtDesktop
}