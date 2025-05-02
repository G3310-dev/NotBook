let timeLeft = 60;
const countdownEl = document.getElementById("countdown");
const gameForm = document.getElementById("game-form");
const timeoutMessage = document.getElementById("timeout-message");

const timer = setInterval(() => {
    timeLeft--;
    countdownEl.textContent = `⏳ ${timeLeft}s`;

    if (timeLeft <= 0) {
        clearInterval(timer);
        gameForm.style.display = "none";
        timeoutMessage.style.display = "block";
    }
}, 1000);