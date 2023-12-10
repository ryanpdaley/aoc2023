const fs = require('fs');
const dataBlock = fs.readFileSync('data.txt', 'utf-8');
const data = dataBlock.split('\n');

const parseRow = (row, index) => {
  let matchCount = 0;
  const cleanData = row.split(':')[1].split('|');
  const winningNumbers = cleanData[0].match(/\d+/g).map(Number);
  const matchingNumbers = cleanData[1].match(/\d+/g).map(Number);
  winningNumbers.forEach((winner) => {
    if (matchingNumbers.includes(winner)) {
      matchCount++;
    }
  });
  const matchMultiplier = cardCount[index];
  for (let i = index + 1; i <= matchCount + index; i++) {
    let current = cardCount[i];
    cardCount[i] = current + matchMultiplier;
  }
};

const rowCount = data.length;
console.log(rowCount);
let cardCount = new Array(rowCount).fill(1);
data.forEach((line, index) => {
  parseInt(parseRow(line, index));
});
var count = cardCount.reduce((accumulator, currentValue) => {
  return accumulator + currentValue;
}, 0);
console.log('-----');
console.log('Total: ', count);
console.log('-----');
