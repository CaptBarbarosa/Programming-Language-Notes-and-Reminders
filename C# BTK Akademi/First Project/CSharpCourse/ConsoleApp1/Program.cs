using System;

class Program
{
    static void Main()
    {
        Console.WriteLine(Days.Thursday);
        Console.WriteLine((int)Days.Thursday);
    }
    enum Days
    {
        Monday, Tuesday, Wednesday, Thursday=5, Friday, Saturday, Sunday
    }
}
