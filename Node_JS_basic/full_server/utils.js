import fs from 'fs';

export default function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
      } else {
        const database = data
          .split('\n')
          .filter((line) => line.trim() !== '')
          .slice(1);
        const groups = {};
        database.forEach((line) => {
          const parts = line.split(',');
          const firstname = parts[0];
          const field = parts[3];
          if (groups[field]) {
            groups[field].push(firstname);
          } else {
            groups[field] = [firstname];
          }
        });
        resolve(groups);
      }
    });
  });
}
