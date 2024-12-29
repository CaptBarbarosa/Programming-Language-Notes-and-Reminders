using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Strings_in_CSharp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string city = "Ankara", city2 = "Istanbul";
            Console.WriteLine(String.Format("{0} {1}",city, city2)); //If we define this within the Console.WriteLine we didn't create a new variable
        }
    }
}
