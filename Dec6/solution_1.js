const fs = require('fs');
const data = fs.readFileSync('data.txt', 'utf-8');
// const data = fs.readFileSync('sampleData.txt', 'utf-8');

const findWaysToWin = (dataPair) => {
  // Brut force
  let winCount = 0;
  const time = dataPair[0];
  const distanceRecord = dataPair[1];
  for (let i = 0; i < time; i++) {
    const distanceTraveled = (time - i) * i;
    if (distanceTraveled > distanceRecord) {
      winCount++;
    }
  }
  return winCount;
};

const countWaysToWin = (parsedData) => {
  let waysToWin = 1;
  parsedData.forEach((dataPair) => {
    waysToWin *= findWaysToWin(dataPair);
  });
  return waysToWin;
};

const parseData = (data) => {
  let parsedData = [];
  const rowData = data.split(/\r?\n/);
  const time = rowData[0].split(':')[1].match(/\d+/g).map(Number);
  const distance = rowData[1].split(':')[1].match(/\d+/g).map(Number);
  for (let i = 0; i < time.length; i++) {
    parsedData.push([time[i], distance[i]]);
  }
  return parsedData;
};

const parsedData = parseData(data);
console.log('-----');
console.log('Total: ', countWaysToWin(parsedData));
console.log('-----');
