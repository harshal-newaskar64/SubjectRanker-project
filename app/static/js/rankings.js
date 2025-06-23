document.getElementById('feedback-form').onsubmit = async e => {
  e.preventDefault();
  const text = document.getElementById('feedback').value;
  const res  = await fetch("/feedback", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ feedback: text })
  });
  if (res.ok) {
    document.getElementById('feedback-msg').innerText = "Thanks for your feedback!";
    document.getElementById('feedback').value = "";
  } else {
    document.getElementById('feedback-msg').innerText = "Error—please try again.";
  }
};
