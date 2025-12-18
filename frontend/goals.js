//functie pentru updatarea goalurilor
document.addEventListener("DOMContentLoaded", () => {
    const userId = localStorage.getItem("user_id"); // luam user din localstorage

    document.getElementById("updateGoalsBtn")
        .addEventListener("click", async () => {

            const kcal = document.getElementById("kcalGoal").value;
            const water = document.getElementById("waterGoal").value;
            const activity = document.getElementById("activityGoal").value;

            if (!kcal || !water || !activity) {
                alert("COMPLETEAZA TOT");
                return;
            }

            try {
                const response = await fetch(
                    "http://127.0.0.1:5000/update_goals",
                    {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({
                            user_id: userId,
                            kcal_goal: kcal,
                            water_goal: water,
                            activity_goal: activity
                        })
                    }
                );

                if (response.ok) {

                    document.getElementById("kcalGoal").value = "";
                    document.getElementById("waterGoal").value = "";
                    document.getElementById("activityGoal").value = "";
                } else {
                    alert("Eroare");
                }
            } catch (err) {
                console.error(err);
                alert("Eroare");
            }
        });
});
