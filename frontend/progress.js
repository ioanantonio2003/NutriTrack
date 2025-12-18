document.addEventListener("DOMContentLoaded", async () => {
    const userId = localStorage.getItem("user_id");
    if (!userId) {
        window.location.href = "login.html";
        return;
    }

    const progressList = document.getElementById("progress-list");
    const rangeSelect = document.getElementById("progress-range");

    async function loadProgress() {
        const days = rangeSelect.value;
        try {
            const response = await fetch(`http://127.0.0.1:5000/progress?user_id=${userId}&range=${days}`);
            const data = await response.json();

            progressList.innerHTML = "";

            data.forEach(day => {
                const div = document.createElement("div");
                div.classList.add("progress-day");

                div.innerHTML = `
                    <h3>${day.date}</h3>
                    <span>🔥 Calorii: ${day.kcal.value}/${day.kcal.goal} ${day.kcal.ok ? "✅" : "❌"}</span>
                    <span>💧 Apa: ${day.water.value}/${day.water.goal} ${day.water.ok ? "✅" : "❌"}</span>
                    <span>🏃 Sport: ${day.activity.value}/${day.activity.goal} ${day.activity.ok ? "✅" : "❌"}</span>
                `;
                progressList.appendChild(div);
            });

        } catch (error) {
            console.error("Eroare:", error);
        }
    }

    rangeSelect.addEventListener("change", loadProgress);

    document.getElementById("backHomeBtn").addEventListener("click", () => {
    window.location.href = "main.html";
});

    // incarcare initiala
    loadProgress();
});
