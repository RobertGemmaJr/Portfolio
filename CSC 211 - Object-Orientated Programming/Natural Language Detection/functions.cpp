#include <vector>
#include <string>
#include <iostream>
#include "functions.h"
#include "bigint/bigint.h"


std::vector<long long> statistics(std::string &text);
double similarity (std::vector<long long> &testing, std::vector<long long> &training);

/*
Takes one argument in the form of an ifstream text file. It will
return a vector of long long numbers representing the trigram frequencies
of the text.
*/
std::vector<long long> frequencies(std::ifstream &infile) {

    std::string text;
    char ch;

    /*
    Creates a string with only lower case letters, stripping spaces
    and special characters. Converts capital letters into lower case
    letters.
    */
    while (infile.get(ch)) {
      if (ch >= 'a' && ch <= 'z') text+=(ch);
      if (ch >= 'A' && ch <= 'Z') text+=(ch + 32);
    }

    // Sends the string as an argument
    return statistics(text);

}

/*
Actually calulates the trigram frequnecies and return a vector filled
with them. Takes a string as and argument.
*/
std::vector<long long> statistics(std::string &text) {
  // Initialized at size 17576 because 26^3==17576
  std::vector<long long> freqVec(17576, 0);
  // Makes the left most letter most significant in the base 26 number
  for (long long i = 0; i <= (long long)(text.length()-3); i++) {
    int a = ((int)(text[i] - 'a') * 676);
    int b = ((int)(text[i+1] - 'a') * 26);
    int c = (int)(text[i+2] - 'a');

    int total = (a+b+c);
    // Adds one to the vector index equal to the base 26 trigam value
    freqVec[total] += 1;
  }

  return freqVec;
}

/*
Calculate the cosine similarity between the testing language and all of the
training languages. It takes in a vector of all of the calculated trigrams
frequency analysis vectors - one per file. It returns the index at which
the most similar training language is.
*/
int language(std::vector< std::vector<long long> > &allFreq) {
  // Don't compute the similarity between the testing language and itself
  std::vector<double> allSimilarities(allFreq.size()-1, 0);

  double max = allSimilarities[0];
  int maxIndex = 0;
  for(int i = 0; i < (int)allFreq.size()-1; i++) {
    allSimilarities[i] = similarity(allFreq[allFreq.size()-1], allFreq[i]);

    // Find the maximum value in allSimilarities and its index number
    if(allSimilarities[i] > max) {
      max = allSimilarities[i];
      maxIndex = i;
    }
  }

  return maxIndex;
}


/*
Actually calculate the cosine similarities between 2 vectors recieved as an
input. This fuction returns the similarity as a double.
*/
double similarity (std::vector<long long> &testing, std::vector<long long> &training) {
  // Calculate the numerator, which is the dot-product of the vectors
  bigint numerator;
  for(int i = 0; i < (int)testing.size(); i++) {
    numerator += testing[i] * training[i];
  }
  numerator *= numerator;

  // Calculate the denominator which is the product of the norms of each vector
  bigint testNorm;
  bigint trainNorm;
  for (int i = 0; i < (int)testing.size(); i++) {
    testNorm += testing[i] * testing[i];
    trainNorm += training[i] * training[i];
  }
  bigint denominator = (testNorm * trainNorm);

  // Use scaled division to calculate the cosine simularity
  numerator *= 1000000;
  bigint scaledAnswer = (numerator / denominator);
  std::string temp = scaledAnswer.to_string();
  std::string::size_type sz;
  double answer = ((std::stod(temp, &sz)) / 1000000);

  // Test Prints
  //std::cout << "numerator   " << numerator.to_string() << std::endl;
  //std::cout << "denominator " << denominator.to_string() << std::endl;
  //std::cout << "scaled answer: " << scaledAnswer.to_string() << std::endl;
  //std::cout << "answer:        " << answer << std::endl;

  return answer;
}



//
