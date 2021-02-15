/**
 * Started by Najib 3/21/18
 **/

#ifndef __FUNCTIONS_H__
#define __FUNCTIONS_H__

#include <vector>
#include <string>
#include <iostream>
#include <math.h>
#include "bigint/bigint.h"

/*
Return a series of 17576 numbers reprisenting the trigram frequenices of
a given text file. This function take one argument in the form of a
ifstream text file. The function only counts letters and disregards special
characters and spaces.
*/
std::vector<long long> frequencies(std::ifstream &infile);

/*
Return the name of the training language that is most similar to the inputed
testing language. The function takes in multiple ifstream text files. The last
command line argument is the testing language and all other text files are the
training languages to "choose" from.
*/
int language(std::vector< std::vector<long long> > &allFreq);


#endif
