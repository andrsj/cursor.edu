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
    public enum StanMjacha
    {
        vGriA,
        vGriB,
        pozaGroju,
        vCentri,
        vVorotahA,
        vVorotahB
    }
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        public static string newLine = "\r";
        public static string sumText = "";
        public static string PlanText = "";
        public static int j = 1;

        private void button1_Click(object sender, EventArgs e)
        {
            PlanText = "Планується зробити:" + newLine;
            sumText = "Початок роботи:" + newLine;
            int i = 1;
            label2.Text = sumText + newLine;
            PlanText = PlanText + Convert.ToString(1) +
            ". Плануємо створити екземпляр класу Футбол_мяч, викликавши конструктор" +
            "з параметром" + newLine; i++;
            Futbol_mjach fm = new Futbol_mjach(StanMjacha.vCentri);
            if(String.IsNullOrEmpty(sumText)) { sumText = ""; }
            int GolA = 0, GolB = 0;
            fm.masa = 0.6F;
            fm.rkuli = 0.12F;
            fm.TstanMjacha = StanMjacha.vGriA;
            PlanText = PlanText + Convert.ToString(i) + ". Плануємо викликати метод Попав ( T , ref GolA) " +
            "перевизначений в класі Футбол_Мяч [overrride]" + newLine; i++;
            fm.popav(true, ref GolA);
            PlanText = PlanText + Convert.ToString(i) + ". Плануємо викликати метод Попав ( Т , ref GolA , ref GolB) " +
            " перевизначений у класі Футбол_Мяч з іншою сигнатурою ніж у базовому класі " + newLine; i++;
            fm.Popav(true, ref GolA, ref GolB);
            PlanText = PlanText + Convert.ToString(i) + ", " + Convert.ToString(i + 1) +
            ". Плануємо за посередністю методу ПопавBASE ( T , ref GolA) класу Футбол_Мяч " +
            "викликати метод Попав класу Мяч" + newLine; i++; i++;
            fm.PopavBase(true, ref GolA);
            double s, v;
            PlanText = PlanText + Convert.ToString(i) + ". Плануємо викликати метод Удар (2 , out v, 200, 0.1)" +
            " класу Футбол_Мяч" + newLine; i++;
            s = fm.Udar(2, out v, 200, 0.1);
            PlanText = PlanText + Convert.ToString(i) + ". Плануємо викликати метод Котитись ( 5 , 1 ) класу Сфера" +
            " з класу Футбол_Мяч " + newLine; i++;
            s = fm.Kotytys(5, 1);
            PlanText = PlanText + Convert.ToString(i) + ". Плануємо викликати метод Летіти ( 20 , 30 ) класу Сфера з класу " +
            "Футбол_Мяч " + newLine; i++;
            s = fm.Letity(20, 30);
            PlanText = PlanText + Convert.ToString(i) + ". Плануємо викликати метод Летіти ( 20 , 30 , 5 ) з класу" +
            " Футбол_Мяч" + newLine; i++;
            s = fm.Letity(20, 30, 5);
            label1.Text = PlanText;
            label2.Text = sumText;

        }
    }
    public class Sphere
    {
        public const double Pi = Math.PI;
        double r, l, v, s, m;
        public double rkuli
        {
            get { return r; }
            set
            {
                r = value; l = 2 * Pi * r; v = 4 * Pi * r * r * r;
                s = 4 * Pi * r * r;
            }
        }
        public double lKola { get { return l; } }
        public double vKuli { get { return v; } }
        public double sKuli { get { return s; } }
        public double masa
        {
            get { return m; }
            set { m = value; }
        }
        virtual public double Kotytys(double t, double v)
        {
            Form1.sumText = Form1.sumText + Convert.ToString(Form1.j) +
            ". Виконано метод Котитись ( ) класу СФЕРА" + Form1.newLine;
            Form1.j++;
            return 2 * Pi * r * t * v;
        }
        virtual public double Letity(double t, double v)
        {
            Form1.sumText = Form1.sumText + Convert.ToString(Form1.j) +
            ". Виконано метод Летіти ( ) класу СФЕРА" + Form1.newLine;
            Form1.j++;
            return t * v;
        }
        virtual public double Udar(double t, out double v, double f, double t1)
        {
            v = f * t1 / m;
            Form1.sumText = Form1.sumText + Convert.ToString(Form1.j) +
            ". Виконано метод Удар ( ) класу СФЕРА s = v * t = " +
            Convert.ToString(t * v) + Form1.newLine;
            Form1.j++;
            return t * v;
        }
    }
    public class Mjach : Sphere
    {
        virtual public void popav(bool je, ref int kilkist)
        {
            if (je) kilkist++;
            Form1.sumText = Form1.sumText + Convert.ToString(Form1.j) +
            ". Виконано метод Попав ( ) класу МЯЧ. К-сть = " +
            Convert.ToString(kilkist) + Form1.newLine;
            Form1.j++;
        }
        virtual public double Letity(double t, double v, double ftertcja)
        {
            Form1.sumText = Form1.sumText + Convert.ToString(Form1.j) +
            ". Виконано метод Летіти ( ) класу МЯЧ" + Form1.newLine;
            Form1.j++;
            return t * v - ftertcja / masa * t * t / 2;
        }
        public double LetityBase(double t, double v)
        {
            Form1.sumText = Form1.sumText + Convert.ToString(Form1.j) +
            ". Виконано метод ЛетітиBase" +
            " ( ) класу МЯЧ" + Form1.newLine;
            Form1.j++;
            return base.Letity(t, v);
        }
    }
    public class Povitrjana_kulja : Sphere
    {
        double tysk, maxTysk;
        public double tyskGazu
        {
            get { return tysk; }
            set { tysk = value; }
        }
        public double MaxTyskGazu
        {
            get { return maxTysk; }
            set { maxTysk = value; }
        }
        public bool Lopatys()
        {
            Form1.sumText = Form1.sumText + Convert.ToString(Form1.j) +
            ". Виконано метод Лопатись ( ) класу ПОВІТРЯНА КУЛЯ" + Form1.newLine;
            Form1.j++;
            if (tysk > maxTysk) return true; else return false;
        }
        public double Letity(double t, double v, double vVitru, double kutVitru)
        {
            Form1.sumText = Form1.sumText + Convert.ToString(Form1.j) +
            ". Виконано метод Летіти ( ) класу ПОВІТРЯНА КУЛЯ" + Form1.newLine;
            Form1.j++;
            return t * v - vVitru * Math.Sin(kutVitru);
        }
        new public double Letity(double t, double v)
        {
            double s;
            s = t * v;
            Form1.sumText = Form1.sumText + Convert.ToString(Form1.j) +
            ". Виконано метод Летіти ( ) класу ПОВІТРЯНА КУЛЯ. Ми пролетіли" +
            Convert.ToString(s) + " метрів!" + Form1.newLine;
            Form1.j++;
            return s;
        }
    }
    public class Futbol_mjach : Mjach
    {
        StanMjacha stanM;
        public StanMjacha TstanMjacha { get => stanM; set => stanM = value; }
        public bool stanOut
        {
            get
            {
                if (stanM == StanMjacha.pozaGroju) return true;
                else return false;
            }
        }
        public Futbol_mjach(StanMjacha sm)
        {
            Form1.sumText = Form1.sumText + Convert.ToString(Form1.j) +
            ". Виконано конструктор Футбол_мяч ( ) " + Form1.newLine;
            Form1.j++;
            stanM = sm;
            masa = 0.5F;
            rkuli = 0.1F;
        }
        public void Popav(bool je, ref int kilkistA, ref int kilkistB)
        {
            if (je)
            {
                if (stanM == StanMjacha.vGriA) kilkistA++;
                else if (stanM == StanMjacha.vGriB) kilkistB++;
                Form1.sumText = Form1.sumText + Convert.ToString(Form1.j) +
                ". Виконано метод Попав ( ) класу ФУТБОЛ_МЯЧ з (bool, ref int, ref int)" +
                Form1.newLine; Form1.j++;
            }
        }
        public void PopavBase(bool b, ref int i)
        {
            Form1.sumText = Form1.sumText + Convert.ToString(Form1.j) +
            ". Виконано метод Попав ( ) класу ФУТБОЛ_МЯЧ з (bool b, ref int i)" +
            Form1.newLine; Form1.j++;
            base.popav(b, ref i);
        }
        override public void popav(bool je, ref int kilkist)
        {
            if (je) kilkist++;
            Form1.sumText = Form1.sumText + Convert.ToString(Form1.j) +
            ". Виконано метод Попав ( ) класу ФУТБОЛ_МЯЧ з (bool je, ref int kilkist) [override]" +
            Form1.newLine; Form1.j++;
        }
        public override double Letity(double t, double v, double ftertcja)
        {
            Form1.sumText = Form1.sumText + Convert.ToString(Form1.j) +
            ". Виконано метод Летіти ( ) класу ФУТБОЛ_МЯЧ з (double , double , double) [override]" +
            Form1.newLine; Form1.j++;
            return t * v - ftertcja / masa * t * t / 2 ;
        }
    }

}

