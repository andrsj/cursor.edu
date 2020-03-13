using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace lab5_demo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        public class CaseStudentInfo
        {
            public string FirstName { get; set; }
            public string LastName { get; set; }
            public string Subject { get; set; }
            public int Score { get; set; }
            StudentSubjectName[] SubjectNames;    
            CaseStudentInfo[] StudentInfo;  
            public int Length;     
            public int ErrorCode;   

            public CaseStudentInfo(int size, string sFirstName, string sLastName, string sSubject, int iScore)
            {
                StudentInfo = new CaseStudentInfo[size]; 
                Length = size;
                setSubjectName(); 
                FirstName = sFirstName;
                LastName = sLastName;
                Subject = sSubject;
                Score = iScore;
            } 

            struct StudentSubjectName // Структура для опису префіксів імен транзисторів
            {
                public string SubjectName;
            }

            // Перевизначений метод для видруку інформації про транзистор
            public override string ToString()
            {
                return " Ім'я: " + FirstName + " Прізвище: " + LastName + " Предмет: " + Subject + " Оцінка" + Score;
            }

            void setSubjectName()
            {
                SubjectNames = new StudentSubjectName[10];

                SubjectNames[0].SubjectName = "ООП";
                SubjectNames[1].SubjectName = "Електроніка";
                SubjectNames[2].SubjectName = "Схемотехніка";
                SubjectNames[3].SubjectName = "Кросплатформне";
                SubjectNames[4].SubjectName = "Мат.аналіз";
                SubjectNames[5].SubjectName = "Алгоритми";
                SubjectNames[6].SubjectName = "Мережі";
                SubjectNames[7].SubjectName = "Бази даних";
                SubjectNames[8].SubjectName = "Дискретна";
                SubjectNames[9].SubjectName = "ДВВ";

            }

            bool OkSubjectName(string subject)
            {
                for(int i=0; i<10; i++)
                {
                    if (SubjectNames[i].SubjectName == subject) return true;
                }
                return false;
            }

            bool OkIndex(int i)
            {
                if (i >= 0 && i < Length) return true; else return false;
            }
           
            public CaseStudentInfo this[int index]
            {
                get 
                {
                    if (OkIndex(index))
                    {
                        ErrorCode = 0;
                        return StudentInfo[index];
                    }
                    else
                    {
                        ErrorCode = 1;
                        return null;
                    }
                }
                set 
                {
                    if(!OkIndex(index)) { ErrorCode = 1; return; }
                    if(!OkSubjectName(value.Subject.ToString())) { ErrorCode = 2; return; }
                    StudentInfo[index] = value;
                    ErrorCode = 0;
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            CaseStudentInfo MyStud = new CaseStudentInfo(3, "name", "p", "ООП", 1);

            CaseStudentInfo MyStud1 = new CaseStudentInfo(1, "1", "1", "ООП", 1); 
            CaseStudentInfo MyStud2 = new CaseStudentInfo(1, "2", "2", "Мережа", 1);
            CaseStudentInfo MyStud3 = new CaseStudentInfo(1, "3", "3", "Електроніка", 1);
            CaseStudentInfo MyStud4 = new CaseStudentInfo(1, "4", "4", "ДВВ", 1);

            CaseStudentInfo[] Massive = new CaseStudentInfo[] { MyStud1, MyStud2, MyStud3, MyStud4};

            //Massive[0] = MyStud1;
            //Massive[1] = MyStud2;
            //Massive[2] = new CaseStudentInfo(1, "5", "5", "Мат.аналіз", 1);
            string Message = " ";
            for (int j = 0; j < Massive.Length; j++)
            {
                MyStud[j] = Massive[j];
                if (MyStud.ErrorCode > 0)
                    Message = Message + "\n Не додано студента " + Massive[j].LastName + " , код помилки: " + MyStud.ErrorCode;
                else
                    Message = Message + "\n Студента " + Massive[j].LastName + " " + Massive[j].FirstName
                        + " з предметом " + Massive[j].Subject + " та оцінкою" + Massive[j].Score + " додано ";
            }
            //Message = Convert.ToString (Massive.Length);


            label1.Text = Message;
            Message = "";

            for(int i=0; i<MyStud.Length; i++)
            {
                if (MyStud[i] != null) Message = Message + "\n" + Convert.ToString(i + 1) + " " + MyStud[i].ToString();
            }
            label2.Text = Message;

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            button1_Click(sender, e);
        }
    }
}
