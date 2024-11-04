async function getPrediction() {
    // Recover values
    const data = {
        MedInc: parseFloat(document.getElementById("MedInc").value),
        HouseAge: parseFloat(document.getElementById("HouseAge").value),
        AveRooms: parseFloat(document.getElementById("AveRooms").value),
        AveBedrms: parseFloat(document.getElementById("AveBedrms").value),
        Population: parseFloat(document.getElementById("Population").value),
        AveOccup: parseFloat(document.getElementById("AveOccup").value),
        Latitude: parseFloat(document.getElementById("Latitude").value),
        Longitude: parseFloat(document.getElementById("Longitude").value)
    };

    try {
        // Send the POST request
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        // Extract JSON response
        const result = await response.json();
        document.getElementById("prediction-value").innerText = `$${(result.prediction*100).toFixed(0)}k`;

        document.getElementById("prediction-result").style.display = "block";
    } catch (error) {
        console.error("Erreur lors de la prédiction :", error);
    }
}
