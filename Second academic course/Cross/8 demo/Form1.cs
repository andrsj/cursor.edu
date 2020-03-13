using System;
using System.Collections.Generic;
using System.Collections;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace lab8_demo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        public class MyBook
        {
            public int BookNumber { get; set; }
            public String Avtor { get; set; }
            public String Nazva { get; set; }
            public String Vydavnytstvo { get; set; }
            public Int16 RikVyhodu { get; set; }
            public MyBook(int bookNumber, String Avtor, String Nazva, String Vydavnytstvo, Int16 RikVyhodu)
            {
                this.BookNumber = bookNumber;
                this.Avtor = Avtor;
                this.Nazva = Nazva;
                this.Vydavnytstvo = Vydavnytstvo;
                this.RikVyhodu = RikVyhodu;
            }
            public override string ToString()
            {
                return "Книга №" + BookNumber.ToString() + " Автор " + Avtor.ToString() + " Назва " +
                Nazva.ToString() + " Видавництво " + Vydavnytstvo.ToString() + " Рік: " + RikVyhodu.ToString();
            }
        }




        public class MyBooks1 : ArrayList, IEnumerable
        {
            public MyBook[] MyBooksArray { get; set; }
            public MyBooks1(int KilkistKnyh)
            // Це конструктор класу. Він відразу створює масив із
            // елементів типу book кількістю, заданою у параметрі
            {
                MyBooksArray = new MyBook[KilkistKnyh];
            }
        }
        // Ітератор для класу MyBooks1 створювати не потрібно, оскільки він є у класі ArrayList



        // Клас містить власну реалізацію методу GetEnumerator
        public class MyBooks2 : IEnumerable
        {
            MyBook[] myBooksArray;
            // (Нище) Це конструктор класу. Він відразу створює масив із елементів типу book кількістю, заданою у параметрі
            public MyBook[] MyBooksArray { get; set; }
            public MyBooks2(int KilkistKnyh)
            {
                MyBooksArray = new MyBook[KilkistKnyh];
            }
            // (Нище) Це ітерарор класу MyBooks. Тут використано ітератор класу array, оскільки myBooksArray має цей тип
            public IEnumerator GetEnumerator()
            {
                return myBooksArray.GetEnumerator();
            }

        }




        // Цей клас підтримує також інтерфейс IEnumerator, який дозволяє рухатись по елементах масиву з доп.методу MoveNext
        // Від класу MyBooks2 він відрізняється тим, що у класі MyBooks3 створено свій індексатор, 
        // а також повністю з нуля реалізовано інтерфейси IEnumerable та Ienumerator. 
        // Інтерфейс IEnumerable вимагає наявності одного лиш методу GetEnumerator(),
        // інтерфейс IEnumerator вимагає 3 методи: Current(), MoveNext() i Reset(), які дозволяють позиціювати елемент масиву.
        // Додано також метод Add для додавання нових книг у масив.
        public class MyBooks3 : IEnumerable, IEnumerator
        {
            MyBooks3[] myBooksArray; // Це масив для індексатора
            int kilkistKnyh = 0; 
            int CurrentNomer = 0;
            int bookNomer { get; set; }
            String Avtor { get; set; }
            String Nazva { get; set; }
            String Vydavnyctvo { get; set; }
            public Int16 RikVyhodu { get; set; }
            int position = -1;

            public MyBooks3(int kilkistKnyh, int bookNomer, String Avtor,
            String Nazva, String Vydavnyctvo, Int16 RikVyhodu)
            {
                if (kilkistKnyh <= 0) return;
                this.myBooksArray = new MyBooks3[kilkistKnyh];
                this.kilkistKnyh = kilkistKnyh;
                this.bookNomer = bookNomer;
                this.Avtor = Avtor;
                this.Nazva = Nazva;
                this.Vydavnyctvo = Vydavnyctvo;
                this.RikVyhodu = RikVyhodu;
            }
            public MyBooks3(int kilkistKnyh)
            {
                myBooksArray = new MyBooks3[kilkistKnyh];
                this.myBooksArray = new MyBooks3[kilkistKnyh];
                this.kilkistKnyh = kilkistKnyh;
                bookNomer = 0;
            }
            public MyBooks3 this[int index]
            {
                get { if (index <= kilkistKnyh && index >= 0) return myBooksArray[index]; else return null; }
                set { if (index < kilkistKnyh) myBooksArray[index] = value; }
            }
            public IEnumerator GetEnumerator()
            {
                foreach (MyBooks3 b in myBooksArray)
                {
                    yield return (IEnumerator)b;
                }
            }
            public object Current
            {
                get { if (position >= 0 && position < kilkistKnyh) return myBooksArray[position]; else return null; }
            }
            public bool MoveNext()
            {
                position++;
                return (position < kilkistKnyh);
            }
            public void Reset()
            {
                position = -1;
            }
            public override string ToString()
            {
                return "Книга №" + bookNomer.ToString() + " Автор: " + Avtor + " Назва: " + Nazva + 
                    " Видавництво: " + Vydavnyctvo + " Рік: " + RikVyhodu.ToString();
            }
            public void Add(int bookNomer, String Avtor, String Nazva, 
            String Vydavnyctvo, Int16 RikVyhodu, ref int KodError)
            {
                if (CurrentNomer < kilkistKnyh)
                {
                    myBooksArray[CurrentNomer] = new MyBooks3(1)
                    {
                        bookNomer = bookNomer,
                        Avtor = Avtor,
                        Nazva = Nazva,
                        Vydavnyctvo = Vydavnyctvo,
                        RikVyhodu = RikVyhodu
                    };
                    CurrentNomer++;
                    KodError = 0; 
                }
                else KodError = 1; 
            }
        }





        public void Message(int KodError)
        {
            if (KodError > 0) MessageBox.Show(" Не вдалось додати книжку, оскільки масив переповнений ");
        }





        private void button1_Click(object sender, EventArgs e)
        {
            string ss = "Вивід для класу MyBooks1 \n";
            MyBooks1 mbs1 = new MyBooks1(3);
            mbs1.MyBooksArray[0] = new MyBook(1, "Marija Remark", "Три товариші", "Ранок", 1981);
            mbs1.MyBooksArray[1] = new MyBook(2, "Нестайко", "У країні сонячних зайчиків", "Ранок", 1961);
            mbs1.MyBooksArray[2] = new MyBook(3, "Баскаков", "Радиотехнические цепи и сигналы ", "М.:Высшая школа", 2000);
            foreach (MyBook b in mbs1.MyBooksArray)
            {
                if (b != null) ss = ss + b.ToString() + "\n";
            }
            ss = ss + "\nВивід для класу MyBooks2 \n";
            MyBooks2 mbs2 = new MyBooks2(3);
            mbs2.MyBooksArray[0] = new MyBook(1, "Marija Remark", "Три товариші", "Ранок", 1981);
            mbs2.MyBooksArray[1] = new MyBook(2, "Нестайко", "У країні сонячних зайчиків", "Ранок", 1961);
            mbs2.MyBooksArray[2] = new MyBook(3, "Баскаков", "Радиотехнические цепи и сигналы ", "М.: Высшая школа", 2000);
            foreach (MyBook b in mbs2.MyBooksArray)
            {
                if (b != null) ss = ss + b.ToString() + "\n";
            }
            ss = ss + "\nВивід для класу MyBooks3 \n";
            int KodError = 0;
            MyBooks3 mbs3 = new MyBooks3(5);    
            mbs3.Add(1, "Еріх Марія Ремарк", "Три товариші", "Ранок", 1981, ref KodError); 
            Message(KodError);
            mbs3.Add(2, "Нестайко", "У країні сонячних зайчиків", "Ранок", 1961, ref KodError);
            Message(KodError);
            mbs3.Add(3, "Баскаков", "Радиотехнические цепи и сигналы ", "М.: Высшая школа", 2000, ref KodError);
            Message(KodError);
            mbs3.Add(4, "Загребельний ", "Роксолана", "Світанок", 2000, ref KodError);
            Message(KodError);
            mbs3.Add(5, "В.Косик", "Україна і Німеччина у другій світовій війні ", "Наукове товариство ім.Шевченка у Львові", 1993, ref KodError);
            Message(KodError);
            foreach (MyBooks3 b in mbs3)
            {
                if (b != null) ss = ss + b.ToString() + "\n";
            }
            // position = -1
            mbs3.MoveNext();
            // position = 0
            ss = ss + "\nВивід текучого елементу\n";
            ss = ss + mbs3.Current.ToString() + "\n";
            ss = ss + "Ще раз MoveNext\n";
            mbs3.MoveNext();
            ss = ss + mbs3.Current.ToString();
            mbs3.Reset();
            label1.Text = ss;
        }
    }
}

