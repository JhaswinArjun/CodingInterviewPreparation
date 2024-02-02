// Problem 1: Find last digit in a number.
console.log('Problem 1: Find last digit in a number.');

// Method 1: Using string.
function lastDigitUsingString(a,b){
    result = parseInt(a) ** parseInt(b)
    return result.toString().charAt(result.toString().length - 1);
}

console.log(lastDigitUsingString('3','10'));
console.log(lastDigitUsingString('6','2'));

// Method 2: Using modulus.
// Note: Math.pow(parseInt(a),parseInt(b))
// Note: lastCharacter = result.toString().charAt(result.toString().length - 1)
function lastDigitUsingModulus(a,b){
    return (parseInt(a) ** parseInt(b)) % 10;
}

console.log(lastDigitUsingModulus('3','10'));
console.log(lastDigitUsingModulus('6','2'));

// Problem 2: Find first and last digits of a number.
console.log('Problem 2: Find first and last digits of a number.');

// Method 1: Number with loop.
console.log('Method 1: Number with loop.');
const getLastDigit = number => number % 10;
const getFirstDigit = number => {
    while (number >= 10){
        number /= 10;
    }
    return Math.floor(number)
}
function firstLastNumberWithLoop(number){
    return `Last Digit: ${getLastDigit(number)} , First Digit: ${getFirstDigit(number)}.`
}


