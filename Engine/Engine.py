#include <iostream>
#include <complex>
#include <cmath>
#include <string>
#include <vector>

using namespace std;

class ComplexMathEngine {
public:
    complex<double> add(complex<double> a, complex<double> b) {
        return a + b;
    }

    complex<double> subtract(complex<double> a, complex<double> b) {
        return a - b;
    }

    complex<double> multiply(complex<double> a, complex<double> b) {
        return a * b;
    }

    complex<double> divide(complex<double> a, complex<double> b) {
        if (b == 0) {
            cerr << "Error: Division by zero" << endl;
            exit(1);
        }
        return a / b;
    }

    complex<double> square_root(complex<double> a) {
        return sqrt(a);
    }

    complex<double> power(complex<double> a, complex<double> b) {
        return pow(a, b);
    }

    complex<double> conjugate(complex<double> a) {
        return conj(a);
    }

    double absolute(complex<double> a) {
        return abs(a);
    }
};

void handle_system_call(string operation, vector<complex<double>>& args) {
    ComplexMathEngine math_engine;
    complex<double> result;
    
    if (operation == "add") {
        result = math_engine.add(args[0], args[1]);
    } else if (operation == "subtract") {
        result = math_engine.subtract(args[0], args[1]);
    } else if (operation == "multiply") {
        result = math_engine.multiply(args[0], args[1]);
    } else if (operation == "divide") {
        result = math_engine.divide(args[0], args[1]);
    } else if (operation == "square_root") {
        result = math_engine.square_root(args[0]);
    } else if (operation == "power") {
        result = math_engine.power(args[0], args[1]);
    } else if (operation == "conjugate") {
        result = math_engine.conjugate(args[0]);
    } else if (operation == "absolute") {
        double abs_val = math_engine.absolute(args[0]);
        cout << abs_val << endl;
        return;
    } else {
        cerr << "Error: Invalid operation" << endl;
        exit(1);
    }
    
    cout << result.real() << " + " << result.imag() << "i" << endl;
}

int main(int argc, char* argv[]) {
    if (argc > 1) {
        string operation = argv[1];
        vector<complex<double>> args;
        for (int i = 2; i < argc; ++i) {
            double real_part, imag_part;
            sscanf(argv[i], "%lf+%lfi", &real_part, &imag_part);
            args.push_back({real_part, imag_part});
        }
        handle_system_call(operation, args);
    } else {
        ComplexMathEngine math_engine;
        complex<double> num1(2, 3);
        complex<double> num2(1, -1);

        cout << "Addition: " << math_engine.add(num1, num2) << endl;
        cout << "Subtraction: " << math_engine.subtract(num1, num2) << endl;
        cout << "Multiplication: " << math_engine.multiply(num1, num2) << endl;
        cout << "Division: " << math_engine.divide(num1, num2) << endl;
        cout << "Square Root of " << num1 << ": " << math_engine.square_root(num1) << endl;
        cout << num1 << " raised to " << num2 << ": " << math_engine.power(num1, num2) << endl;
        cout << "Conjugate of " << num1 << ": " << math_engine.conjugate(num1) << endl;
        cout << "Absolute value of " << num1 << ": ";
        handle_system_call("absolute", {num1});
    }

    return 0;
}
