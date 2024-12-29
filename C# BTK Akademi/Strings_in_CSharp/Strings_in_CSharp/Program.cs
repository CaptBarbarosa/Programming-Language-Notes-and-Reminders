﻿using System;
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
            int res = city.Length;
            Console.WriteLine(res);
            var city3 = city.Clone();
            Console.WriteLine(city3);

            bool ends_with = city.EndsWith("a");
            Console.WriteLine(ends_with);

            string name = "Hi, my name is Kaan";

            var index_of = name.IndexOf("name"); // If it is unable to find it will return -1.
            Console.WriteLine(index_of);


        }
    }
}