/*Desenvolva uma função que recebe uma lista de palavras e um caractere como parâmetro e retorna apenas as 
palavras que começam com esse caractere.
*/
function palavrasQueComecamCom(listaPalavras, caractere) {
    return listaPalavras.filter(function(palavra) {
        return palavra.charAt(0).toLowerCase() === caractere.toLowerCase();
    });
}

