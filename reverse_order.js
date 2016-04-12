// Reverser the order of a string only if characters are alphanumeric

var str = "hell#o the..+=re";

function is_alpha_numeric(char){
    // :param char: char within string
    // :returns: boolean value true if alphanumeric
    var char_ascii = char.charCodeAt();

    if (char_ascii >= 48 && char_ascii <= 57){
        return true
    } else if (char_ascii >= 65 && char_ascii <= 90){
        return true
    } else if (char_ascii >= 97 && char_ascii <= 122){
        return true
    }
    return false
}

function swap_chars(str, min, max) {
    // :param str: string in which letters are swapped
    // :param min: min index of string
    // :param max: max index of string
    // :returns: string with swapped letters
    var arr = str.split('')

    var temp = arr[min]
    arr[min] = arr[max]
    arr[max] = temp

    return arr.join('')
}

function reverse_string(str){
    // :param str: str
    // :returns: reversed string
    var min = 0
    var max = str.length - 1

    // for (var i=0;i<(str.length-1)/2; i++){
    while (min < max){
        if (is_alpha_numeric(str[min]) === true && is_alpha_numeric(str[max]) === true){
            str = swap_chars(str, min, max)
            min++
            max--
        } else if (is_alpha_numeric(str[min]) === true && is_alpha_numeric(str[max]) === false){
            max--
        } else if (is_alpha_numeric(str[min]) === false && is_alpha_numeric(str[max]) === true){
            min++
        } else {
            min++
            max--
        }
    }
    return str
}
console.log(reverse_string(str))
