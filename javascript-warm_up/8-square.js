#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let gisa = '';
    for (let z = 0; z < size; z++) {
      gisa += 'X';
    }
    console.log(gisa);
  }
}
