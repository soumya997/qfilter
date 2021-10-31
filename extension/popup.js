let questionPop=document.getElementById("ques");
let sincere=document.getElementById("sincere");
let insincere=document.getElementById("insincere");
let fix=document.getElementById("fix");

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    console.log(message);
});

// fetch(APIurl).then(res => console.log(res));