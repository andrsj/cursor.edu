using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data;
using System.Drawing;
using System.Windows.Forms;
using System.IO;

namespace lab11_demo
{
    class TabStorage
    {
        public DataTable TStorage = new DataTable();
        public DataView StorageView;



        public TabStorage()
        {
            DataColumn cNpp = new DataColumn("Н _за_ пп");
            DataColumn cNameGroup = new DataColumn("Група");
            DataColumn cNameProduct = new DataColumn("Назва");
            DataColumn cMaker = new DataColumn("Виробник");
            DataColumn cCount = new DataColumn("Кількість");
            DataColumn cPrise = new DataColumn("Ціна");
            DataColumn cCost = new DataColumn("Вартість");

            cNpp.DataType = System.Type.GetType("System.Int32");
            cNameGroup.DataType = System.Type.GetType("System.String");
            cMaker.DataType = System.Type.GetType("System.String");
            cCount.DataType = System.Type.GetType("System.Int32");
            cPrise.DataType = System.Type.GetType("System.Decimal");
            cCost.DataType = System.Type.GetType("System.Decimal");

            TStorage.Columns.Add(cNpp);
            TStorage.Columns.Add(cNameGroup);
            TStorage.Columns.Add(cNameProduct);
            TStorage.Columns.Add(cMaker);
            TStorage.Columns.Add(cPrise);
            TStorage.Columns.Add(cCount);
            TStorage.Columns.Add(cCost);

            StorageView = new DataView(TStorage);
        }



        public string Filter;
        public string Sort;
        public void TabStorageValueFilter(string pFilter, DataGridView DGV)
        {
            try
            {
                StorageView.RowFilter = pFilter;
                Filter = pFilter;
                DGV.DataSource = StorageView;
            }
            catch
            {
                MessageBox.Show("Введений фільтр неправильний");
                return;
            }
        }



        public void TabStorageValueSort(string pSort, DataGridView DGV, DataGridView DGVsum)
        {
            try
            {
                StorageView.Sort = pSort;
                Sort = pSort;
                DGV.DataSource = StorageView;
                DGV.Refresh();
            }
            catch
            {
                MessageBox.Show("Введений сортувальник неправильний");
                return;
            }
        }



        public void SearchName(string sName, DataGridView DGV)
        {
            int nn = -1;
            for (int i = 0; i < DGV.Rows.Count; i++)
            {
                if ((string)DGV.Rows[i].Cells["Назва"].Value == sName)
                {
                    nn = i;
                    break;
                }
            }
            if (nn >= 0)
            {
                DGV.FirstDisplayedCell = DGV.Rows[nn].Cells["Назва"];
                DGV.Rows[nn].Selected = true;
                DGV.CurrentCell = DGV.Rows[nn].Cells["Назва"];
            }
            else
            {
                MessageBox.Show("Значення не знайдено");
            }
        }



        public void TabStorageAddRow (string pNameGroup, string pNameProduct, string pMaker, decimal pPrice, int pCount)
        {
            int nn;
            nn = TStorage.Rows.Count;
            DataRow rowStorage = TStorage.NewRow();
            rowStorage["Н _за_ пп"] = nn++;
            rowStorage["Група"] = pNameGroup;
            rowStorage["Назва"] = pNameProduct;
            rowStorage["Виробник"] = pMaker;
            rowStorage["Ціна"] = pPrice;
            rowStorage["Кількість"] = pCount;
            rowStorage["Вартість"] = pCount * pPrice;
            TStorage.Rows.Add(rowStorage);
        }



        public void ColumnPropSet(DataGridView DGV)
        {
            DGV.Columns[0].HeaderText = "# за п/п";
            DGV.Columns[1].HeaderText = "Група";
            DGV.Columns[2].HeaderText = "Назва";
            DGV.Columns[3].HeaderText = "Виробник";
            DGV.Columns[4].HeaderText = "Ціна";
            DGV.Columns[5].HeaderText = "Кількість";
            DGV.Columns[6].HeaderText = "Вартість";

            DGV.Columns[0].ReadOnly = true;
            DGV.Columns[6].ReadOnly = true;
            DGV.Columns[1].Width = 40;
            DGV.Columns[2].Width = 100;
            DGV.Columns[3].Width = 160;
            DGV.Columns[4].Width = 70;
            DGV.Columns[5].Width = 70;
            DGV.Columns[6].Width = 70;

            DGV.Columns[0].DefaultCellStyle.BackColor = Color.Green;
        }



