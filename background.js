chrome.runtime.onMessage.addListener(async (message, sender, sendResponse) => {
    if (message.action === "analyzeEmail") {
      try {
        const response = await fetch("1069159049068-1vvrtv6bsn1c4jrn9td45smeija45je1", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ content: message.content })
        });
  
        if (!response.ok) throw new Error("Failed to analyze email.");
  
        const result = await response.json();
        sendResponse(result);
      } catch (error) {
        sendResponse({ error: error.message });
      }
      
      return true; // Keep the message channel open for async response
    }
  });
  