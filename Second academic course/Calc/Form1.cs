using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Calculator
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void buttonNumberZero_Click(object sender, EventArgs e)
        {
            label2.Text += (sender as Button).Text;
            if ((sender as Button).Text == ",")
                buttonComma.Enabled = false;
        }

        private void buttonClear_Click(object sender, EventArgs e)
        {
            label2.Text = "";
            label3.Text = "";
            buttonComma.Enabled = true;
        }
        public double a,b,c;

        private void buttonEnd_Click(object sender, EventArgs e)
        {
            b = Convert.ToDouble(label2.Text);
            switch (znak)
            {
                case "+": c = a + b; break;
                case "-": c = a - b; break;
                case "x": c = a * b; break;
                case "/": c = a / b; break;
                case "x*": c = Math.Pow(a, b); break;
            }
            label3.Text = a.ToString() + " " + znak + " " + b.ToString() + " =";
            label2.Text = c.ToString();
        }

        private void buttonPlusMinus_Click(object sender, EventArgs e)
        {
            if (label2.Text != "")
                if (label2.Text[0] == '-')
                    label2.Text = label2.Text.Remove(0, 1);
                else label2.Text = '-' + label2.Text;
        }

        private void buttonClearOneChar_Click(object sender, EventArgs e)
        {
            if (label2.Text != "")
                label2.Text = label2.Text.Remove(label2.Text.Length - 1, 1);
            bool enabled = true;
            for (int i = 0; i < label2.Text.Length; i++)
                if (label2.Text[i] == ',')
                    enabled = false;
            buttonComma.Enabled = enabled;

        }

        private void Form1_KeyUp(object sender, KeyEventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            label2.Text = Math.PI.ToString();
            buttonComma.Enabled = false;
        }

        private void button16_Click(object sender, EventArgs e)
        {
            a = Convert.ToDouble(label2.Text);
            znak = (sender as Button).Text;
            switch (znak)
            {
                case "sin": b = Math.Sin(a); break;
                case "cos": b = Math.Cos(a); break;
                case "tan": b = Math.Tan(a); break;
                case "log": b = Math.Log10(a); break;
                case "ln":  b = Math.Log(a); break;
                case "√":   b = Math.Sqrt(a); break;
            }
            label3.Text = znak + " ( " + a + " ) = ";
            label2.Text = b.ToString();
        }

        private void button21_Click(object sender, EventArgs e)
        {
            label2.Text = Math.E.ToString();
            buttonComma.Enabled = false;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            a = Convert.ToDouble(label2.Text);
            a *= a;
            label2.Text = a.ToString();
            label3.Text = a + "^2 = ";
            buttonComma.Enabled = true;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            buttonComma.Enabled = false;
            buttonPlus.Enabled = false;
            button2.Enabled = false;
            button3.Enabled = false;
            button4.Enabled = false;
            ControlBox = false;
        }

        private void button16_Click_1(object sender, EventArgs e)
        {
            Close();
        }

        private void label2_TextChanged(object sender, EventArgs e)
        {
            buttonComma.Enabled = true;
            for (int i = 0; i < label2.Text.Length; i++)
                if (label2.Text[i] == ',')
                    buttonComma.Enabled = false;
            if (label2.Text == "")
            {
                buttonPlus.Enabled = false;
                button2.Enabled = false;
                button3.Enabled = false;
                button4.Enabled = false;
                buttonComma.Enabled = false;
            }
            else
            {
                buttonPlus.Enabled = true;
                button2.Enabled = true;
                button3.Enabled = true;
                button4.Enabled = true;
            }
        }

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            void znakSender(Keys key)
            {
                a = Convert.ToDouble(label2.Text);
                switch (key)
                {
                    case Keys.OemMinus: znak = "-"; break;
                    case Keys.Subtract: znak = "-"; break;
                    case Keys.Oemplus: znak = "+"; break;
                    case Keys.Add: znak = "+"; break;
                    case Keys.Multiply: znak = "x"; break;
                    case Keys.Divide: znak = "/"; break;
                }
                label2.Text = "";
                label3.Text = a + " " + znak;
            }

            switch (e.KeyCode)
            {
                case Keys.D1: label2.Text += "1"; break;
                case Keys.D2: label2.Text += "2"; break;
                case Keys.D3: label2.Text += "3"; break;
                case Keys.D4: label2.Text += "4"; break;
                case Keys.D5: label2.Text += "5"; break;
                case Keys.D6: label2.Text += "6"; break;
                case Keys.D7: label2.Text += "7"; break;
                case Keys.D8: label2.Text += "8"; break;
                case Keys.D9: label2.Text += "9"; break;
                case Keys.D0: label2.Text += "0"; break;

                case Keys.NumPad1: label2.Text += "1"; break;
                case Keys.NumPad2: label2.Text += "2"; break;
                case Keys.NumPad3: label2.Text += "3"; break;
                case Keys.NumPad4: label2.Text += "4"; break;
                case Keys.NumPad5: label2.Text += "5"; break;
                case Keys.NumPad6: label2.Text += "6"; break;
                case Keys.NumPad7: label2.Text += "7"; break;
                case Keys.NumPad8: label2.Text += "8"; break;
                case Keys.NumPad9: label2.Text += "9"; break;
                case Keys.NumPad0: label2.Text += "0"; break;

                case Keys.OemMinus: znakSender(e.KeyCode); break;
                case Keys.Oemplus: znakSender(e.KeyCode); break;
                case Keys.Add: znakSender(e.KeyCode); break;
                case Keys.Subtract: znakSender(e.KeyCode); break;
                case Keys.Divide: znakSender(e.KeyCode); break;
                case Keys.Multiply: znakSender(e.KeyCode); break;

                case Keys.Back:
                    if (label2.Text != "")
                        label2.Text = label2.Text.Remove(label2.Text.Length - 1, 1);
                    bool enabled = true;
                    for (int i = 0; i < label2.Text.Length; i++)
                        if (label2.Text[i] == ',')
                            enabled = false;
                    buttonComma.Enabled = enabled;
                    break;
                case Keys.Enter:
                    b = Convert.ToDouble(label2.Text);
                    switch (znak)
                    {
                        case "+": c = a + b; break;
                        case "-": c = a - b; break;
                        case "x": c = a * b; break;
                        case "/": c = a / b; break;
                        case "x*": c = Math.Pow(a, b); break;
                    }
                    label3.Text = a.ToString() + " " + znak + " " + b.ToString() + " ="; 
                    label2.Text = c.ToString();
                    break;
            }
        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            MessageBox.Show(a + "\n" + b + "\n" + c);
        }

        string znak = "+";
        private void buttonPlus_Click(object sender, EventArgs e)
        {
            a = Convert.ToDouble(label2.Text);
            znak = (sender as Button).Text;
            label2.Text = "";
            label3.Text = a.ToString() + " " + znak + " =";
        }
    }
}
