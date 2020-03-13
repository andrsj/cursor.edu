using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Gold
{
    class MathLib
    {
        static public double fi = (1 + Math.Sqrt(5)) / 2;
        static public double Function(double x) { return Math.Pow(0.2 * x, 3) - Math.Cos(x); }
    }                                                                     //return x * x * Math.Pow(Math.E, x); -> -2/0
    class Program                                                         //return (x * x -3) / (x + 2); -> -3/-1
    {                                                                     //return Math.Pow(0.2 * x,3) - Math.Cos(x) ; -> -3/0/~3.4
        static void Main(string[] args)
        {
            double a, b, Eps = 1e-6, x;
            Console.Write(" Метод золотого сечения\n Для того чтоб использовать програму - введите отрезок [a,b] на котором" +
                " хотите найти екстремум функции. \n В отрезке должен быть только ОДИН екстремум, иначе программа выдаст" +
                "неверный ответ.\n Для того чтоб выйти из программы после работы (поиска) ввести \"Exit\".\n");
            while(true)
            { 
                Console.Write(" Enter a: ");
                a = Convert.ToDouble(Console.ReadLine());
                Console.Write(" Enter b: ");
                b = Convert.ToDouble(Console.ReadLine());
                int j = 0;
                do
                {
                    double x1, x2, y1, y2;
                    j++;
                    x1 = b - ((b - a) / MathLib.fi);
                    x2 = a + ((b - a) / MathLib.fi);
                    y1 = MathLib.Function(x1);
                    y2 = MathLib.Function(x2);
                    //if(y1 <= y2) { a = x1; } //MAX
                    if(y1 >= y2) { a = x1; } //MIN
                    else { b = x2; }
                    Console.WriteLine("x1 = {0:0.000000} | x2 = {1:0.000000} for {2} iteration", x1, x2, j);
                }
                while (Math.Abs(b - a) > Eps);
                x = (a + b) / 2;
                Console.WriteLine(" Екстремум функции x = {0:0.####} , f(x) = {1:0.####}, кол-тво итераций - {2} ", x, MathLib.Function(x), j);
                string key;
                key = Console.ReadLine();
                if (key == "Exit") { Environment.Exit(0); }

            }
        }
    }
}
