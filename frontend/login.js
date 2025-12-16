document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.querySelector("form");

    loginForm.addEventListener("submit", async (e) => {
        e.preventDefault(); 

        //luam valorile din fielduri
        const name = document.getElementById("username").value;
        const password = document.getElementById("password").value;

        try {
            const response = await fetch("http://127.0.0.1:5000/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ name, password })
            });


            const data = await response.json();

            //daca avem un raspuns ok redirectionam utilizatorul la pagina principala
            if (response.ok) {
                window.location.href = "main.html";
            } else {
                alert(data.error); //mesajul de aroare
            }
        } catch (error) {
            console.error("Eroare la conectare:", error);
            alert("A aparut o eroare. Incearca din nou.");
        }
    });
});
