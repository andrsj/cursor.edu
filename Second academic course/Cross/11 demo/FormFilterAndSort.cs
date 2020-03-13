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
    public partial class FormFilterAndSort : Form
    {
        public FormFilterAndSort()
        {
            InitializeComponent();
        }

        private void BtnFilterAndSearch_Click(object sender, EventArgs e)
        {
            Form1.GlobalStringParametr = TBFilterAndSearch.Text;
            Close();
        }
    }
}
