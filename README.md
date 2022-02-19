# sus
Sussy baka programming language

crewmate x;
x = 4;

sus(1 > 2){
    x = 5;
} 

Program Syntax

program = "print", "(", expression, ")", ";" ;

expression = number, { ("+"|"-"), number }, ";" ;

identifier = alphabetic character, {alphabetic character | digit} ;
number = [ "-" ], digit, {digit} ;
string '"' , {all characters - '"' }, '"' ;
assignment = identifier, "=", (number|string) ;
digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
white space = ? white space characters ? ;
all characters = ? all visible characters ? ;