using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Methodds
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("30 + 30: {0}",Add(30));
            int number1 = 10;
            Console.WriteLine("Initially number1 was {0}",number1);
            send_ref(ref number1);
            Console.WriteLine("After number1 was {0}", number1);

            int number2 = 20;
            Console.WriteLine("\n\nInitially number2 was {0}", number2);
            send_out(out number2);
            Console.WriteLine("After number2 was {0}", number2);

            Console.WriteLine("Summation of 10+20+30+40 is: {0}",Add(10,20,30,40));


        }
        static int Add(int number1 = 20, int number2 = 30) { 
            return number1 + number2;
        }

        static int Add(params int[] numbers) {
            return numbers.Sum();
        }

        static void send_ref(ref int num1) {
            num1 = 20;
        }

        static void send_out(out int num1)
        {
            num1 = 50; // If you are sending an out, you have to set it at least once.
        }
    }
}
