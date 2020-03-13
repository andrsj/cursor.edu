using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace XIO_Demo_Delegate
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        public class Car
        {
            public int CurrentSpeed { get; set; }
            public int MaxSpeed { get; set; }
            public string PetName { get; set; }
            private bool carIsDead;  // Поле для перевірки, чи автомобіль не зламався
            public Car() // Конструктор класу
            {
                MaxSpeed = 100;
            }
            public Car(string name, int maxSp, int currSp) // Конструктор з параметрами
            {
                MaxSpeed = maxSp;
                CurrentSpeed = currSp;
                PetName = name;
            }

            // Оголошення делегата у класі Car
            public delegate void CarEngineHandler(string msgForCaller);
            // Оголошення приватної змінної listOfHandlers типу делегат 

            CarEngineHandler listOfHandlers;

            // Додавання методу для доступу до змінної listOfHandlers ззовні
            public void RegisterWithCarEngine(CarEngineHandler metodToCall)
            {

                // Змінній типу делегат присвоюємо метод, що має сигнатуру, яка вказана при оголошенні делегата
                listOfHandlers = metodToCall;
            }

            /* Метод для зміни поточної швидкості автомобіля. Він буде викликати процес
            створення повідомлення і додавання його до тексту мітки. У залежності від швидкості 
            автомобіля, будуть генеруватись різні повідомлення */
            public void Accselerate(int delta)
            {
                if (carIsDead)

                {

                    /* Змінна типу делегат listOfHandlers запускає метод, вказаний при її створенні з
                    параметрами, заданими в операторі звертання до змінної. Перевіримо, чи передано 
                    метод у змінну listOfHandlers і якщо так, то викликаємо метод, адреса якого записана 
                    у змінній listOfHandlers */
                    if (listOfHandlers != null)
                        listOfHandlers("На жаль автомобіль зламався");
                }
                else
                {
                    CurrentSpeed += delta;

                    // Перевіряємо , чи передано метод у змінну listOfHandlers, а також
                    // перевіряємо, чи не занадто велика швидкість і якщо так, то видаємо повідомлення
                    if ((MaxSpeed - CurrentSpeed < 10) && listOfHandlers != null)
                    // Викликаємо метод, записаний у делегаті за допомогою змінної типу делегат з новими параметрами 
                    {
                        listOfHandlers("Увага! Занадто велика  швидкість!");
                    }
                    else
                    {
                        if (CurrentSpeed >= MaxSpeed)
                            carIsDead = true;
                        else
                            listOfHandlers("Поточна швидкість = " + CurrentSpeed.ToString());
                    }
                }
            }
        }
        public void OnCarEngineEvent(string msg)
        {
            label1.Text = label1.Text + msg + " \n";
        }
        private void button1_Click(object sender, EventArgs e)
        {
            {

                // Створюємо об'єкт типу Car
                Car myCar = new Car("Авто Запорожець", 100, 0);
                // Створимо метод, адресу якого будемо передавати делегату
        // Створимо о змінну типу делегат і зашлемо в неї адресу методу, який буде викликатись через цю змінну
                Car.CarEngineHandler myDelegat = new Car.CarEngineHandler(OnCarEngineEvent);
        // Звернемось до методу RegisterWithCarEngine, щоб вказати метод, який повинен викликатись (зареєструвати) 
                myCar.RegisterWithCarEngine(myDelegat);
                // Ми можемо викликати метод OnCarEngineEvent і поза делегатом

                OnCarEngineEvent("Вмикаємо запалювання ");

                // Будемо змінювати швидкість автомобіля і відслідковувати, що буде
                for (int i = 0; i < 10; i++)
                    myCar.Accselerate(10); 
            }
        }
    }
}
        