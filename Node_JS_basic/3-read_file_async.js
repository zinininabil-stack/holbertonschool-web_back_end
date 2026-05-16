const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);
      const fields = {};

      students.forEach((line) => {
        const [firstname, , , field] = line.split(',');
        if (field) {
          if (!fields[field]) fields[field] = [];
          fields[field].push(firstname);
        }
      });

      console.log(`Number of students: ${students.length}`);
      Object.entries(fields).forEach(([field, list]) => {
        console.log(
          `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`,
        );
      });

      resolve();
    });
  });
}

module.exports = countStudents;