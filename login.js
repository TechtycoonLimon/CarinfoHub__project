// ── Register ──
async function register() {
    const email    = document.getElementById("login-email").value;
    const password = document.getElementById("login-password").value;

    const res  = await fetch("http://localhost:5000/register", {
        method:  "POST",
        headers: { "Content-Type": "application/json" },
        body:    JSON.stringify({ email, password })
    });

    const data = await res.json();
    document.getElementById("login-message").innerText = data.message;
}

// ── Login ──
async function login() {
    const email    = document.getElementById("login-email").value;
    const password = document.getElementById("login-password").value;

    const res  = await fetch("http://localhost:5000/login", {
        method:  "POST",
        headers: { "Content-Type": "application/json" },
        body:    JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (res.ok) {
        document.getElementById("login-page").style.display = "none";
    } else {
        document.getElementById("login-message").innerText = data.message;
    }
}
