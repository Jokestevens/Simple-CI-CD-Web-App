const btn = document.getElementById("btn");
const out = document.getElementById("output");

btn.addEventListener("click", async () => {
  out.textContent = "Calling backend...";
  try {
    // IMPORTANT:
    // We call "/api/hello" on the same origin.
    // Nginx will reverse-proxy /api/* to the backend container.
    const res = await fetch("/api/hello");
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    out.textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    out.textContent = `Error: ${err.message}`;
  }
});
