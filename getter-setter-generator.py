print("C++ Getters/Setters Generator")
print("By hiraki\n")

seperate = input("Do you want to seperate the declaration and the implementation? [Y/N]: ").lower()
if (seperate == "y"):
    seperate = True
    classname = input("Enter class name: ")

else:
    seperate = False

print("\nPlease enter the member variables as if you are declaring them in a C++ class (with or without semicolons).")
print("You can also paste your existing declaration code here.")
print("Lines can begin or end with spaces, tab characters or semicolons. Failing to comply to these rules might lead to unexpected result.")
print("Enter 'DONE' (in capital, without quotes) to finish.")
print("""\nExample:
string foo
int bar;
float foobar;
AnotherClass barfoo\n""")

declaration = ""
implementation = ""

while True:
    line = input("> ")
    line = line.strip("\n").strip().strip("\t").strip(";")

    if (line == "DONE"):
        break

    try:
        datatype, name = [x.strip() for x in line.split()]
    except:
        print("Not enough parameters to parse.")
        print("Please check that you entered both the datatype and the variable name correctly.")
        continue

    getPrototype = f"{datatype} get{name}()"
    getImplementation = ""

    if (not seperate):
        getPrototype += f" {{\n\treturn this->{name}; \n}}\n\n"
    else:
        getImplementation += f"{datatype} {classname}::get{name}()"
        getImplementation += f" {{\n\treturn this->{name}; \n}}\n\n"
        getPrototype += ";\n"

        implementation += getImplementation
    
    declaration += getPrototype

    setPrototype = f"void set{name}({datatype} {name.lower()})"
    setImplementation = ""

    if (not seperate):
        setPrototype += f" {{\n\tthis->{name} = {name.lower()}; \n}}\n\n"
    else:
        setImplementation += f"void {classname}::set{name}({datatype} {name.lower()})"
        setImplementation += f" {{\n\tthis->{name} = {name.lower()}; \n}}\n\n"
        setPrototype += ";\n"

        implementation += setImplementation
    
    declaration += setPrototype

print(declaration)
print("-----------------------")
print(implementation)