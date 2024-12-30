using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Classes_in_Csharp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            CustomerManager myCustomerManager = new CustomerManager();
            myCustomerManager.Add();
            myCustomerManager.Update();

            Customer my_customer = new Customer();
            my_customer.Id=1;
            my_customer.FirstName = "Kaan";

            Customer my_customer2 = new Customer{Id = 2, FirstName = "Kaan", 
                LastName = "2", Address = "Istanbul"
            };

            Console.WriteLine(my_customer2.FirstName);
            
        }
    }

    
}
