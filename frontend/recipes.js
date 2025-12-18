document.addEventListener("DOMContentLoaded", async () => {
    const list = document.getElementById("recipes-list");
    const typeSelect = document.getElementById("recipe-type");

    async function loadRecipes(type = "") {
        try {
            let url = "http://127.0.0.1:5000/recipes";
            if (type) url += `?type=${type}`;

            const response = await fetch(url);
            const data = await response.json();

            //curatam lista
            list.innerHTML = "";

            //creem div urile pt retete
            if (response.ok && data.length > 0) {
                data.forEach(recipe => {
                    const div = document.createElement("div");
                    div.className = "recipe-item";

                    div.innerHTML = `
                        <h4>${recipe.title}</h4>
                        <p>${recipe.description}</p>
                        <small>Calorii: ${recipe.calories} | Tip: ${recipe.type}</small>
                    `;
                    list.appendChild(div);
                });
            } else {
                list.innerHTML = "<p>Nu exista retete.</p>";
            }
        } catch (error) {
            console.error("Eroare:", error);
            list.innerHTML = "<p>Eroare</p>";
        }
    }

    //initial pe toate
    loadRecipes();

    // filtru dupa tip
    if (typeSelect) {
        typeSelect.addEventListener("change", () => {
            loadRecipes(typeSelect.value);
        });
    }
});
