// Step1: print somthing
console.log('Hello World'); //out: Hello World

// note: use node to run js code on a machine
    // Example: $ node main.js

// Step 2: variables
let name = 'JustWait';
console.log(name); //out: JustWait

let firstname = 'Just';
let lastname = 'Wait';

let string = "this is a string";
let integer = 30;
let boolean = false; //or true
let notdefined; // undefined (let undefined = undefined;)
let variable = null; // null is a placeholder, change it afterward

// Step 3: const
    //const can't be changed
const Rate = 0.3;
console.log(Rate); //out: 0.3

// Step 4: Object
let /*or cost*/ person = {
    name: /*this is the key*/ "JustWait", /*this is the value*/
    age: 14
};
console.log(person); //out: { name: 'JustWait', age: 14 }

// Step 4.1: dot notation
person.name = "JustWait1" // change the value of an object
console.log(person.name); // read the value of an object //out: JustWait1

// Step 4.2: Bracket Notation
let selection = "name" // example
person[selection] = "JustWait2"; //change the value of an object, but select the value's name by a variable

console.log(person.name); //out: JustWait2

// Step 5: Arrays
let Arrey = ["test1", "test2"]; //the variable is now an array

console.log(Arrey); //out: [ 'test1', 'test2' ]

//Step 5.1: index of an object
console.log(Arrey[0]/*this is the index. The Index starts at 0*/); //out: test1
console.log(Arrey[1]); //out: test2

//Step 5.2 Change or add an object by the index
    //add
Arrey[2] = "test3";
console.log(Arrey); //out: [ 'test1', 'test2', 'test3' ]
    //change
Arrey[0] = "test1 (changed)";
console.log(Arrey); //out: [ 'test1 (changed)', 'test2', 'test3' ]

// note: you can store any type of object in an array (str, int, ...)

//Step 5.3: length
let length = Arrey.length/*the length of the Arrey*/;
console.log(length); //out: 3


//Step 6: Functions
function happy1() {      //start
    //this is a Funktion called happy
    console.log("call me to be happy!");
}                       //end

happy1(); //call the Function //out: call me to be happy!

//Step 6.1: Parameters
function happy2(name /*this is the parameter of this function, you can give it an value*/) {    //start
    console.log("hey " + name + ", you make me so happy!")
}                                                                                               //end

//by calling the function with a value, the parameter gets the value
happy2("JustWait1"); //out: hey JustWait1, you make me so happy!
happy2("JustWait2"); //out: hey JustWait2, you make me so happy!
happy2("JustWait3"); //out: hey JustWait3, you make me so happy!

//Step 6.2: Returning a value of a Function
function happy3(number1, number2) { //start
    return number1 + number2; //returning a Answer to the Caller
}           	                    //end

console.log(happy3(6, 8)) //print the Answer by Calling the Function wit parameters //out: 14

//Step 7: innerHTML
    //get
let html = document.getElementById("titel_1" /*This is the ObjectId*/).innerHTML; //get the HTML out of an HTML Code and save as a variable
console.log(html); //print the code inside the tag //out: Hi, User!
    //change
document.getElementById("change_1").innerHTML = "javascript is != Java"; //change the Content of an HTML Tag
    //save in a variable 
const element_1 = document.getElementById("titel_1"); //Save a HTML Element in an variable
const element_2 = document.getElementById("Input_1");
    //call from HTML / get from HTML
function getValue() {                    //start
    var inputField = element_2; //save the Input Field
    var name = inputField.value; //save the value of the Input Field
    console.log(name); //print the Inputfrom HTML
    element_1.innerHTML = "Hi, " + name; //change the title to the entry
    element_2.disabled = true;
}                                       //end