        public void ZapTabFile()
        {
            string sNameFile, textRow;
            //string sdir = Directory.GetCurrentDirectory();
            string sdir = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
            sNameFile = sdir + @"\FileTabStorage.txt";
            try
            {
                if (!File.Exists(sNameFile))
                {
                    MessageBox.Show("No find file");

                    using (StreamWriter sw = new StreamWriter(sNameFile))
                    {
                        foreach (DataRow rr in TStorage.Rows)
                        {
                            textRow = rr["Група"] + ";" + rr["Назва"] + ";" + rr["Виробник"] + ";" +
                            Convert.ToString(rr["Ціна"]) + ";" + Convert.ToString(rr["Кількість"]);
                            sw.WriteLine(textRow);
                        }
                    }
                }
                else
                {
                    MessageBox.Show("Find file");
                    File.Delete(sNameFile);
                    using (StreamWriter sw = new StreamWriter(sNameFile))
                    {
                        foreach (DataRow rr in TStorage.Rows)
                        {
                            textRow = rr["Група"] + ";" + rr["Назва"] + ";" + rr["Виробник"] + ";" +
                            Convert.ToString(rr["Ціна"]) + ";" + Convert.ToString(rr["Кількість"]);
                            sw.WriteLine(textRow);
                        }
                    }
                }
                MessageBox.Show(sdir);
            }
            catch (Exception e)
            {
                MessageBox.Show("Таблиця не записана");
            }
        }



        public void SetSum(DataGridView DGV)
        {
            string sGroup, sSort;
            decimal DSuma;
            int i;
            DataTable TabStorageSum = new DataTable();
            DataColumn cNameGroupS = new DataColumn("Група");
            DataColumn cCostS = new DataColumn("Вартість");
            cNameGroupS.DataType = System.Type.GetType("System.String");
            cCostS.DataType = System.Type.GetType("System.Decimal");
            TabStorageSum.Columns.Add(cNameGroupS);
            TabStorageSum.Columns.Add(cCostS);
            sSort = StorageView.Sort;
            StorageView.Sort = "Група";
            i = 0;
            while (i < StorageView.Count)
            {
                sGroup = (string)StorageView[i]["Група"];
                DSuma = 0.0M;
                while( (i < StorageView.Count) && (sGroup == (string)StorageView[i]["Група"]))
                {
                    try
                    {
                        DSuma = DSuma + (decimal)StorageView[i]["Вартість"];
                    }
                    catch
                    {
                        StorageView[i]["Вартість"] = 0M;
                    }
                    i = i + 1;
                    if (i == StorageView.Count) break;
                }
                DataRow rowStorageSum = TabStorageSum.NewRow();
                rowStorageSum["Група"] = sGroup;
                rowStorageSum["Вартість"] = DSuma;
                TabStorageSum.Rows.Add(rowStorageSum);
            }
            DGV.DataSource = TabStorageSum;
            StorageView.Sort = Sort;
        }



        public void ReadTabFile(DataGridView DSG)
        {
            string sNameFile, textRow;
            string pGroup, pName, pMaker, sCount, sPrice;
            int pCount;
            decimal pPrice;
            int i, ip;
            TStorage.Rows.Clear();
            //string sdir = Directory.GetCurrentDirectory();
            string sdir = Environment.GetFolderPath(Environment.SpecialFolder.Desktop);
            sNameFile = sdir + @"\FileTabStorage.txt";
            using (StreamReader sr = new StreamReader(sNameFile))
            {
                while (sr.Peek() >= 0)
                {
                    pGroup = ""; pName = ""; pMaker = ""; sPrice = ""; sCount = "";
                    textRow = sr.ReadLine();
                    i = textRow.IndexOf(';') - 1;
                    for (int j = 0; j<=i; j++)
                    {
                        pGroup = pGroup + textRow[j];
                    }
                    ip = i + 2;
                    i = textRow.IndexOf(';', ip) - 1;
                    for (int j = ip; j<= i; j++)
                    {
                        pName = pName + textRow[j];
                    }
                    ip = i + 2;
                    i = textRow.IndexOf(';', ip) - 1;
                    for (int j = ip; j<=i; j++)
                    {
                        pMaker = pMaker + textRow[j];
                    }
                    ip = i + 2;
                    i = textRow.IndexOf(';', ip) - 1;
                    for (int j = ip; j <= i; j++)
                    {
                        sPrice = sPrice + textRow[j];
                    }
                    ip = i + 2;
                    for (int j = ip; j<=textRow.Length - 1; j++)
                    {
                        sCount = sCount + textRow[j];
                    }
                    pCount = Convert.ToInt32(sCount);
                    pPrice = Convert.ToDecimal(sPrice);
                    TabStorageAddRow(pGroup, pName, pMaker, pPrice, pCount);
                }
            }
            SetSum(DSG);
        }

    }



}
