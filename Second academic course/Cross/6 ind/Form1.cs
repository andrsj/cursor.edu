using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace lab6_demo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public class Triangle
        {
            public int[] PointA = new int[3];
            public int[] PointB = new int[3];
            public int[] PointC = new int[3];
            public Triangle()
            {
                PointA[0] = 1;
                PointA[1] = 1;
                PointA[2] = 1;

                PointB[0] = 1;
                PointB[1] = 1;
                PointB[2] = 1;

                PointC[0] = 1;
                PointC[1] = 1;
                PointC[2] = 1;
            }
            public Triangle(int[] num)
            {
                this.PointA[0] = num[0];
                this.PointA[1] = num[1];
                this.PointA[2] = num[2];

                this.PointB[0] = num[3];
                this.PointB[1] = num[4];
                this.PointB[2] = num[5];

                this.PointC[0] = num[6];
                this.PointC[1] = num[7];
                this.PointC[2] = num[8];
            }
            public double Line(int[] A, int[] B)
            {
                return
                    Math.Sqrt(Math.Pow((B[0] - A[0]), 2) +
                    Math.Pow((B[1] - A[1]), 2) +
                    Math.Pow((B[2] - A[2]), 2));
            }
            public double Perimeter(int[] A, int[] B, int[] C)
            {
                return Line(A,B) + Line(A,C) + Line(B,C); 
            }
            public double Area(int[] A, int[] B, int[] C)
            {
                double p = Perimeter(A,B,C) / 2;
                return 
                    Math.Sqrt( p * ( p - Line(A,B) ) * ( p - Line(A,C) ) * ( p - Line(B,C) ) );
            }
            public string Info()
            {
                return 
                    Convert.ToString(Line(PointA, PointB)) + " - довжина прямої AB\n" +
                    Convert.ToString(Line(PointA, PointC)) + " - довжина прямої AC\n" +
                    Convert.ToString(Line(PointB, PointC)) + " - довжина прямої BC\n" +
                    Convert.ToString(Perimeter(PointA, PointB, PointC)) + " - периметр ABC\n" +
                    Convert.ToString(Area(PointA, PointB, PointC)) + " - площа ABC\n";
            }
        }

        public class Piramida : Triangle
        {
            public int[] PointD = new int[3];
            public Piramida(int[] numb) : base(numb)
            {
                PointD[0] = 1;
                PointD[1] = 1;
                PointD[2] = 1;
            }
            public Piramida(int[] numb, int[] num) : base(numb)
            {
                this.PointD[0] = num[0];
                this.PointD[1] = num[1];
                this.PointD[2] = num[2];
            }
            public double SummArea(double ABC, double ABD, double ACD, double BCD)
            {
                return ABC + ABD + ACD + BCD;
            }
            public string Info(int[] A, int[] B, int[] C)
            {
                return
                    Convert.ToString(Line(A, B)) + " - довжина прямої 1\n" +
                    Convert.ToString(Line(A, C)) + " - довжина прямої 2\n" +
                    Convert.ToString(Line(B, C)) + " - довжина прямої 3\n" +
                    Convert.ToString(Perimeter(A, B, C)) + " - периметр \n" +
                    Convert.ToString(Area(A, B, C)) + " - площа \n"; 
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int[] coordinatsABC = new int[] { 2, 1, 2, 3, 4, 1, 6, 1, 0 };
            int[] coordinatsD = new int[] { 4, 3, -1 };
            
            Triangle lol = new Triangle(coordinatsABC);
            Piramida plol = new Piramida(coordinatsABC,coordinatsD);
            //Piramida plol = new Piramida(coordinatsABC);
            label1.Text =  
                " Відомості про піраміду\n" +
                "\n Грань ABC\n" +
                plol.Info(plol.PointA, plol.PointB, plol.PointC) +
                "\n Грань ABD\n" +
                plol.Info(plol.PointA, plol.PointB, plol.PointD) +
                "\n Грань BCD\n" +
                plol.Info(plol.PointB, plol.PointC, plol.PointD) +
                "\n Грань ACD\n" +
                plol.Info(plol.PointA, plol.PointC, plol.PointD);

            label3.Text =
                " Відомості про трикутник\n" +
                lol.Info() +
                "_________________________\n\n" +
                Convert.ToString(plol.SummArea(
                    plol.Area(plol.PointA, plol.PointB, plol.PointC),
                    plol.Area(plol.PointA, plol.PointB, plol.PointD),
                    plol.Area(plol.PointA, plol.PointD, plol.PointC),
                    plol.Area(plol.PointB, plol.PointD, plol.PointC)
                    )) + " - сума всіх площ піраміди ABCD";


            label2.Text =
                string.Join(" ", lol.PointA) + " - Точка А \n" +
                string.Join(" ", lol.PointB) + " - Точка B \n" +
                string.Join(" ", lol.PointC) + " - Точка C \n" + "\n" +
                string.Join(" ", plol.PointA) + " - Точка А піраміди \n" +
                string.Join(" ", plol.PointB) + " - Точка B піраміди\n" +
                string.Join(" ", plol.PointC) + " - Точка C піраміди\n" +
                string.Join(" ", plol.PointD) + " - Точка D піраміди\n";
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}

