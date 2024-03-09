def get_grade(s1, s2, s3):
    # Code here
    result = (s1 + s2 + s3) / 3
    
    if (result >= 90 and result <= 100):
        return 'A'
    elif (result >= 80 and result < 90):
        return 'B'
    elif (result >= 70 and result < 80):
        return 'C'
    elif (result >= 60 and result < 70):
        return 'D'
    else:
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