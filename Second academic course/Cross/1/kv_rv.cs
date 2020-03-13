using System; // Kvadr. Rivn. XIO
namespace kv_r
{
	class Program
   	{
 		static void Main(string[] args)
     		{
   			double a, b, c, d, Re, Im, x1, x2;
			Console.Write("¬ведите число a: ");
            			a = Convert.ToDouble(Console.ReadLine());
			Console.Write("¬ведите число b: ");
            			b = Convert.ToDouble(Console.ReadLine());
			Console.Write("¬ведите число c: ");
            			c = Convert.ToDouble(Console.ReadLine());	
   			d = b * b - 4 * a * c;
   			if (d < 0)
   			{
    				Re = - b / (2 * a);
				Im = Math.Sqrt ( Math.Abs(d) ) / (2 * a);
				Console.WriteLine("\n X1 = {0} +j {1} \n X2 = {0} -j {1} \n",Re,Im);
   			}
   			else
   			{
				if (d == 0)
				{
					x1 = -b / (2 * a);
					Console.WriteLine("\n X1 = X2 = {0} ",x1);
				}
				else
				{
					x1 = (-b + Math.Sqrt(d)) / (2 * a);
     					x2 = (-b - Math.Sqrt(d)) / (2 * a);
					Console.WriteLine("\n X1 = {0} \n X2 = {1}",x1,x2);
				}
   			}
  			Console.WriteLine("\n Press <ENTER> ");
		}
	}
}