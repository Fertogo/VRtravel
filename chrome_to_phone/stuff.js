$('body').append("TEST")
console.log("ON STUFF")

//chrome.extension.sendRequest({method: "talk", data:"hi"}); 

chrome.runtime.sendMessage({method: "talk"}, function(response){ 
	console.log("Got a response");
})