async function spinWheel() {

    const input = document.getElementById("options").value;

    console.log("Raw input:", input);

    const options = input
        .split(",")
        .map(opt => opt.trim())
        .filter(opt => opt.length > 0);

    console.log("Processed options:", options);

    if (options.length === 0) {
        alert("Please enter valid options!");
        return;
    }

    try {
        const response = await fetch("/spin", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ options: options })
        });

        const data = await response.json();

        console.log("Backend response:", data);

        if (data.error) {
            alert(data.error);
            return;
        }

        document.getElementById("result").innerText =
            "🎯 Result: " + data.result;

    } catch (error) {
        console.error("Error:", error);
    }
}