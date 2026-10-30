
document.addEventListener("DOMContentLoaded", async function () {

    try {
        const response = await fetch("/api/dashboard");

        if (!response.ok) {
            throw new Error("Dashboard API error");
        }

        const data = await response.json();

        document.getElementById("totalVehicles").textContent =
            data.total_vehicles;

        document.getElementById("totalTransactions").textContent =
            data.total_transactions;

        document.getElementById("totalRevenue").textContent =
            "₹" + data.total_revenue;

        document.getElementById("totalBooths").textContent =
            data.total_booths;

        console.log("Dashboard data loaded:", data);

    } catch (error) {
        console.error("Error loading dashboard:", error);
    }

});
