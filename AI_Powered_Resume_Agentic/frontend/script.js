let currentTab = "manual";

function showTab(tab) {
    currentTab = tab;

    document.querySelectorAll(".tab").forEach(btn => {
        btn.classList.remove("active");
    });

    document.querySelectorAll(".tab-content").forEach(content => {
        content.classList.remove("active");
    });

    if (tab === "manual") {
        document.querySelectorAll(".tab")[0].classList.add("active");
        document.getElementById("manual").classList.add("active");
    } else {
        document.querySelectorAll(".tab")[1].classList.add("active");
        document.getElementById("upload").classList.add("active");
    }
}

async function generate() {
    const output = document.getElementById("output");
    output.innerText = "Processing...";

    try {
        if (currentTab === "manual") {
            const data = {
                name: document.getElementById("name").value,
                education: document.getElementById("education").value,
                skills: document.getElementById("skills").value,
                experience: document.getElementById("experience").value,
                projects: document.getElementById("projects").value
            };

            const response = await fetch("http://localhost:8000/enhance", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            output.innerText = result.enhanced;

        } else {
            const fileInput = document.getElementById("resumeFile");
            const formData = new FormData();
            formData.append("file", fileInput.files[0]);

            const response = await fetch("http://localhost:8000/upload", {
                method: "POST",
                body: formData
            });

            const result = await response.json();
            output.innerText = result.enhanced;
        }
    } catch (err) {
        output.innerText = "Error processing request.";
        console.error(err);
    }
}
