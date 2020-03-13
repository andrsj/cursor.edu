using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;

namespace lab7_demo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.timer1.Interval = 1000;
            this.timer1.Enabled = true;
            this.timer1.Stop();
            this.folderBrowserDialog1.Description =
            "Виберіть будь ласка каталог з файлами типу .jpg (фотографії)";
            this.folderBrowserDialog1.ShowNewFolderButton = false;
            this.folderBrowserDialog1.RootFolder = Environment.SpecialFolder.MyComputer;
            this.button3.Enabled = false;
            this.button4.Enabled = false;
            this.label1.Visible = false;
            this.button2.Enabled = false;
            this.button5.Enabled = false;
            this.radioButton1.Enabled = false;
            this.radioButton2.Enabled = false;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string sourse = "*.jpg";
            switch (comboBox1.SelectedIndex)
            {
                case 0: sourse = "*.jpg"; break;
                case 1: sourse = "*.png"; break;
            }
            folderBrowserDialog1.ShowDialog(); // Відкрити вікно для вибору каталогу
            DirectoryInfo d = new DirectoryInfo(folderBrowserDialog1.SelectedPath);
            int i; // Поле для лічильника файлів з фотографіями
            i = Convert.ToInt16(label2.Text); // Лічильник файлів з фотографіями зберігаємо у мітці label2
            FileInfo[] fis = d.GetFiles(sourse); // Вибираємо лише jpg - файли
            if (fis.GetLength(0) == 0) // Перевіряємо, чи є у вибраному каталогу фотографії
            {
                MessageBox.Show("Виберіть, будь ласка, інший каталог. У цьому немає " + sourse +"-файлів");
                return;
            }
            if (i > fis.GetLength(0))
            {
                i = 0;
                label2.Text = i.ToString();
            }
            // Засилаємо у вікно для малюнка перший вибраний з каталога малюнок (фото)
            pictureBox1.ImageLocation = fis[i].DirectoryName + "\\" + fis[i].Name;
            pictureBox1.Load();
            button2.Visible = true; //робимо видимою кнопку Старт
            radioButton1.Enabled = true;
            radioButton2.Enabled = true;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (this.button2.Text == "Старт")
            {
                this.button2.Text = "Стоп";
                this.timer1.Start();
                button1.Visible = false;
                label1.Visible = true;
            }
            else
            {
                this.button2.Text = "Старт";
                this.timer1.Stop();
                button1.Visible = true;
                label1.Visible = false;
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            string sourse = "*.jpg";
            switch (comboBox1.SelectedIndex)
            {
                case 0: sourse = "*.jpg"; break;
                case 1: sourse = "*.png"; break;
            }
            this.label1.Text = Convert.ToString(System.DateTime.Now);
            int i;
            i = Convert.ToInt16(label2.Text);
            i++;
            label2.Text = i.ToString();
            DirectoryInfo d = new DirectoryInfo(folderBrowserDialog1.SelectedPath);
            FileInfo[] fis = d.GetFiles(sourse);
            if( i >= fis.GetLength(0))
            {
                timer1.Stop();
                MessageBox.Show("Спочатку!");
                
            }
            timer1.Start();
            if( i >= fis.GetLength(0))
            {
                i = 0;
                label2.Text = i.ToString();   
            }
            pictureBox1.ImageLocation = fis[i].DirectoryName + "\\" + fis[i].Name;
            pictureBox1.Load();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string sourse = "*.jpg";
            switch (comboBox1.SelectedIndex)
            {
                case 0: sourse = "*.jpg"; break;
                case 1: sourse = "*.png"; break;
            }
            int i = Convert.ToInt16(label2.Text);
            i++;
            label2.Text = i.ToString();
            DirectoryInfo d = new DirectoryInfo(folderBrowserDialog1.SelectedPath);
            FileInfo[] fis = d.GetFiles(sourse);
            if (i >= fis.GetLength(0))
            {
                MessageBox.Show("Прокрутка з початку");
                i = 0;
                label2.Text = i.ToString();
            }
            pictureBox1.ImageLocation = fis[i].DirectoryName + "\\" + fis[i].Name;
            pictureBox1.Load();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string sourse = "*.jpg";
            switch (comboBox1.SelectedIndex)
            {
                case 0: sourse = "*.jpg"; break;
                case 1: sourse = "*.png"; break;
            }
            int i = Convert.ToInt16(label2.Text);
            DirectoryInfo d = new DirectoryInfo(folderBrowserDialog1.SelectedPath);
            FileInfo[] fis = d.GetFiles(sourse);
            if (i == 0)
            {
                MessageBox.Show("Прокрутка з кінця");
                i = fis.Length;
                label2.Text = i.ToString();                
            }
            i--;
            label2.Text = i.ToString();           
            pictureBox1.ImageLocation = fis[i].DirectoryName + "\\" + fis[i].Name;
            pictureBox1.Load();
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            this.button3.Enabled = false;
            this.button4.Enabled = false;
            this.button2.Enabled = true;
            label1.Visible = true;
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {           
            this.button3.Enabled = true;
            this.button4.Enabled = true;
            this.button5.Enabled = true;
            this.button2.Enabled = false;
            label1.Visible = false;
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            this.label3.Visible = false;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string sourse = "*.jpg";
            switch (comboBox1.SelectedIndex)
            {
                case 0: sourse = "*.jpg"; break;
                case 1: sourse = "*.png"; break;
            }
            int i = Convert.ToInt16(label2.Text);
            Random rnd = new Random();            
            DirectoryInfo d = new DirectoryInfo(folderBrowserDialog1.SelectedPath);
            FileInfo[] fis = d.GetFiles(sourse);
            i = rnd.Next(0, fis.Length);
            label2.Text = i.ToString(); 
            pictureBox1.ImageLocation = fis[i].DirectoryName + "\\" + fis[i].Name;
            pictureBox1.Load();
        }
    }
}
