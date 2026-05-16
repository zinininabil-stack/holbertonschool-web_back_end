const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    if (!path) {
      reject(new Error('Cannot load the database'));
      return;
    }
    fs.readFile(path, 'utf8', (error, data) => {
      if (error) {
        reject(new Error('Cannot load the database'));
      } else {
        const database = data.split('\n').filter((line) => line.trim() !== '').slice(1);
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
        console.log(`Number of students: ${database.length}`);
        let result = `Number of students: ${database.length}`;
        for (const field in groups) {
          if (Object.prototype.hasOwnProperty.call(groups, field)) {
            console.log(`Number of students in ${field}: ${groups[field].length}. List: ${groups[field].join(', ')}`);
            result += `\nNumber of students in ${field}: ${groups[field].length}. List: ${groups[field].join(', ')}`;
          }
        }
        resolve(result);
      }
    });
  });
}
module.exports = countStudents;