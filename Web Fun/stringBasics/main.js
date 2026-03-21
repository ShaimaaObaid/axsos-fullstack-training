//Q1
function removeBlanks(str) {
    var result = "";
    for (var i = 0; i < str.length; i++) {
        if (str[i] !== " ") { 
            result += str[i];
        }
    }
    return result;
}
console.log(removeBlanks(" Pl ayTha tF u nkyM usi c ")); 
console.log(removeBlanks("I can not BELIEVE it's not BUTTER")); 
//Q2
function getDigits(str) {
    var result = "";
    for (var i = 0; i < str.length; i++) {
        if (!isNaN(str[i]) && str[i] !== " ") { 
            result += str[i];
        }
    }
    return Number(result); 
}


console.log(getDigits("abc8c0d1ngd0j0!8")); 
console.log(getDigits("0s1a3y5w7h9a2t4?6!8?0")); 

//Q3
function acronym(str) {
    var words = str.split(" "); 
    var result = "";
    for (var i = 0; i < words.length; i++) {
        if (words[i] !== "") { 
            result += words[i][0].toUpperCase(); 
        }
    }
    return result;
}

console.log(acronym(" there's no free lunch - gotta pay yer way. ")); 
console.log(acronym("Live from New York, it's Saturday Night!"));
//Q4
function countNonSpaces(str) {
    var count = 0;
    for (var i = 0; i < str.length; i++) {
        if (str[i] !== " ") { 
            count++;
        }
    }
    return count;
}

console.log(countNonSpaces("Honey pie, you are driving me crazy")); 
console.log(countNonSpaces("Hello world !"));
//Q5
function removeShorterStrings(arr, minLength) {
    var result = [];
    for (var i = 0; i < arr.length; i++) {
        if (arr[i].length >= minLength) {
            result.push(arr[i]);
        }
    }
    return result;
}

console.log(removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4)); 
console.log(removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3)); 
