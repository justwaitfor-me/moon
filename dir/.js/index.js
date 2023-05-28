const style = document.getElementById("style_1"); //Save a HTML Element in an variable
const button_style = document.getElementById("button");
const div_change = document.getElementById("style_2");
const Input_3 = document.getElementById("Input_3");
function change_back() {
    style.innerHTML = "body {color:white; background-color: black;}";
    button_style.innerHTML = "<button id='button' onclick='change_back_back()'>change background-color</button>";
}

function change_back_back() {
    style.innerHTML = "body {color:black; background-color: aliceblue;}";
    button_style.innerHTML = "<button id='button' onclick='change_back()'>change background-color</button>";
}

function change_to_self() {
    var inputField_3 = Input_3; //save the Input Field
    var style_change = inputField_3.value; //save the value of the Input Fi
    div_change.innerHTML = style_change;
}