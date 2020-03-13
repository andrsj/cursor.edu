using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab2_Newton
{
    class Program
    {
        class MathLib
        {
            public const double Eps = 1e-10;
            public static double Function(double x)
            {
                // return Math.Exp(-x) - 2 + x * x;
                //return Math.Pow(0.2 * x, 3) - Math.Cos(x); // roots: -4.119 | -1.604 | 1.541 
                return x * Math.Exp(x) - x - 1;
            }
            public static double FunctionP1(double x)
            {
                double D = Eps / 1000;
                return ((Function(x + D) - Function(x)) / D);
            }
            public static double FunctionP2(double x)
            {
                double D = Eps / 1000;
                //return ((FunctionP1(x + D) - FunctionP1(x)) / D);
                return ((Function(x + D) + Function(x - D) - 2 * Function(x))/( D * D ));
            }
        }

        public static void Function(int Kmax, double x)
        {
            double Dx = 0;
            int i = 0;
            for ( ; ; )
            {
                if (MathLib.FunctionP1(x) == 0)
                {
                    Console.WriteLine("Newtonian step becomes infinity");
                    Console.ReadKey();
                    break;
                }
                Dx = MathLib.Function(x) / MathLib.FunctionP1(x);
                x = x - Dx;
                Console.WriteLine("      {0}      |  {1}  |    {2}", i,x,MathLib.Function(x));
                if (Math.Abs(Dx) < MathLib.Eps)
                {
                    Console.WriteLine("\nx = {0} ; f(x) = {1} ; counter - {2}",x,MathLib.Function(x),i);
                    Console.ReadKey();
                    break;
                }
                if (i == Kmax)
                {
                    Console.WriteLine("For Kmax the roots with Eps = " + MathLib.Eps + " not found");
                    Console.ReadKey();
                    break;
                }
                i++;
            }
        }

        static void Main(string[] args)
        {
            double x,a,b;
            int Kmax;
            Console.Write("Enter a: ");
            a = Convert.ToDouble(Console.ReadLine());
            Console.Write("Enter b: ");
            b = Convert.ToDouble(Console.ReadLine());
            Console.Write("Enter Kmax: ");
            Kmax = Convert.ToInt16(Console.ReadLine());
            Console.WriteLine("  Iteration  |         x          |     f(x)        ");
            if (MathLib.Function(a) * MathLib.Function(b) > 0)
            {
                Console.WriteLine("     0       |        None        |     None       " + "\nNo roots in [a;b]");
                Console.ReadKey();
                Environment.Exit(0);
            }

            x = b;
            if (MathLib.Function(x) * MathLib.FunctionP2(x) < 0)
            {
                x = a;
            }
            else
            {
                Function(Kmax, x);
                Environment.Exit(0);
            }
            if (MathLib.Function(x) * MathLib.FunctionP2(x) > 0)
            {
                Function(Kmax, x);
                Environment.Exit(0);
            }
            else
            {
                Console.WriteLine("For this function method Newton`s is not guaranteed");
                Function(Kmax, x);
            }
            Console.Write("End!");
            Console.ReadKey();
        }
    }
}
