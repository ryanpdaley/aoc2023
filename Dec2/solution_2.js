const GAME_REGEX = /Game\s\d{1,3}:\s/gi;
const BLUE_REGEX = /\s*\d+\s+blue/gi;
const RED_REGEX = /\s*\d+\s+red/gi;
const GREEN_REGEX = /\s*\d+\s+green/gi;

const parseColour = (colour, trial) => {
  let regex = '';
  switch (colour) {
    case 'blue':
      regex = BLUE_REGEX;
      break;
    case 'green':
      regex = GREEN_REGEX;
      break;
    case 'red':
      regex = RED_REGEX;
      break;
  }

  const found = trial.match(regex);
  if (found) {
    return parseInt(found);
  }
};

const calculatePower = (row) => {
  const greenCounts = [];
  const blueCounts = [];
  const redCounts = [];
  const gameChunk = row.match(GAME_REGEX)[0];
  const gameId = gameChunk.replace(/\D/g, '');
  const results = row.replace(gameChunk, '');
  const trials = results.split(';');
  for (i in trials) {
    const blue = parseInt(parseColour('blue', trials[i]));
    const red = parseInt(parseColour('red', trials[i]));
    const green = parseInt(parseColour('green', trials[i]));

    if (blue) {
      blueCounts.push(blue);
    }
    if (red) {
      redCounts.push(red);
    }
    if (green) {
      greenCounts.push(green);
    }
  }
  return (
    Math.max(...blueCounts) * Math.max(...redCounts) * Math.max(...greenCounts)
  );
};

const fs = require('fs');
const data = fs.readFileSync('data.txt', 'utf-8');

let count = 0;
data.split(/\r?\n/).forEach((line) => {
  count += parseInt(calculatePower(line));
});
console.log('-----');
console.log('Total: ', count);
console.log('-----');
