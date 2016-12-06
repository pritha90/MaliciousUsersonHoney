//THe js file to perform background tasks

function injectedMethod (tab, method, callback) {
    chrome.tabs.executeScript(tab.id, { file: 'data.js' }, callback);
    		
    	
}

function applyTrigger (tab) {
  injectedMethod(tab, 'applyTrigger', function (response) {
    return true;
  });
}

chrome.browserAction.onClicked.addListener(applyTrigger);
