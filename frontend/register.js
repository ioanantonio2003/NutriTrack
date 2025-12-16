document.addEventListener("DOMContentLoaded", () => {
    const registerForm = document.getElementById("registerForm");

    registerForm.addEventListener("submit", async (e) => {
        e.preventDefault(); // prevenim reload-ul paginii la submit

        //luam valorile din fielduri
        const name = document.getElementById("username").value;
        const password = document.getElementById("password").value;
        const age = parseInt(document.getElementById("age").value);

        try {
            const response = await fetch("http://127.0.0.1:5000/register", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ name, password, age })
            });

            const data = await response.json();

            //daca avem un raspuns ok redirectionam utilizatorul sa se conecteze
            if (response.ok) {
                window.location.href = "login.html";
            } else {
                alert(data.error); //mesaj de aroare
            }
        } catch (error) {
            console.error("Eroare la înregistrare:", error);
            alert("A aparut o eroare. Incearca din nou.");
        }
    });
});
