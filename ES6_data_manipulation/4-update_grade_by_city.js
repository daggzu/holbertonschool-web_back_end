/* eslint-disable */
export default function updateStudentGradeByCity(students, city, newGrades) {
    if (!Array.isArray(students)) {
      return [];
    }
  
  
    const sortFilter = students.filter((student) => student.location === city);
  
    const mapping = sortFilter.map((student) => {
        const newGrade = newGrades.filter((grade) => grade.studentId === student.id);
        const updated_grade = { ...student };
          if (newGrade[0]) {
              updated_grade.grade = newGrade[0].grade;
          } else {
              updated_grade.grade = 'N/A';
          }
          return updated_grade;
      });
  
      return mapping;
  }
