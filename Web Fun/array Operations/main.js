//Q1
let colors = ["red", "blue", "green", "yellow", "purple"];

console.log(colors[0]);

console.log(colors[colors.length - 1]);

console.log(colors[1]);

colors[2] = "orange";

console.log(colors);
//Q2
let numbers = [10, 20, 30, 40, 50];

for(let i = 0; i < numbers.length; i++){
    console.log(numbers[i]);
}
for(let i = numbers.length - 1; i >= 0; i--){
    console.log(numbers[i]);
}
//Q3
let numbers2 = [5, 10, 15, 20, 25];

let index = numbers2.indexOf(25);

if(index !== -1){
    console.log("Found at position " + index);
}else{
    console.log("Not Found");
}
//Q4
//A
let scores = [50, 20, 70, 10, 40];

scores.sort((a,b) => a - b);

console.log(scores);

scores.sort((a,b) => b - a);

console.log(scores);
//b
let names = ["Shatha", "Sara", "Lina", "Sami", "Dalia"];

names.sort();

console.log(names);
//Q5
let animals = ["dog", "cat", "rabbit"];

animals.push("elephant");

animals.unshift("lion");

animals.splice(2,0,"tiger");

console.log(animals);
//Q6
let fruits = ["apple", "banana", "cherry", "date"];

fruits.shift();

fruits.pop();
fruits = fruits.filter(fruit => fruit !== "banana");

console.log(fruits);
//Q7
let array1 = [1,2,3];
let array2 = [4,5,6];

let combined = array1.concat(array2);

console.log(combined);
//Q8
let items = ["a","b","c","d","e"];

let firstPart = items.slice(0,3);
let secondPart = items.slice(3);

console.log(firstPart);
console.log(secondPart);
//Q9
let numbers3 = [1,5,10,15,20,25,30];

let filtered = numbers3.filter(num => num > 15);

console.log(filtered);
//Q10
//A
let arrDuplicates = [1,2,2,3,4,4,5];

let unique = [...new Set(arrDuplicates)];

console.log(unique);
//B
let arr = [1,2,3,4,5];
let n = 2;

for(let i = 0; i < n; i++){
    let last = arr.pop();
    arr.unshift(last);
}

console.log(arr);
//bouns
let arr1 = [1, 3, 5];
let arr2 = [2, 4, 6];
let merged = [];

let i = 0; 
let j = 0; 
while(i < arr1.length && j < arr2.length){
    if(arr1[i] < arr2[j]){
        merged.push(arr1[i]);
        i++; 
    } else {
        merged.push(arr2[j]); 
        j++; 
    }
}
while(i < arr1.length){
    merged.push(arr1[i]);
    i++;
}

while(j < arr2.length){
    merged.push(arr2[j]);
    j++;
}

console.log(merged);