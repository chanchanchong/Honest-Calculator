# Work on project Stage 3/5: Total recall
### Project: Honest Calculator

### Description
Take a look at the upgraded flowchart. As before, the old blocks are red-colored. Be
careful; some flows can now work differentely.

![](../../../../../../AppData/Local/Temp/Stage3.jpg)

Objectives
To complete this stage, you need to implement the flowchart above. While doing it, please, follow our recommendations below:

Don't use the built-in function eval() to calculate from a string;
The memory variable must be of a float type;
There are no tests when M is negative. For example, there will be no test input like this: -M + 6;
Copy two messages. The tests will check if the correct message appears in the correct order. Don't add extra lines or characters.
msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"
Example
The greater-than symbol followed by a space (> ) represents the user input. Note that it's not part of the input.

Example 1:

Enter an equation
> 3 + 3

6

Do you want to store the result? (y / n):
>y

Do you want to continue calculations? (y / n):
>y

> 5 + M
11

Do you want to store the result? (y / n):
>y

Do you want to continue calculations? (y / n):
>n