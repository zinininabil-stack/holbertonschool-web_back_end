import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    response.status(200);
    readDatabase(process.argv[2])
      .then((groups) => {
        let result = 'This is the list of our students';
        Object.keys(groups)
          .sort()
          .forEach((field) => {
            const students = groups[field].join(', ');
            result += `\nNumber of students in ${field}: ${groups[field].length}. List: ${students}`;
          });
        response.send(result);
      })
      .catch(() => {
        response.status(500);
        response.send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    response.status(200);
    readDatabase(process.argv[2])
      .then((groups) => {
        const { major } = request.params;
        if (major !== 'CS' && major !== 'SWE') {
          response.status(500);
          response.send('Major parameter must be CS or SWE');
        } else {
          response.send(`List: ${groups[major].join(', ')}`);
        }
      })
      .catch(() => {
        response.status(500);
        response.send('Cannot load the database');
      });
  }
}
export default StudentsController;
