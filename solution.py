def get_grade(s1, s2, s3):
    m = (s1 + s2 + s3) / 3.0
    if 90 <= m <= 100:
        return 'A'
    elif 80 <= m < 90:
        return 'B'
    elif 70 <= m < 80:
        return 'C'
    elif 60 <= m < 70:
        return 'D'
    return "F"


"""
JS SOLUTION

function getGrade(s1, s2, s3) {
  // Code here
  let result = (s1 + s2 + s3) / 3;

  if (result >= 90 && result <= 100) {
    return 'A';
  } else if (result >= 80 && result < 90) {
    return 'B';
  } else if (result >= 70 && result < 80) {
    return 'C';
  } else if (result >= 60 && result < 70) {
    return 'D';
  } else {
    return 'F';
  }
}

"""