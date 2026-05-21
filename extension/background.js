// Helper function to send the URL to your Python server
async function sendUrl(url) {
// Don't send internal browser pages like chrome://settings
if (!url || url.startsWith('chrome://') || url.startsWith('edge://')) return;

  try {
    await fetch('http://127.0.0.1:5000/receive-url', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url: url })
    });
    console.log("✅ Sent:", url);
  } catch (error) {
    console.log("❌ Error connecting to Python:", error);
  }
}

// Trigger 1: When you switch to a different tab
chrome.tabs.onActivated.addListener(async (activeInfo) => {
  try {
    let tab = await chrome.tabs.get(activeInfo.tabId);
    if (tab.url) sendUrl(tab.url);
  } catch (error) {
    console.error("Error getting tab:", error);
  }
});

// Trigger 2: When the webpage you are looking at changes its URL
chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  // Only send if the URL actually changed and the tab is currently active
  if (changeInfo.url && tab.active) {
    sendUrl(changeInfo.url);
  }
});
