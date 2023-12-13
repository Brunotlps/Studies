/* Desenvolva uma função que verifica se duas strings são anagramas uma da outra (ou seja, se possuem as 
mesmas letras, mas em ordem diferente).
*/ 
function saoAnagramas(str1, str2) {

    const s1 = str1.replace(/\s/g, '').toLowerCase();
    const s2 = str2.replace(/\s/g, '').toLowerCase();

    if (s1.length !== s2.length) {
        return false;
    }
    const sortedStr1 = s1.split('').sort().join('');
    const sortedStr2 = s2.split('').sort().join('');   
    return sortedStr1 === sortedStr2;

}

