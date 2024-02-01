// Find odd or even.

console.log('Method 1: Using Modulus');
// Method 1: Using Modulus
function isEvenModulus(number){
    return (number % 2) == 0;
}

console.log(isEvenModulus(6));
console.log(isEvenModulus(9));

// Use arrow function
const isEvenModulusArrow = (number) => number % 2 == 0;

console.log(isEvenModulusArrow(6));
console.log(isEvenModulusArrow(9)); 

console.log('Method 2: Using Binary');
function isEvenBinary(number){
    return (number & 1) == 0;
}
console.log(isEvenBinary(6));
console.log(isEvenBinary(9)); 
// Arrow function.
const isEvenBinaryArrow = (number) => (number & 1) == 0;
console.log(isEvenBinaryArrow(6));
console.log(isEvenBinaryArrow(9)); 

console.log('Method 3: Using Bitwise shift.');
function isEvenBitwiseShift(number){
    return number == (number >> 1) << 1;
}
console.log(isEvenBitwiseShift(6));
console.log(isEvenBitwiseShift(9)); 
// Arrow function.
const isEvenBitwiseShiftArrow = (number) => number == (number >> 1) << 1;
console.log(isEvenBitwiseShiftArrow(6));
console.log(isEvenBitwiseShiftArrow(9)); 