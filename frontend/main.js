document.addEventListener("DOMContentLoaded", () => {

    const streakText = document.getElementById("streak-text");

    //id ul salvat din locatStoarge de la login
    const userId = localStorage.getItem("user_id");

    if (!userId) {
        //daca cineva itnra direct in main se duce la login
        window.location.href = "login.html";
        return;
    }

    //functie pentru streak
    async function loadStreak() {
        try {
            const response = await fetch(
                `http://127.0.0.1:5000/streak?user_id=${userId}`
            );

            const data = await response.json();
            //daca raspunsul este ok schimbam valoarea 
            if (response.ok) {
                streakText.textContent = `🔥 Streak: ${data.streak} zile`;
            } else {
                streakText.textContent = "🔥 Eroare streak";
            }
        } catch (error) {
            console.error("Eroare la streak:", error);
        }
    }

    //functie pentru goal urile generale
   async function loadGoals() {
        try {
            const response = await fetch(`http://127.0.0.1:5000/goals?user_id=${userId}`);
            const data = await response.json();
            //daca raspunsul este ok schimbam goal urile generale
            if (response.ok) {
                document.getElementById("kcal-goal").textContent = data.kcal_goal;
                document.getElementById("water-goal").textContent = data.water_goal;
                document.getElementById("sport-goal").textContent = data.activity_goal;
            } else {
                console.error("EROARE");
            }
        } catch (error) {
            console.error("EROAREE:", error);
        }
    }

    //functie pt updatarea panelului prinicpal 
    async function updateProgressPanel() {
        const userId = localStorage.getItem("user_id");
        if (!userId) return;

        try {
            const response = await fetch(`http://127.0.0.1:5000/progress?user_id=${userId}&range=1`);
            const data = await response.json();

            if (response.ok && data.length > 0) {
                const todayData = data[0]; //luam doar progresul de astazi
                //updatam
                document.getElementById("kcal-current").textContent = todayData.kcal.value;
                document.getElementById("water-current").textContent = todayData.water.value;
                document.getElementById("sport-current").textContent = todayData.activity.value;
            } else {
                //daca azi nu s a facut nicio data
                document.getElementById("kcal-current").textContent = 0;
                document.getElementById("water-current").textContent = 0;
                document.getElementById("sport-current").textContent = 0;
            }
        } catch (error) {
            console.error("Eroare:", error);
        }
}


    const addWaterBtn = document.getElementById("addWaterBtn");
    const waterInput = document.getElementById("waterAmount");
    //functie pentru adaugarea de apa
    addWaterBtn.addEventListener("click", async () => {
        const amount = parseFloat(waterInput.value);
        //daca nu s a introdus o cantitate valida
        if (!amount || amount <= 0) {
            alert("CANTITATE IVNALIDA");
            return;
        }

        try {
            await fetch("http://127.0.0.1:5000/add_water", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    user_id: userId,
                    water: amount
                })
            });

            waterInput.value = "";

            //modificam streakul si progress panelul dupa daugarea
            loadStreak();
            updateProgressPanel();

        } catch (error) {
            alert("Eroare");
        }
    });

    //calorii per minut pentru variante
   const activityCaloriesPerMinute = {
    "mers": 0.4,
    "alergat": 3,
    "inot": 2,
    "ciclism": 7,
    "fotbal": 9,
    "dans": 6,
    "sala": 8
};

const addActivityBtn = document.getElementById("addActivityBtn");
const activityTypeInput = document.getElementById("activityType");
const activityMinutesInput = document.getElementById("activityMinutes");

addActivityBtn.addEventListener("click", async () => {
    const type = activityTypeInput.value;
    const minutes = parseInt(activityMinutesInput.value);

    if (!type) {
        alert("Alege activitatea!");
        return;
    }
    if (!minutes || minutes <= 0) {
        alert("MINUTE INVALIDE");
        return;
    }

    //calculcam valoarea
    const calPerMinute = activityCaloriesPerMinute[type] || 5;
    const activityCal = minutes * calPerMinute;

    try {
        const response = await fetch("http://127.0.0.1:5000/add_activity", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ user_id: localStorage.getItem("user_id"), activity_cal: activityCal })
        });

        const data = await response.json();

        if (response.ok) {
            //updatam progress panel si verificam sa fie actualizat si streakul
            updateProgressPanel();
            loadStreak();
        } else {
            alert(data.error);
        }
    } catch (error) {
        alert("EROARE");
    }
});

    //LA INCARCAREA PAGINII
    loadStreak();
    loadGoals();
    updateProgressPanel();
});
