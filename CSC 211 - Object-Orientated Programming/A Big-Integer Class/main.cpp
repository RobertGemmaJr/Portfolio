
#include "catch/catch.hpp"
#include "bigint/bigint.h"
#include <sstream>
#include <fstream>
#include <iostream>

using std::string;

typedef std::vector<vec_bin> vec;

TEST_CASE("Constructors", "[constructors]") {
    SECTION("Default") {
        bigint x;
        REQUIRE(x.getNumber() == vec{0});
    }
    SECTION("Vector") {
        bigint x(vec{6, 7, 5});
        REQUIRE(x.getNumber() == vec{6, 7, 5});
    }
    SECTION("String") {
        bigint x("025");
        REQUIRE(x.getNumber() == vec{5, 2});
    }
    SECTION("Integer") {
        bigint x(250);
        REQUIRE(x.getNumber() == vec{0, 5, 2});
    }
    SECTION("File") {
        std::ifstream infile("test.txt");
        bigint x(infile);
        infile.close();
        REQUIRE(x.getNumber() == vec{5, 2});
    }
    SECTION("bigint") {
        bigint x(100);
        bigint y(x);
        REQUIRE(y.getNumber() == vec{0, 0, 1});
    }
}

TEST_CASE("Displaying Bigints", "[display]") {
    bigint x(1234);
    SECTION("to_string()") {
        REQUIRE(x.to_string() == std::string("1234"));
        REQUIRE(x.to_string(true) == std::string("1,234"));
    }
    SECTION("scientific()") {
      bigint x2("1234567891011121314151617181920");
      REQUIRE(x2.scientific() == std::string("1.234E30"));
      REQUIRE(x2.scientific(1) == std::string("1.2E30"));
    }
    SECTION("to_file()") {
      bigint y("123456789012345678901234567890");
      std::ofstream outfile("writeTest.txt");
      y.to_file(outfile, 4);
      outfile.close();
    }
}

TEST_CASE("Comparators", "[compare]") {
  bigint x(100);
  bigint y(100);
  bigint z(200);
  REQUIRE(x == y);
  REQUIRE(x != z);
  REQUIRE(x[0] == 0);
  REQUIRE(y[2] == 1);
  REQUIRE(x < z);
  REQUIRE(x <= y);
  REQUIRE(z > y);
  REQUIRE(x >= y);
}

TEST_CASE("Arithmetic", "[math]") {
    SECTION(".add()") {
        bigint x(56);
        bigint y(115);
        bigint z(x.add(y));
        REQUIRE(z.getNumber() == vec{1, 7, 1});
    }
    SECTION(".subtract()") {
        bigint x(25);
        bigint y(5);
        bigint z(x.subtract(y));
        //y.subtract(x); //Evaluates to an error
        REQUIRE(z.getNumber() == vec{0, 2});
    }
    SECTION(".multiply()") {
        bigint x(187);
        bigint y(161);
        bigint z(x.multiply(y));
        REQUIRE(z.getNumber() == vec{7, 0, 1, 0, 3});
    }
    SECTION(".divide()") {
        bigint x(100);
        bigint y(15);
        bigint z(x.divide(y));
        REQUIRE(z.getNumber() == vec{6});
    }
    SECTION(".mod") {
        bigint x(187);
        bigint z(x.mod(15));
        REQUIRE(z.getNumber() == vec{7});
    }
    SECTION(".pow()") {
        bigint x(2);
        bigint z(x.pow(3));
        REQUIRE(z.getNumber() == vec{8});
    }
}

TEST_CASE("Operators", "[operators]") {
    bigint x(10);
    bigint y(15);
    SECTION("+") {
      bigint z(x+y);
      REQUIRE(z.getNumber() == vec{5, 2});
    }
    SECTION("+=") {
      bigint z(5);
      z += x;
      REQUIRE(z.getNumber() == vec{5, 1});
    }
    SECTION("++") {
      bigint z(24);
      z++;
      REQUIRE(z.getNumber() == vec{5, 2});
    }
    SECTION("++ int") {
      bigint z(26);
      ++z;
      REQUIRE(z.getNumber() == vec{6, 2});
    }
    SECTION("-") {
      bigint z(y-x);
      REQUIRE(z.getNumber() == vec{5});
    }
    SECTION("-=") {
      bigint z(35);
      z -= x;
      REQUIRE(z.getNumber() == vec{5, 2});
    }
    SECTION("--") {
      bigint z(27);
      z--;
      REQUIRE(z.getNumber() == vec{6, 2});
    }
    SECTION("-- int") {
      bigint z(26);
      z--;
      REQUIRE(z.getNumber() == vec{5, 2});
    }
    SECTION("*") {
      bigint z(x*y);
      REQUIRE(z.getNumber() == vec{0, 5, 1});
    }
    SECTION("*=") {
      bigint z(43);
      z *= x;
      REQUIRE(z.getNumber() == vec{0, 3, 4});
    }
    SECTION("/") {
      bigint z(y/x);
      REQUIRE(z.getNumber() == vec{1});
    }
    SECTION("/=") {
      bigint z(100);
      z /= y;
      REQUIRE(z.getNumber() == vec{6});
    }
    SECTION("%") {
      bigint z(y % x);
      REQUIRE(z.getNumber() == vec{5});
    }
    SECTION("%=") {
      bigint z(100000);
      z %= x;
      REQUIRE(z.getNumber() == vec{0});
    }
}

TEST_CASE("OS Stream ") {
    bigint x(12345);
    SECTION("<<") {
      std::cout << x << std::endl;
    }
}
