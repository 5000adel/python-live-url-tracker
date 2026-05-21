document.getElementById('sendBtn').addEventListener('click', async () => {
const statusText = document.getElementById('status');
statusText.innerText = "Sending...";

  try {
    // 1. Get the current active tab
    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    
    // 2. Send the URL to the Python server
    let response = await fetch('http://127.0.0.1:5000/receive-url', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ url: tab.url })
    });

    if (response.ok) {
      statusText.innerText = "✅ Sent successfully!";
    } else {
      statusText.innerText = "❌ Failed to send.";
    }
  } catch (error) {
    statusText.innerText = "❌ Error! Is Python running?";
    console.error(error);
  }
});
