using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ExampleDelegate
{
    class Program
    {
        delegate void Operation(int a, int b);
        static void Main(string[] args)
        {
            Operation op;
            op = Add;
            op += Minus;
            op += Multiply;
            op += Divide;
            op(20, 4);
            Console.ReadKey();
        }
        static void Add (int a,int b)
        {
            Console.WriteLine(a + b);
        }
        static void Multiply (int a, int b)
        {
            Console.WriteLine(a * b);
        }
        static void Minus (int a, int b)
        {
            Console.WriteLine(a - b);
        }
        static void Divide (int a, int b)
        {
            Console.WriteLine(a / b);
        }
    }
}
