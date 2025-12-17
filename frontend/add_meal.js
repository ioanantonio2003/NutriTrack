document.addEventListener("DOMContentLoaded", () => {
    const mealSearch = document.getElementById("meal-search");
    const mealSuggestions = document.getElementById("meal-suggestions");
    const mealAmount = document.getElementById("meal-amount");
    const addMealForm = document.getElementById("addMealForm");

    const userId = localStorage.getItem("user_id"); // id ul dupa login

    let allMeals = [];

    // lista alimentelor din baza de date
    async function loadMeals() {
        try {
            const response = await fetch("http://127.0.0.1:5000/meals");
            const data = await response.json();
            allMeals = data.meals;
        } catch (error) {
            console.error("EROARE:", error);
        }
    }

    loadMeals();

    // sugestii
    mealSearch.addEventListener("input", () => {
        const query = mealSearch.value.toLowerCase();
        mealSuggestions.innerHTML = "";

        if (query.length === 0) return;

        const filtered = allMeals.filter(meal => meal.name.toLowerCase().includes(query));

        filtered.forEach(meal => {
            const li = document.createElement("li");
            li.textContent = meal.name;
            li.addEventListener("click", () => {
                mealSearch.value = meal.name;
                mealSuggestions.innerHTML = "";
            });
            mealSuggestions.appendChild(li);
        });
    });

    // Aduagam masa
    addMealForm.addEventListener("submit", async (e) => {
        e.preventDefault();

        const mealName = mealSearch.value.trim();
        const amount = parseFloat(mealAmount.value);

        if (!mealName || !amount) {
            alert("Completeaza corect");
            return;
        }

        try {
            const response = await fetch("http://127.0.0.1:5000/add_meal", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ user_id: userId, name: mealName, amount })
            });

            const data = await response.json();

            if (response.ok) {
                mealSearch.value = "";
                mealAmount.value = "";
            } else {
                alert(data.error);
            }
        } catch (error) {
            console.error("Eroare:", error);
        }
    });
});