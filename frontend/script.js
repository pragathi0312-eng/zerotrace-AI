async function scanCode(){

    const folder =
        document.getElementById("folderPath").value;

    const response = await fetch(
        "http://127.0.0.1:5000/scan",
        {
            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({
                folder:folder
            })
        }
    );

    const data = await response.json();

    document.getElementById("output")
        .innerText =
        JSON.stringify(data, null, 2);
}