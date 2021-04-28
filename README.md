# C++ Getters and Setters Generator
A simple Python script to generate C++ getters and setters.

Some IDEs (such as Visual Studio, which is required by my university) have no extension (afaik) to generate setters and getters for C++ classes, which might become a pain in the ass when the class has over 10 member attributes.<br>
Using this script is pretty straightforward. Just execute it using a Python 3 intepreter, then follow the guidance on your screen.

Not supported: keywords such as `static`, `virtual`, `inline`, `override`, `public`, `private`, .... Type them in can lead to unexpected results.

Features:
- Seperate class header and implementation.
- You can type the member variables directly into the program, or simply paste your existing class declaration code.
