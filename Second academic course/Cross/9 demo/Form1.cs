using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace lab9_demo
{
    public partial class Form1 : Form
    {
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
