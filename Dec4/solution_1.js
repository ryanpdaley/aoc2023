const fs = require('fs');
const data = fs.readFileSync('data.txt', 'utf-8');

const parseRow = (row) => {
  let matchCount = 0;
  const cleanData = row.split(':')[1].split('|');
  const winningNumbers = cleanData[0].match(/\d+/g).map(Number);
  const matchingNumbers = cleanData[1].match(/\d+/g).map(Number);
  winningNumbers.forEach((winner) => {
    if (matchingNumbers.includes(winner)) {
      if (matchCount === 0) {
        matchCount = 1;
      } else {
        matchCount = matchCount * 2;
      }
    }
  });
  return matchCount;
};

let count = 0;
data.split(/\r?\n/).forEach((line) => {
  count += parseInt(parseRow(line));
});
console.log('-----');
console.log('Total: ', count);
console.log('-----');
