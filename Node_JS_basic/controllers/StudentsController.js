const { readDatabase } = require('../utils');

class StudentsController {
  static async getAllStudents(req, res) {
    const databasePath = process.argv[2];
    try {
      const fields = await readDatabase(databasePath);
      let responseText = 'This is the list of our students\n';

      for (const [field, students] of Object.entries(fields).sort()) {
        responseText += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
      }

      res.status(200).send(responseText.trim());
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const databasePath = process.argv[2];
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    try {
      const fields = await readDatabase(databasePath);
      const students = fields[major] || [];
      res.status(200).send(`List: ${students.join(', ')}`);
    } catch (err) {
      res.status(500).send('Cannot load the database');
    }
  }
}

module.exports = StudentsController;