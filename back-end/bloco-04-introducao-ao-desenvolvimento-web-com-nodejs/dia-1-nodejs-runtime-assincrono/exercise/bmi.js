const readline = require('readline-sync');

const weight = readline.questionFloat("Peso? ");
const height = readline.questionInt("Altura? ");

const imcCalc = (w, h) => w / (h / 100) ** 2;

const imc = imcCalc(weight, height);

console.log(imc);
