const uploadBtn = document.getElementById("uploadBtn");
const fileInput = document.getElementById("pdfFile");
const askBtn = document.getElementById("askBtn");
const questionInput = document.getElementById("question");
const chatBox = document.getElementById("chatBox");
const newChatBtn = document.querySelector(".new-chat");

// Upload PDF
uploadBtn.onclick = () => {
    fileInput.click();
};

fileInput.onchange = async () => {

    const file = fileInput.files[0];

    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    addBotMessage("📄 Uploading PDF...");

    try {

        const res = await fetch("http://127.0.0.1:8000/upload", {
            method: "POST",
            body: formData
        });

        const data = await res.json();

        addBotMessage("✅ " + data.message);

    } catch (err) {

        addBotMessage("❌ Upload Failed");

    }

};

// Ask Question
askBtn.onclick = askQuestion;

questionInput.addEventListener("keypress", function (e) {

    if (e.key === "Enter") {
        askQuestion();
    }

});

async function askQuestion() {

    const q = questionInput.value.trim();

    if (q === "") return;

    addUserMessage(q);

    questionInput.value = "";

    const loading = addBotMessage("Thinking...");

    try {

        const res = await fetch("http://127.0.0.1:8000/ask", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: q
            })

        });

        const data = await res.json();

        loading.innerHTML = data.answer;

    }

    catch (err) {

        loading.innerHTML = "❌ Server Error";

    }

}

// User Bubble
function addUserMessage(text) {

    const div = document.createElement("div");

    div.className = "user-message";

    div.innerHTML = text;

    chatBox.appendChild(div);

    scrollBottom();

}

// Bot Bubble
function addBotMessage(text) {

    const div = document.createElement("div");

    div.className = "bot-message";

    div.innerHTML = text;

    chatBox.appendChild(div);

    scrollBottom();

    return div;

}

function scrollBottom() {

    chatBox.scrollTop = chatBox.scrollHeight;

}

// New Chat
newChatBtn.addEventListener("click", function () {

    chatBox.innerHTML = `
        <div class="bot-message">
            👋 Hello! Upload a PDF and ask me anything about it.
        </div>
    `;

    questionInput.value = "";
    fileInput.value = "";

});