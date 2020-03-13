using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace lab11_demo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

        }

        private TabStorage MyStorage;
        public static string GlobalStringParametr;
        private void Form1_Load(object sender, EventArgs e)
        {
            MyStorage = new TabStorage();
            DGStorage.DataSource = MyStorage.TStorage;
            MyStorage.ColumnPropSet(DGStorage);
        }

        private void buttonAddRowToTable_Click(object sender, EventArgs e)
        {
            Decimal pPrice = 0;
            Int32 pCount = 0;
            if (tbGroup.Text == "")
            {
                MessageBox.Show("Group empty");
                return;
            }
            if (tbName.Text == "")
            {
                MessageBox.Show("Empty Name");
                return;
            }
            if (tbMaker.Text == "")
            {
                MessageBox.Show("Empty Maker");
                return;
            }
            try
            {
                if (tbPrice.Text != "")
                    pPrice = Convert.ToDecimal(tbPrice.Text);
            }
            catch
            {
                MessageBox.Show("PRICE!");
                return;
            }
            try
            {
                if (tbCount.Text != "")
                    pCount = Convert.ToInt32(tbCount.Text);
            }
            catch
            {
                MessageBox.Show("COUNT!");
                return;
            }
            MyStorage.TabStorageAddRow(tbGroup.Text, tbName.Text, tbMaker.Text, pPrice, pCount);
            MyStorage.SetSum(DGStorageSum);
        }

        private void записатиToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MyStorage.ZapTabFile();
            MessageBox.Show("Таблиця записана у файл");
        }

        private void зчитатиToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MyStorage.ReadTabFile(DGStorageSum);
            MessageBox.Show("Зчитано з файлу");
        }

        private void встановитиФільтрToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form FilterDialod = new FormFilterAndSort();
            FilterDialod.Text = "Введіть критерій фільтрування (Приклад: Група = 'книги' & Ціна < 70";
            GlobalStringParametr = MyStorage.Filter;
            FilterDialod.ShowDialog();
            MyStorage.TabStorageValueFilter(GlobalStringParametr, DGStorage);
        }

        private void знятиФільтрToolStripMenuItem_Click(object sender, EventArgs e)
        {
            GlobalStringParametr = "";
            MyStorage.TabStorageValueFilter(GlobalStringParametr, DGStorage);
        }

        private void встановитиСортуванняToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form SortedForm = new FormFilterAndSort();
            SortedForm.Text = "Введіть критерій сортування (Приклад: Виробник, Ціна Desc";
            GlobalStringParametr = MyStorage.Sort;
            SortedForm.ShowDialog();
            MyStorage.TabStorageValueSort(GlobalStringParametr, DGStorage, DGStorageSum);
        }

        private void знятиСортуванняToolStripMenuItem_Click(object sender, EventArgs e)
        {
            GlobalStringParametr = "";
            MyStorage.TabStorageValueSort(GlobalStringParametr, DGStorage, DGStorageSum);
        }

        private void сортуванняПоГРУПІToolStripMenuItem_Click(object sender, EventArgs e)
        {
            GlobalStringParametr = "Група, Назва";
            MyStorage.TabStorageValueSort(GlobalStringParametr, DGStorage, DGStorageSum);
        }

        private void пошукПоНазвіToolStripMenuItem_Click(object sender, EventArgs e)
        {
            string Name;
            Form SearchDialog = new FormFilterAndSort();
            SearchDialog.Text = "Введіть назву:";
            SearchDialog.ShowDialog();
            MyStorage.SearchName(GlobalStringParametr, DGStorage);
        }
    }
}
