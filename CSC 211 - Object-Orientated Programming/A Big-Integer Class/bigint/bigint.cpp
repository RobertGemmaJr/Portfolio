// Started by Tom on 2/9/18.

#include "bigint.h"
#include <iostream>


/* Secondary Functions */

//Remove any leading zeros from the bigint
void bigint::strip_zeros() {
  while(number.back() == 0 && number.size() > 1) { number.pop_back(); }
}


/* Constructors */

//Default constructor - create a bigint with a value of 0
bigint::bigint() {
  number.clear();
  number.push_back(0);
}

// Create a bigint from a vector
bigint::bigint(const std::vector<vec_bin> &that) {
  number.clear();
  number = that;
  this->strip_zeros();
}

// Create a bigint from a number
bigint::bigint(unsigned long long i) {
  number.clear();
  while (i > 0) {
    // Remove each digit and push it into the bigint one by one
    int lastDigit = i % 10;
    number.push_back(lastDigit);
    i /= 10;
  }
  // While loop never runs if i = 0, give number the correct value
  if(number.empty()) { number.push_back(0); }
}

//Create a bigint from a string
bigint::bigint(std::string str) {
  number.clear();
  for(int i = str.length() - 1; i >=0; i--) {
    int strInt = (int)(str[i] - '0'); //Gets ACII value equal to the character
    number.push_back(strInt);
  }
  this->strip_zeros();
}

//Create a bigint from a text file
bigint::bigint(std::ifstream &infile) {
  number.clear();
  char ch;

  if(!infile.fail()) {
    while(infile.get(ch)) {
      int charInt = (int)(ch - '0');
      //File is read top to bottom so the numbers must be inserted backwards
      number.insert(number.begin(), charInt);
    }
  } else{
    std::cerr << "Unable to open file" << '\n';
    exit(EXIT_FAILURE);
   }
  this->strip_zeros();
}

//Create a bigint from another bigint
bigint::bigint(const bigint &that) {
  number.clear();
  number = that.getNumber();
  this->strip_zeros();
}


/* Number Access */

//Return the vector that stores the bigint
const std::vector<vec_bin> &bigint::getNumber() const {
  return number;
}

//Return the digit of a bigint at a specified index
vec_bin bigint::operator[](size_t index) const {
  return number[index];
}


/* Comparators */

bool bigint::operator==(const bigint &that) const {
  return number == that.number;
}

bool bigint::operator!=(const bigint &that) const {
  return number != that.number;
}

bool bigint::operator<(const bigint &that) const {
  // Preliminary test that they aren't equal
  if(*this == that) { return false; }

  std::vector<vec_bin> thatNum = that.getNumber();
  if (number.size() < thatNum.size()) {
    return true; // This has less digits
  } else if (number.size() == thatNum.size()) {
    // This has same number of digits but...
    for(int i = number.size()-1; i >= 0; i--) {
      if (number[i] < thatNum[i]) {
        return true; // ... This' digit is < than that's digit
      } else if (number[i] > thatNum[i]) {
        return false; // ... This' digit is >= that last digit
      }
    }
  } else {
    return false; // This has more digits
  }
}

bool bigint::operator<=(const bigint &that) const {
  return *this < that || *this == that;
}

bool bigint::operator>(const bigint &that) const {
  return !(*this <= that);
}

bool bigint::operator>=(const bigint &that) const {
  return *this > that || *this == that;
}


/* Addition */

bigint bigint::add(const bigint &that) const {
  // The maximum length of the anwser is 1 digit greater than the length of the
  // largest operand
  int maxSize;
  if (that.getNumber().size() > number.size()) {
    maxSize = that.getNumber().size() + 1; // That is the larger operand
  } else {
    maxSize = number.size() + 1; //This is the larger operand
  }
  std::vector<vec_bin> anwser(maxSize, 0);

  // Add the bigints together one digit at a time
  for(int i = 0; i < maxSize - 1; i++) {
    if(i >= that.getNumber().size()) {
      anwser[i] += number[i]; // Only this has a value at the current digit
    } else if (i >= number.size()) {
      anwser[i] += that[i]; // Only that has a value at the current digit
    } else {
      anwser[i] += number[i] + that[i]; // Both operands have a value at the current digit
    }
    // Carry over a digit if needed
    if (anwser[i] >= 10) {
        anwser[i] %= 10;
        anwser[i+1] += 1;
    }
  }
  return  anwser;
}

bigint bigint::operator+(const bigint &that) const {
  return add(that);
}

bigint &bigint::operator+=(const bigint &that) {
  *this = this->add(that);
  return *this;
}

bigint &bigint::operator++() {
  return *this;
}

bigint bigint::operator++(int) {
  bigint x(1);
  *this = this->add(x);
  return *this;
}


/* Subtraction */

