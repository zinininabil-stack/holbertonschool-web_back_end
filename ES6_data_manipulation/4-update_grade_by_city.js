export default function updateStudentGradeByCity(
  listStudents,
  city,
  newGrades,
) {
  const listStudentsByCity = listStudents.filter(
    (student) => student.location === city,
  );
  return listStudentsByCity.map((student) => {
    const gradeObj = newGrades.find((grade) => grade.studentId === student.id);
    const grade = gradeObj ? gradeObj.grade : 'N/A';
    return { ...student, grade };
  });
}