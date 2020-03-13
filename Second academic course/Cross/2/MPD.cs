using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lab2
{
    class Program
    {
        public static double f(double x)
        {
            //return x * x - 4;
            //return Math.Pow(0.2 * x, 3) - Math.Cos(x);
            return x * Math.Exp(x) - x - 1;
        }

        static void Main(string[] args)
        {
            double a, b, c, Eps = 1e-13;
            int Lich = 0;
            Console.Write("Введiть a: ");
            a = Convert.ToDouble(Console.ReadLine());
            Console.Write("Введiть b: ");
            b = Convert.ToDouble(Console.ReadLine());
            if (f(a) * f(b) > 0)
            {
                Console.WriteLine("Немає коренiв у вказанiй межi");
                Console.ReadLine();
                return;
            }
            if (Math.Abs(f(a)) < Eps)
            {
                Console.WriteLine("x = " + a + " Кiлькiсть крокiв: " + Lich + "Корiнь знаходиться на лiвiй межi");
                Console.ReadLine();
                return;
            }
            else
            if (Math.Abs(f(b)) < Eps)
            {
                Console.WriteLine("x = " + b + " Кiлькiсть крокiв: " + Lich + "\nКорiнь знаходиться на правій межi");
                Console.ReadLine();
                return;
            }
            else
            {
                Console.WriteLine("|    i     |    x     |    y");
                while (Math.Abs(b - a) > Eps)
                {
                    c = (a + b) / 2;
                    Lich++;
                    if (Lich < 10)
                    {
                        Console.WriteLine("|    {0}     |  {1:0.0000}  |   {2}", Lich, c, f(c));
                    }
                    else
                    {
                        Console.WriteLine("|    {0}    |  {1:0.0000}  |   {2}", Lich, c, f(c));
                    }

                    if (Math.Abs(f(c)) < Eps)
                    {
                        Console.WriteLine("x = " + c + " f(x) = " + f(c) + " Кiлькiсть крокiв: " + Lich);
                        Console.ReadLine();
                        return;
                    }
                    else if (f(a) * f(c) < 0) b = c;
                    else a = c;
                }
                Console.WriteLine("x = " + Math.Round((a + b) / 2) + " Кiлькiсть крокiв: " + Lich);
                Console.ReadLine();
                return;
            }
        }
    }
}
