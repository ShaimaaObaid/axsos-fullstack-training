// Always Hungry
function alwaysHungry(arr) {
    var found = false; 

    for (var i = 0; i < arr.length; i++) {
        if (arr[i] === "food") { 
            console.log("yummy");
            found = true; 
        }
    }

    if (!found) { 
        console.log("I'm hungry");
    }
}

alwaysHungry([3.14, "food", "pie", true, "food"]);
alwaysHungry([4, 1, 5, 7, 2]); 

// High Pass Filter
function highPass(arr, cutoff) {
    var filteredArr = [];

    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > cutoff) {
            filteredArr.push(arr[i]); 
        }
    }

    return filteredArr;
}

var resultHighPass = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(resultHighPass); 

//Better Than Average
function betterThanAverage(arr) {
    var sum = 0;

    for (var i = 0; i < arr.length; i++) {
        sum += arr[i]; 
    }

    var avg = sum / arr.length;
    var count = 0;

    for (var i = 0; i < arr.length; i++) {
        if (arr[i] > avg) {
            count++;
        }
    }

    return count;
}

var resultBetter = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(resultBetter); 

// Array Reverse
function reverse(arr) {
    var left = 0;
    var right = arr.length - 1;

    while (left < right) {
        var temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;

        left++;
        right--;
    }

    return arr;
}

var resultReverse = reverse(["a", "b", "c", "d", "e"]);
console.log(resultReverse); 

//Fibonacci Array
function fibonacciArray(n) {
    var fibArr = [0, 1];

    for (var i = 2; i < n; i++) {
        var next = fibArr[i - 1] + fibArr[i - 2]; 
        fibArr.push(next);
    }

    return fibArr;
}

var resultFibonacci = fibonacciArray(10);
console.log(resultFibonacci); 