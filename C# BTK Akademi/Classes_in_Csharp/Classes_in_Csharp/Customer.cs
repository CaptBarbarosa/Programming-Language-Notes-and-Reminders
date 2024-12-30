using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Classes_in_Csharp
{
    internal class Customer
    {
        // Properties
        /*
        public int ID { get; set; }
        public string Name { get; set; }
        public string Surname { get; set; }
        public string Address { get; set; }
        */
        private int _id;
        public int Id 
        {
            get { return _id; } 
            set { _id = value; }
        }

        private string _firstName;
        public string FirstName
        {
            get {
                Console.WriteLine("You are in the get method for _firstName");
                return _firstName; 
            }
            set {
                Console.WriteLine("You are in the set method for _firstName");
                _firstName = value; 
            }
        }

        private string _lastName;
        public string LastName
        {
            get { return _lastName; }
            set { _lastName = value; }
        }

        private string _address;
        public string Address
        {
            get { return _address; }
            set { _address = value; }
        }
    }
}
