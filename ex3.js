/*
Desenvolva uma função que calcula o fatorial de um número.
*/

function fat(num) {
    if (num === 0 || num === 1) {
        return 1;
    } else {
        return num * fat(num - 1);
    }
}

 