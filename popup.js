document.getElementById("analyzeButton").addEventListener("click", async () => {
    const emailContent = document.getElementById("emailContent").value;
    
    if (!emailContent.trim()) {
      alert("Please enter email content.");
      return;
    }
  
    // Send email content to background script for analysis
    chrome.runtime.sendMessage({ action: "analyzeEmail", content: emailContent }, (response) => {
      if (response.error) {
        document.getElementById("result").innerText = `Error: ${response.error}`;
      } else {
        const { spam, phishing } = response;
        document.getElementById("result").innerHTML = `
          <p><strong>Spam Analysis:</strong> ${spam.label} (Confidence: ${spam.confidence}%)</p>
          <p><strong>Phishing Analysis:</strong> ${phishing.label} (Confidence: ${phishing.confidence}%)</p>
        `;
      }
    });
  });
  