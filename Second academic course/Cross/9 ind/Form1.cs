using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Threading;
using System.Drawing.Drawing2D;

namespace lab9_demo
{
    public partial class Form1 : Form
    {
        class Draw
        {
            double h, krx, kry, maxx, maxy, minx, miny, kx, ky, zx, zy, gx = 0, gy = 0, xx, yy;
            int L, krokx, kroky;
            double[] xe = new double[1000];
            double[] ye = new double[1000];
            private double f(double x)
            {
                //return Math.Sqrt(x);
                return x * x - 1000;
                //return x * Math.Sin(x);
            }
            public void Build(double al, double bl, int ne, PictureBox pictureBox1)
            {
                Pen p = new Pen(Color.Black);
                p.DashStyle = DashStyle.Dot;
                p.Color = Color.Black;
                Graphics pbl = pictureBox1.CreateGraphics();
                L = 10;
                h = (bl - al) / (ne - 10);
                xe[0] = al;
                for (int i = 0; i <= ne - 1; i++)
                {
                    ye[i] = f(xe[i]);
                    xe[i + 1] = xe[i] + h;
                }
                maxx = xe[ne - L];
                minx = xe[0];
                maxy = ye[0];
                miny = ye[0];
                for (int i = L; i <= ne - L; i++)
                {
                    if (maxy < ye[i]) maxy = ye[i];
                    if (miny > ye[i]) miny = ye[i];
                }

                // коефіціенти масштабування

                kx = (pictureBox1.Width - 2 * L) / (maxx - minx);
                ky = (pictureBox1.Height - 2 * L) / (miny - maxy);
                zx = (pictureBox1.Width * minx - L * (minx + maxx)) / (minx - maxx);
                zy = (pictureBox1.Height * maxy - L * (miny + maxy)) / (maxy - miny);

                // обчислення параметрів для побудови рухомих осей

                if (minx * maxx <= 0) gx = 0;
                if (minx * maxx > 0) gx = minx;
                if ((minx * maxx > 0) && (minx < 0)) gx = maxx;
                if (miny * maxy <= 0) gy = 0;
                if ((miny * maxy > 0) && (miny > 0)) gy = miny;
                if ((miny * maxy > 0) && (miny < 0)) gy = maxy;

                // обчислення відстаней між лініями сітки

                krokx = (pictureBox1.Width - 2 * L) / 10;
                kroky = (pictureBox1.Height - 2 * L) / 10;

                // побудова гратки

                int mr1, mr2, mr3, mr4, mr5;
                for (int i = 0; i <= 10; i++)
                {
                    mr1 = mr2 = mr3 = mr4 = (int)Math.Round(ky * gy + zy);
                    mr5 = (int)Math.Round(kx * gx + zx);
                    pbl.DrawLine(p, L, mr3 - i * kroky, pictureBox1.Width - L, mr4 - i * kroky);
                    pbl.DrawLine(p, L, mr3 + i * kroky, pictureBox1.Width - L, mr4 + i * kroky);
                    pbl.DrawLine(p, mr5 + i * krokx, L, mr5 + i * krokx, pictureBox1.Height - L);
                    pbl.DrawLine(p, mr5 - i * krokx, L, mr5 - i * krokx, pictureBox1.Height - L);

                }

                // побудова рухомих осец координат

                p.Color = Color.Blue;
                p.DashStyle = DashStyle.Solid;
                p.Width = 2;
                int w1 = (int)Math.Round(ky * gy + zy),
                    w2 = (int)pictureBox1.Width - L,
                    w3 = (int)Math.Round(ky * gy + zy),
                    w4 = (int)Math.Round(kx * gx + zx),
                    w5 = (int)Math.Round(kx * gx + zx);
                pbl.DrawLine(p, L, w1, w2, w3);
                pbl.DrawLine(p, w4, L, w5, pictureBox1.Height - L);
                xx = minx;
                yy = maxy;

                // обчислення кроків для масштабних підписів

                krx = (maxx - minx) / 10;
                kry = (maxy - miny) / 10;

                // виведення масштабних підписів

                for (int i = 0; i <= 10; i++)
                {
                    mr1 = (int)Math.Round(ky * gy + zy);
                    mr2 = (int)Math.Round(kx * gx + zx);
                    pbl.DrawString(Convert.ToString(Math.Round(xx, 1)), new Font(new FontFamily("Arial"), 8), Brushes.Black, new Point(i * krokx, mr1 - L + 15));
                    pbl.DrawString(Convert.ToString(Math.Round(yy, 1)), new Font(new FontFamily("Arial"), 8), Brushes.Black, new Point(mr2 - L + 15, L + i * kroky - 4));
                    xx = xx + krx;
                    yy = yy - kry;
                }

                p.Color = Color.Red;
                p.Width = 2;

                // побудова графіка

                for (int i = 2; i < ne - L; i++)
                {
                    Thread.Sleep(3);
                    mr1 = (int)Math.Round(kx * xe[i - 1] + zx);
                    mr2 = (int)Math.Round(ky * ye[i - 1] + zy);
                    mr3 = (int)Math.Round(kx * xe[i] + zx);
                    mr4 = (int)Math.Round(ky * ye[i] + zy);
                    pbl.DrawLine(p, new Point(mr1, mr2), new Point(mr3, mr4));
                }
            }
        }

        double al = 0;
        double bl = 0;
        int ne = 800;

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            pictureBox1.Refresh();
            try
            {
                al = Convert.ToDouble(textBox1.Text);
                bl = Convert.ToDouble(textBox2.Text);
            }
            catch (Exception)
            {
                MessageBox.Show("Межі задано не правильно", "Помилка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                textBox1.Text = "";
                textBox2.Text = "";
                return;
            }
            Draw draw = new Draw();
            draw.Build(al, bl, ne, pictureBox1);
        }
    }
}
