const input = document.getElementById("notation-input");
const rollBtn = document.getElementById("btn-roll");
const errorEl = document.getElementById("error-text");
const resultCard = document.getElementById("result-card");
const resultTotal = document.getElementById("result-total");
const resultMeta = document.getElementById("result-meta");
const dieRow = document.getElementById("die-row");

function setError(message) {
  errorEl.hidden = !message;
  errorEl.textContent = message || "";
}

function formatMeta(data) {
  const parts = data.rolls.join(", ");
  let text = `${data.notation} — dice: ${parts}`;
  if (data.modifier > 0) {
    text += ` + ${data.modifier}`;
  } else if (data.modifier < 0) {
    text += ` ${data.modifier}`;
  }
  text += ` (sum ${data.subtotal})`;
  return text;
}

async function roll() {
  setError(null);
  const notation = input.value.trim();
  if (!notation) {
    setError("Enter dice notation first.");
    input.focus();
    return;
  }

  rollBtn.disabled = true;
  try {
    const res = await fetch("/api/roll", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ notation }),
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(data.detail || "Roll failed.");

    resultCard.hidden = false;
    resultTotal.textContent = String(data.total);
    resultMeta.textContent = formatMeta(data);

    dieRow.innerHTML = "";
    data.rolls.forEach((value) => {
      const die = document.createElement("span");
      die.className = "die";
      die.textContent = String(value);
      dieRow.appendChild(die);
    });
  } catch (err) {
    setError(err.message || "Roll failed.");
  } finally {
    rollBtn.disabled = false;
  }
}

document.querySelectorAll(".chip").forEach((chip) => {
  chip.addEventListener("click", () => {
    input.value = chip.dataset.notation || "";
    input.focus();
  });
});

rollBtn.addEventListener("click", () => roll());
input.addEventListener("keydown", (event) => {
  if (event.key === "Enter") roll();
});