bigint bigint::subtract(const bigint &that) const {
  // Make sure the operation will evaluate to a positive number
  if(*this < that) {
    std::cerr << "Error: bigint would become a negative number" << '\n';
    exit(EXIT_FAILURE);
  }

  //The max value of the anwser is this' original value
  std::vector<vec_bin> anwser = number;
  // Create a temporary value to keep all the digits in the anwser positive
  int value = 0;
  // Prevent the carry from creating a negative # in the next digit
  bool catchCarry = false;

  // Subtract the bigint one digit at a time
  for(int i = 0; i < number.size(); i++) {
    // Reset the temporary value
    if(catchCarry) { value = -1; } else { value = 0; }

    if (i < that.getNumber().size()) {
      value += anwser[i] - that[i];
    } else {
      value += anwser[i]; // that doesn't have a value at the current digit
    }

    // Push the value into the anwser, carrying over a digit if needed
    if(value < 0) {
      anwser[i] = value + 10;
      if (anwser[i+1] == 0) {
        // Carying over a digit would create a negative number
        catchCarry = true;
      } else{
        anwser[i+1] -= 1;
        catchCarry = false;
      }
    } else { anwser[i] = value; }
  }
  return  anwser;
}

bigint bigint::operator-(const bigint &that) const {
  return subtract(that);
}

bigint &bigint::operator-=(const bigint &that) {
  *this = this->subtract(that);
  return *this;
}

bigint &bigint::operator--() {
  return *this;
}

bigint bigint::operator--(int) {
  bigint x(1);
  *this = this->subtract(x);
  return *this;
}


/** Multiplication */

bigint bigint::multiply(const bigint &that) const {
  // The max # of digits in the anwser is equal to the sum of the # of digits
  // in this and that
  std::vector<vec_bin> anwser(number.size() + that.getNumber().size(), 0);

  // Use a nested for loop to execute the grid method of multiplication
  for(int i = 0; i < number.size(); i++) {
    for(int j = 0; j < that.getNumber().size(); j++) {
      int position = i + j;
      anwser[position] += number[i] * that[j];

      // Carry over a digit if needed
      if(anwser[position] >= 10) {
        anwser[position + 1] += anwser[position] / 10;
        anwser[position] %= 10;
      }
    }
  }
  return  anwser;
}

bigint bigint::operator*(const bigint &that) const {
  return multiply(that);
}

bigint &bigint::operator*=(const bigint &that) {
  *this = this->multiply(that);
  return *this;
}


/** Division */

bigint bigint::divide(const bigint &that) const {
  // Prevent a divide by 0 error
  if(that.to_string() == "0") {
    std::cerr << "Error: Divide by 0 error" << '\n';
    exit(EXIT_FAILURE);
  }

  bigint temp(number);
  int anwser = 0;
  // Count how many times you can subtract that from this
  while(temp >= that) {
    anwser += 1;
    temp -= that;
  }
  return anwser;
}

bigint bigint::operator/(const bigint &that) const {
  return divide(that);
}

bigint &bigint::operator/=(const bigint &that) {
  *this = this->divide(that);
  return *this;
}


/** Modulo */

bigint bigint::mod(const bigint &that) const {
  bigint temp(number);   // Create a temporary bigint
  temp /= that; // Calculte floor division
  temp *= that; // Multiply it by the original dividence
  bigint anwser(*this - temp); // Its differnece from this is the anwser
  return anwser;
}

bigint bigint::operator%(const bigint &that) const {
  return mod(that);
}

bigint &bigint::operator%=(const bigint &that) {
  *this = this->mod(that);
  return *this;
}


/** Power */

bigint bigint::pow(unsigned long long n) {
  bigint anwser(number);
  if (n == 0) {
    anwser = 1; // Any number to the 0th power is 1
  } else {
    // Use multiply to calculate the power
    for (int i = 1; i < n; i ++) { anwser *= *this; }
  }
  return anwser;
}

/* Display methods */

std::ostream &operator<<(std::ostream &os, const bigint &bigint1) {
  // Print the bigint to the screen with commas
  return os << bigint1.to_string(true);
}

// Returns the value of a bigint as a string with or without commas
std::string bigint::to_string(bool commas) const {
  std::string str = "";

  for(int i = number.size() - 1; i >= 0; i--) {
    str += '0' + number[i]; //Gets the character equal to the ASCII value
    if(commas && i % 3 == 0 && i != 0) {
      // Adds a comma after every 3 digits
      str += ',';
    }
  }
  return str;
}

// Returns the value of a bigint as a string in scientific notation
std::string bigint::scientific(unsigned int decimal_points) const {
  // Create the one's place and decimal
  std::string str = std::to_string(number[number.size() - 1]) + '.';

  // Create the decimal places
  if (decimal_points < number.size()-1) {
    for(int i = number.size() - 2; i > (number.size()-2) - decimal_points; i--) {
      str += std::to_string(number[i]);
    }
  } else {
    // All digits shown
    for(int i = number.size() - 2; i >= 0; i--) {
      str += std::to_string(number[i]);
    }
  }

  //Create the scientific part of the scientific notation
  str += "E";
  str += std::to_string(number.size() - 1); //The exponent
  return str;
}

// Writes a bigint to a file as a string with no commas
void bigint::to_file(std::ofstream &outfile, unsigned int wrap) {
  if (!outfile.fail()) {
    std::string str = this->to_string();

    while(!str.empty()) {
      outfile << str.substr(0, wrap) << std::endl; //X is a test
      str.erase(0, wrap);
    }
    outfile.close();
  } else {
    std::cerr << "Unable to open file" << '\n';
    exit(EXIT_FAILURE);
  }
}
