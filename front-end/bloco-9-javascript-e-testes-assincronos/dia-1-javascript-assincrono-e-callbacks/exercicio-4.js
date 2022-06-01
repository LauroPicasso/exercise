const messageDelay = () => Math.floor(Math.random() * 5000);

const getMarsTemperature = () => {
  const maxTemperature = 58;
  return Math.floor(Math.random() * maxTemperature);
};

// crie a função sendMarsTemperature abaixo
function sendMarsTemperature() {
  const a = getMarsTemperature()
  setTimeout(() => {
    console.log(`Mars temperature is: ${a} degree Celsius`);
  }, messageDelay); 
}

sendMarsTemperature(); // imprime "Mars temperature is: 20 degree Celsius", por exemplo