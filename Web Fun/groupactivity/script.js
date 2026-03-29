// Reverse String
function reverseString(str) {
    let output = "";
    for (let i = str.length - 1; i >= 0; i--) {
        output += str[i];
    }
    return output;
}
console.log(reverseString("Bra")); // arB


//Count Vowels 
function countVowels(str) {
    let vowels = "aeiouAEIOU";
    let count = 0;

    for (let char of str) {
        if (vowels.includes(char)) {
            count++;
        }
    }
    return count;
}
console.log(countVowels("braa")); // 2


// Count Vowels 
function countVowels2(str) {
    let vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"];
    let count = 0;

    for (let i = 0; i < str.length; i++) { 
        if (vowels.includes(str[i])) {
            count++;
        }
    }
    return count;
}
console.log(countVowels2("shaima")); // 4


// Palindrome Check
function isPalindrome(str) {
    let reversedStr = "";

    for (let i = str.length - 1; i >= 0; i--) {
        reversedStr += str[i];
    }

    return str === reversedStr;
}
console.log(isPalindrome("dad")); 


// Find Longest Word
function findLongestWord(statement = "I am not a Barcelona fan") {
    let words = statement.split(" ");
    let longest = words[0];

    for (let i = 1; i < words.length; i++) {
        if (words[i].length > longest.length) {
            longest = words[i];
        }
    }

    console.log("The longest word is: " + longest);
}
findLongestWord();


// Find Cases (vowels, digits, spaces, others)
function findCases(str) {
    let output = {
        countVowels: 0,
        digits: 0,
        spaces: 0,
        others: 0
    };

    let vowels = "aeiouAEIOU";

    for (let char of str) {
        if (vowels.includes(char)) {
            output.countVowels++;
        } else if (char === " ") {
            output.spaces++;
        } else if (char >= '0' && char <= '9') {
            output.digits++;
        } else {
            output.others++;
        }
    }

    return output;
}
console.log(findCases("shaimaa 1234"));


// Feedback (FIXED switch)
function feedback(str) {
    let msg = "";

    switch (str) {
        case "A":
        case "a":
            msg = "Excellent";
            break;

        case "B":
        case "b":
            msg = "Good";
            break;

        case "C":
        case "c":
            msg = "You passed";
            break;

        case "D":
        case "d":
            msg = "Need improvement";
            break;

        case "F":
        case "f":
            msg = "Failed";
            break;

        default:
            msg = "Invalid grade";
    }

    console.log(msg);
}
feedback("d");