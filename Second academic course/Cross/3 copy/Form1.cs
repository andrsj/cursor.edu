using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace windowsMPDNewton
{

    public partial class Form1 : Form
    {
        class Functions
        {
            //public const double Eps = 1;
            public static double Function(double x, ref int k1)
            {
                switch (k1)
                {
                    case 0: return x * x - 4;
                    case 1: return 4 * x * x * x - 2 * x * x - 4;
                    case 2: return Math.Pow(0.2 * x, 3) - Math.Cos(x); //roots: -4.119 | -1.604 | 1.541
                                                                       //extr:  max -3 / min 0 / max ~3.4
                }
                return 0;
            }
            public static double FirstDerivative(double x, double d, ref int k1)
            {
                return (Function(x + d, ref k1) - Function(x, ref k1)) / d;
            }
            public static double SecondDerivative(double x, double d, ref int k1)
            {
                return (Function(x + d, ref k1) + Function(x - d, ref k1) - 2 * Function(x, ref k1)) / (d * d);
            }
            public static double MPD(double a, double b, double Eps, ref int k1, ref int L)
            {
                double c = 0, Fc;
                while (b - a > Eps)
                {
                    c = 0.5 * (b - a) + a;
                    L++;
                    Fc = Function(c, ref k1);
                    if (Math.Abs(Fc) < Eps)
                    { return c; }
                    if (Function(a, ref k1) * Fc > 0) { a = c; }
                    else { b = c; }
                }
                return c;
            }
            public static double MN(double a, double b, double Eps, ref int k1, int Kmax, ref int L)
            {
                double x = b, XD = 0.0, D = Eps / 100;
                int i;
                if (Function(x, ref k1) * SecondDerivative(x, D, ref k1) < 0) { x = a; }
                if (Function(x, ref k1) * SecondDerivative(x, D, ref k1) < 0)
                { MessageBox.Show("Для цього рівняння збіжність ітерацій не гарантована"); }
                for (i = 1; i <= Kmax; i++)
                {
                    XD = Function(x, ref k1) / FirstDerivative(x, D, ref k1);
                    x = x - XD;
                    if (Math.Abs(XD) < Eps) { L = i; return x; }
                }
                MessageBox.Show("За задану кількість ітерацій кореня не знайдено");
                return -1000;
            }
            public static double Gold(double a, double b, double Eps, ref int k1, ref int L, bool check)
            {
                double fi = (1 + Math.Sqrt(5)) / 2;
                //int j = 0;
                do
                {
                    double x1, x2, y1, y2;
                    L++;
                    x1 = b - ((b - a) / fi);
                    x2 = a + ((b - a) / fi);
                    y1 = Function(x1, ref k1);
                    y2 = Function(x2, ref k1);
                    if (check == true)
                    {
                        if (y1 <= y2) { a = x1; } //MAX 
                        else { b = x2; }
                    }
                    else                          //
                    {
                        if (y1 >= y2) { a = x1; } //MIN
                        else { b = x2; }
                    }
                }
                while (Math.Abs(b - a) > Eps);
                return (a + b) / 2;
            }
        }
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int L = 0, k = -1, Kmax, m = -1;
            double D, Eps = 0, a, b;
            switch (comboBox1.SelectedIndex)
            {
                case 0: m = 0; break;
                case 1:
                    {
                        m = 1;
                        D = Eps / 100;
                        label7.Visible = true;
                        textBox4.Visible = true;
                        textBox4.Enabled = true;
                    } break;
                case 2: m = 2; break;
            }
            if (m == -1)
            {
                MessageBox.Show("Оберіть метод!");
                return;
            }
            textBox1.Enabled = true;
            textBox2.Enabled = true;
            switch (comboBox2.SelectedIndex)
            {
                case 0: k = 0; break;
                case 1: k = 1; break;
                case 2: k = 2; break;
            }
            if(k == -1)
            {
                MessageBox.Show("Оберіть рівняння!");
                return;
            }
            if (textBox1.Text == "")
            {
                MessageBox.Show("Де число А?");
                textBox1.Focus();
                return;
            }
            a = Convert.ToDouble(textBox1.Text);
            if (textBox2.Text == "Де число В?")
            {
                MessageBox.Show("");
                textBox2.Focus();
                return;
            }
            b = Convert.ToDouble(textBox2.Text);
            if (textBox3.Text == "Де Eps?")
            {
                MessageBox.Show("");
                textBox3.Focus();
                return;
            }
            Eps = Convert.ToDouble(textBox3.Text);
            if((Eps > 1e-1) || (Eps <= 0))
            {
                Eps = 1e-4;
                textBox3.Text = Convert.ToString(Eps);
            }
            if (m == 0)
            {
                if ((Functions.Function(a, ref k) * (Functions.Function(b, ref k))) > 0)
                {
                    MessageBox.Show("");
                    textBox1.Text = "";
                    textBox2.Text = "";
                    textBox1.Focus();
                    return;
                }
                if(Math.Abs(Functions.Function(a,ref k)) < Eps)
                {
                    textBox5.Text = Convert.ToString(a);
                    textBox6.Text = Convert.ToString(L);
                    return;
                }
                if (Math.Abs(Functions.Function(b, ref k)) < Eps)
                {
                    textBox5.Text = Convert.ToString(b);
                    textBox6.Text = Convert.ToString(L);
                    return;
                }
            }
            switch (m)
            {
                case 0:
                    {
                        textBox5.Text = String.Format("{0:f4}", Functions.MPD(a, b, Eps, ref k, ref L));
                        //textBox5.Text = Convert.ToString(Functions.MPD(a, b, Eps, ref k, ref L));
                        textBox6.Text = Convert.ToString(L);
                        textBox7.Text = Convert.ToString(Functions.Function(Functions.MPD(a,b,Eps,ref k, ref L), ref k));
                        //label9.Text = "К-сть поділів = "; 
                    } break;
                case 1:
                    {
                        if(textBox4.Text == "")
                        {
                            MessageBox.Show("Де Кмах?");
                            textBox4.Focus();
                            return;
                        }
                        Kmax = Convert.ToInt32(textBox4.Text);
                        textBox5.Text = String.Format("{0:f4}", Functions.MN(a, b, Eps, ref k, Kmax, ref L));
                        //textBox5.Text = Convert.ToString(Functions.MN(a, b, Eps, ref k, Kmax, ref L));
                        textBox6.Text = Convert.ToString(L);
                        textBox7.Text = String.Format("{0:f4}",Functions.Function(Functions.MN(a,b,Eps,ref k,Kmax,ref L), ref L));
                        //MessageBox.Show("" + Functions.Function(Functions.MN(a,b,Eps,ref k,Kmax, ref L), ref L) + "");
                        //textBox7.Text = Convert.ToString(Functions.Function(Functions.MN(a, b, Eps, ref k, Kmax, ref L), ref L));
                        //label9.Text = "К-сть ітерацій = ";
                    } break;
                case 2:
                    {
                        textBox5.Text = String.Format("{0:f4}", Functions.Gold(a, b, Eps, ref k, ref L, radioButton2.Checked));
                        textBox6.Text = Convert.ToString(L);
                        textBox7.Text = String.Format("{0:f4}",Functions.Function(Functions.Gold(a, b, Eps, ref k, ref L, radioButton2.Checked), ref k));
                    } break;
            }
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            switch (comboBox1.SelectedIndex)
            {
                case 0:
                    {
                        label7.Visible = false;
                        textBox4.Visible = false;
                        radioButton1.Visible = false;
                        radioButton2.Visible = false;
                    } break;
                case 1:
                    {
                        label7.Visible = true;
                        textBox4.Visible = true;
                        radioButton1.Visible = false;
                        radioButton2.Visible = false;
                    } break;
                case 2:
                    {
                        label7.Visible = false;
                        textBox4.Visible = false;
                        radioButton1.Visible = true;
                        radioButton2.Visible = true;
                    } break;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Clear();
            textBox2.Clear();
            textBox3.Clear();
            textBox4.Clear();
            textBox5.Clear();
            textBox6.Clear();
            textBox7.Clear();
            switch (comboBox1.SelectedIndex)
            {
                case 0: { label7.Visible = false; textBox4.Visible = false; } break;
                case 1: { label7.Visible = true; textBox4.Visible = true; } break;
            }
        }

        private void textBox3_KeyPress(object sender, KeyPressEventArgs e)
        {
            if(e.KeyChar == (char)Keys.Enter) { button1_Click(this,new EventArgs()); }
        }

        private void textBox4_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (char)Keys.Enter) { button1_Click(this, new EventArgs()); }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label7.Visible = false;
            textBox4.Visible = false;
            radioButton1.Visible = false;
            radioButton2.Visible = false;
        }
    }
}
