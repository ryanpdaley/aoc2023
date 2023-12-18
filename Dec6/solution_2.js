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
    // console.log(
    //   `${distanceTraveled} > ${distanceRecord} = ${
    //     distanceTraveled > distanceRecord
    //   }`
    // );
    if (distanceTraveled > distanceRecord) {
      winCount++;
    }
  }
  return winCount;
};

const countWaysToWin = (parsedData) => {
  return findWaysToWin(parsedData);
};

const parseData = (data) => {
  const rowData = data.split(/\r?\n/);
  const time = Number(rowData[0].split(':')[1].replace(/\s+/g, ''));
  const distance = Number(rowData[1].split(':')[1].replace(/\s+/g, ''));
  return [time, distance];
};

const parsedData = parseData(data);
console.log('-----');
console.log('Total: ', countWaysToWin(parsedData));
console.log('-----');
