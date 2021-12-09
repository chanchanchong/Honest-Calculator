# Work on project Stage 3/5: The laziness test
### Project: Honest Calculator

### Description
Implement the flowchart below. Take a good look - there are two functions. The old
blocks are in red. Be careful; some flows can now work differently.
![](../../../../../../AppData/Local/Temp/Stage4.jpg)

Objectives
Implement the flowchart with two functions. Please, mind the recommendations below:
- Don't use the built-in function eval() to calculate from a string;
- Copy the messages carefully. The tests will check if the correct message appears in
  the correct order. Don't add extra lines or characters.

>msg_6 = " ... lazy"

>msg_7 = " ... very lazy"

>msg_8 = " ... very, very lazy"

>msg_9 = "You are"
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

Enter an equation
> 2 / M

You are ... lazy

Yeah... division by zero. Smart move...

Enter an equation
> 1 * M

You are ... lazy ... very lazy ... very, very lazy

0.0

Do you want to store the result? (y / n):
> n

Do you want to continue calculations? (y / n):
> y

Enter an equation
> 899 * 0

You are ... very, very lazy

0.0

Do you want to store the result? (y / n):
> n

Do you want to continue calculations? (y / n):
> n