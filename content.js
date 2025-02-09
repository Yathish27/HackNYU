async function fetchUnreadEmails() {
    const token = await getAuthToken();
    
    const response = await fetch("https://gmail.googleapis.com/gmail/v1/users/me/messages?q=is:unread", {
      headers: { Authorization: `Bearer ${token}` }
    });
  
    const data = await response.json();
    
    if (data.messages) {
      data.messages.forEach(async (message) => {
        const emailDetails = await fetchEmailDetails(message.id, token);
        analyzeEmail(emailDetails.snippet); // Analyze email snippet
      });
    }
  }
  
  async function getAuthToken() {
    return new Promise((resolve, reject) => {
      chrome.identity.getAuthToken({ interactive: true }, (token) => {
        if (chrome.runtime.lastError || !token) reject(chrome.runtime.lastError);
        resolve(token);
      });
    });
  }
  
  async function fetchEmailDetails(messageId, token) {
    const response = await fetch(`https://gmail.googleapis.com/gmail/v1/users/me/messages/${messageId}`, {
      headers: { Authorization: `Bearer ${token}` }
    });
  
    return await response.json();
  }
  