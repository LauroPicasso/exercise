/* 1 - Crie uma função que receba uma string e retorne true se for um palíndromo , ou false , se não for.
Exemplo de palíndromo: arara .
verificaPalindrome('arara') ;
Retorno esperado: true
verificaPalindrome('desenvolvimento') ;
Retorno esperado: false */

//Duas formas de resolver o exercício
/*
  Como podemos acessar a posição de uma string da mesma forma que
  acessamos um array, podemos então, comparar o caracter da
  posição 0 (primeira) com o caracter da última posição (length - 1).
  Dessa forma conseguimos verificar se a sequência de caracteres
  na string é a mesma do inicio ao fim e do fim ao inicio 😉
*/
function verificaPalindrome(word){
  for(let index in word){
    if(word[index] === word[(word.length - 1) - index]){
      return true;
    }
  }
  return false;
}

console.log(verificaPalindrome('arara')); //true
console.log(verificaPalindrome('desenvolvimento')); //false