const counter = document.querySelector(".counter-number");
async function updateCounter() {
    let response = await fetch("https://hxtz3b44g5auaj36sj7nuzylu40opdbj.lambda-url.us-east-2.on.aws/");
    let data = await response.json();
    counter.innerHTML = ` This page has ${data} Views!`;
}

updateCounter();