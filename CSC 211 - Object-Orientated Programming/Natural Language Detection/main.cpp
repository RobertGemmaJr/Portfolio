#include "functions.h"
#include "bigint/bigint.h"
#include <iostream>
#include <vector>


/*
The main function takes at least 2 command line arguments, which are text files.
The last argument contains the testing language, and all of the other arguments
are training languages. The function performs a trigram frequency analysis on
each text file and then determines which training language is most similar to
the testing language. This language is printed to the screen.
*/
int main(int argc, char *argv[]) {
  // Need at least 3 arguments (2 training languages and 1 testing language)
  if (argc <= 3) {
    std::cerr << "Too few arguments." << std::endl;
    exit(EXIT_FAILURE);
  }

  std::vector< std::vector<long long> > allFreq;
  std::vector<std::string> files;


  // Complete the trigram frequency analysis for all of the text files.
  for(int i = 0; i < argc - 1; i++) {
    std::ifstream infile(argv[i+1]);

    if (!infile.fail()) {
      /*
      Create a vector from the calulated trigrams. Frequencies function
      calculates the trigram frequencies of the text file.
      */
      std::vector<long long> langFreq = frequencies(infile);
      allFreq.push_back(langFreq);
      files.push_back(argv[i+1]);

    } else {
    std::cerr << "No file by that name. Please choose a valid file." << std::endl;
    exit(EXIT_FAILURE);
    }
  }

  /*
  Calculate the cosine simularity between the testing language and each
  training language. Determine which two are most similar and print the name
  of that training language. Language returns an int, which is the correct
  index for the training language that is most similar to the testing language.
  */
  std::cout << files[language(allFreq)] << std::endl;
}
