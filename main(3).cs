using System;

class MainClass {
public static void Main (string[] args) {
Console.WriteLine ("Hello World");
Console.WriteLine("Please try and work backwards to get Num 4's ");


//basic sequence
Console.WriteLine("N2 is 250");
int N1 = 500; // declaring the var int N1 = 500
int N2 = 250;
int N4 = -850;
int N3 = N1 + N2; // declaring N3 = N1 +N2 this makes the var N3 and uses addition
Console.WriteLine("N1 + N2 = " + N3);
//Selection
if(N2 < N1){
Console.WriteLine("N2 is less then N1");
}
Console.WriteLine("N3 is N1 + N2");
Console.WriteLine("N3 + N4 = -100");

  if(N3 > N4 )
  {
  Console.WriteLine("N4 is negative"); // regular write to console 
  }
Console.WriteLine("The awnser is -850");
//Iteration
int[] number = {1,5,3,2,4,3};
Console.WriteLine("The first value in the array is: " + number[0] + "\n The last value is " + number[5]);

for (int i = 0; i < number.Length; i++)
{
Console.WriteLine("Element " + i + " In the array: " + number[i]);
}
}
}