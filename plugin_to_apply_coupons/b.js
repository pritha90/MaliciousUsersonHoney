//THe js file to perform background tasks

function injectedMethod (tab, method, callback) {
    chrome.tabs.executeScript(tab.id, { file: 'data.js' }, callback);
    		
    	
}

function getBgColors (tab) {
  // When we get a result back from the getBgColors
  // method, alert the data
  injectedMethod(tab, 'getBgColors', function (response) {
    //alert(response.data);
    return true;
  });
}

// When the browser action is clicked, call the
// getBgColors function.
chrome.browserAction.onClicked.addListener(getBgColors);