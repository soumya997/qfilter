// capture question
let askQuestionButton = document.getElementsByClassName("puppeteer_test_add_question_button")[0];
let questionText;
console.log(askQuestionButton)
askQuestionButton.onclick = () => setTimeout(() => {
    try{
        questionText = document.getElementsByClassName("puppeteer_test_selector_input")[0];
        if(questionText){
            try{
                questionText.onchange = () => {
                    //send message to popup
                    let urlText = `https://insinceremodelapi.herokuapp.com/api?qs=${questionText.value.toString().trim().replace(/ /g, '%20')}`;
                    
                    let sincerity;
                    fetch(urlText)
                        .then(response => response.json())
                        .then(data => {
                            if(data.result>0.05){
                                sincerity=0;
                                questionText.style['color'] = "#ff0000";
                            }
                                
                            else{
                                sincerity=1;
                                questionText.style['color'] = "#00ff00";
                            }
                            // console.log(sincerity);
                        });
                    
                    //chrome.runtime.sendMessage({ sincerity: sincerity })

                }
            }catch(e){
                console.log(e);
            }    
        }
    }catch(e){}
},0);




// recieve message from background 
// chrome.runtime.onMessage.addListener(gotMessage);

// function gotMessage(message, sender, sendRequest){
//     console.log(message.msg);
// }