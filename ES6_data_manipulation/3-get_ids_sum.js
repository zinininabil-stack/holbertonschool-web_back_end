export default function getStudentIdsSum(listStudent) {
  return listStudent.reduce((acc, current) => acc + current.id, 0);
}