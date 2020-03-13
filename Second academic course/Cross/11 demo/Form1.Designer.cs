namespace lab11_demo
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.splitContainer1 = new System.Windows.Forms.SplitContainer();
            this.DGStorage = new System.Windows.Forms.DataGridView();
            this.panel1 = new System.Windows.Forms.Panel();
            this.buttonAddRowToTable = new System.Windows.Forms.Button();
            this.label6 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.tbCount = new System.Windows.Forms.TextBox();
            this.tbPrice = new System.Windows.Forms.TextBox();
            this.tbMaker = new System.Windows.Forms.TextBox();
            this.tbName = new System.Windows.Forms.TextBox();
            this.tbGroup = new System.Windows.Forms.TextBox();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.файлToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.записатиToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.зчитатиToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.фільтрToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.встановитиФільтрToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.знятиФільтрToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.сортуванняToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.встановитиСортуванняToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.знятиСортуванняToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.сортуванняПоГРУПІToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.пошукToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.пошукПоНазвіToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.DGStorageSum = new System.Windows.Forms.DataGridView();
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).BeginInit();
            this.splitContainer1.Panel1.SuspendLayout();
            this.splitContainer1.Panel2.SuspendLayout();
            this.splitContainer1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.DGStorage)).BeginInit();
            this.panel1.SuspendLayout();
            this.menuStrip1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.DGStorageSum)).BeginInit();
            this.SuspendLayout();
            // 
            // splitContainer1
            // 
            this.splitContainer1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.splitContainer1.Location = new System.Drawing.Point(0, 0);
            this.splitContainer1.Name = "splitContainer1";
            this.splitContainer1.Orientation = System.Windows.Forms.Orientation.Horizontal;
            // 
            // splitContainer1.Panel1
            // 
            this.splitContainer1.Panel1.Controls.Add(this.DGStorage);
            this.splitContainer1.Panel1.Controls.Add(this.panel1);
            // 
            // splitContainer1.Panel2
            // 
            this.splitContainer1.Panel2.Controls.Add(this.DGStorageSum);
            this.splitContainer1.Size = new System.Drawing.Size(800, 450);
            this.splitContainer1.SplitterDistance = 275;
            this.splitContainer1.TabIndex = 0;
            // 
            // DGStorage
            // 
            this.DGStorage.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.DGStorage.Location = new System.Drawing.Point(3, 109);
            this.DGStorage.Name = "DGStorage";
            this.DGStorage.ReadOnly = true;
            this.DGStorage.Size = new System.Drawing.Size(794, 163);
            this.DGStorage.TabIndex = 1;
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.buttonAddRowToTable);
            this.panel1.Controls.Add(this.label6);
            this.panel1.Controls.Add(this.label5);
            this.panel1.Controls.Add(this.label4);
            this.panel1.Controls.Add(this.label3);
            this.panel1.Controls.Add(this.label2);
            this.panel1.Controls.Add(this.label1);
            this.panel1.Controls.Add(this.tbCount);
            this.panel1.Controls.Add(this.tbPrice);
            this.panel1.Controls.Add(this.tbMaker);
            this.panel1.Controls.Add(this.tbName);
            this.panel1.Controls.Add(this.tbGroup);
            this.panel1.Controls.Add(this.menuStrip1);
            this.panel1.Location = new System.Drawing.Point(3, 3);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(794, 103);
            this.panel1.TabIndex = 0;
            // 
            // buttonAddRowToTable
            // 
            this.buttonAddRowToTable.Location = new System.Drawing.Point(644, 38);
            this.buttonAddRowToTable.Name = "buttonAddRowToTable";
            this.buttonAddRowToTable.Size = new System.Drawing.Size(112, 38);
            this.buttonAddRowToTable.TabIndex = 11;
            this.buttonAddRowToTable.Text = "Додати рядок до таблиці";
            this.buttonAddRowToTable.UseVisualStyleBackColor = true;
            this.buttonAddRowToTable.Click += new System.EventHandler(this.buttonAddRowToTable_Click);
            // 
            // label6
            // 
            this.label6.AutoSize = true;
            this.label6.Location = new System.Drawing.Point(508, 51);
            this.label6.Name = "label6";
            this.label6.Size = new System.Drawing.Size(53, 13);
            this.label6.TabIndex = 10;
            this.label6.Text = "Кількість";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(395, 51);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(29, 13);
            this.label5.TabIndex = 9;
            this.label5.Text = "Ціна";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(273, 51);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(56, 13);
            this.label4.TabIndex = 8;
            this.label4.Text = "Виробник";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(162, 51);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(39, 13);
            this.label3.TabIndex = 7;
            this.label3.Text = "Назва";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(46, 51);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(36, 13);
            this.label2.TabIndex = 6;
            this.label2.Text = "Група";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(217, 28);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(123, 13);
            this.label1.TabIndex = 5;
            this.label1.Text = "Введіть дані в таблицю";
            // 
            // tbCount
            // 
            this.tbCount.Location = new System.Drawing.Point(477, 80);
            this.tbCount.Name = "tbCount";
            this.tbCount.Size = new System.Drawing.Size(111, 20);
            this.tbCount.TabIndex = 4;
            // 
            // tbPrice
            // 
            this.tbPrice.Location = new System.Drawing.Point(360, 80);
            this.tbPrice.Name = "tbPrice";
            this.tbPrice.Size = new System.Drawing.Size(111, 20);
            this.tbPrice.TabIndex = 3;
            // 
            // tbMaker
            // 
            this.tbMaker.Location = new System.Drawing.Point(243, 80);
            this.tbMaker.Name = "tbMaker";
            this.tbMaker.Size = new System.Drawing.Size(111, 20);
            this.tbMaker.TabIndex = 2;
            // 
            // tbName
            // 
            this.tbName.Location = new System.Drawing.Point(126, 80);
            this.tbName.Name = "tbName";
            this.tbName.Size = new System.Drawing.Size(111, 20);
            this.tbName.TabIndex = 1;
            // 
            // tbGroup
            // 
            this.tbGroup.Location = new System.Drawing.Point(9, 80);
            this.tbGroup.Name = "tbGroup";
            this.tbGroup.Size = new System.Drawing.Size(111, 20);
            this.tbGroup.TabIndex = 0;
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.файлToolStripMenuItem,
            this.фільтрToolStripMenuItem,
            this.сортуванняToolStripMenuItem,
            this.пошукToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(794, 24);
            this.menuStrip1.TabIndex = 12;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // файлToolStripMenuItem
            // 
            this.файлToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.записатиToolStripMenuItem,
            this.зчитатиToolStripMenuItem});
            this.файлToolStripMenuItem.Name = "файлToolStripMenuItem";
            this.файлToolStripMenuItem.Size = new System.Drawing.Size(48, 20);
            this.файлToolStripMenuItem.Text = "Файл";
            // 
            // записатиToolStripMenuItem
            // 
            this.записатиToolStripMenuItem.Name = "записатиToolStripMenuItem";
            this.записатиToolStripMenuItem.Size = new System.Drawing.Size(125, 22);
            this.записатиToolStripMenuItem.Text = "Записати";
            this.записатиToolStripMenuItem.Click += new System.EventHandler(this.записатиToolStripMenuItem_Click);
            // 
            // зчитатиToolStripMenuItem
            // 
            this.зчитатиToolStripMenuItem.Name = "зчитатиToolStripMenuItem";
            this.зчитатиToolStripMenuItem.Size = new System.Drawing.Size(125, 22);
            this.зчитатиToolStripMenuItem.Text = "Зчитати";
            this.зчитатиToolStripMenuItem.Click += new System.EventHandler(this.зчитатиToolStripMenuItem_Click);
            // 
            // фільтрToolStripMenuItem
            // 
            this.фільтрToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.встановитиФільтрToolStripMenuItem,
            this.знятиФільтрToolStripMenuItem});
            this.фільтрToolStripMenuItem.Name = "фільтрToolStripMenuItem";
            this.фільтрToolStripMenuItem.Size = new System.Drawing.Size(56, 20);
            this.фільтрToolStripMenuItem.Text = "Фільтр";
            // 
            // встановитиФільтрToolStripMenuItem
            // 
            this.встановитиФільтрToolStripMenuItem.Name = "встановитиФільтрToolStripMenuItem";
            this.встановитиФільтрToolStripMenuItem.Size = new System.Drawing.Size(177, 22);
            this.встановитиФільтрToolStripMenuItem.Text = "Встановити фільтр";
            this.встановитиФільтрToolStripMenuItem.Click += new System.EventHandler(this.встановитиФільтрToolStripMenuItem_Click);
            // 
            // знятиФільтрToolStripMenuItem
            // 
            this.знятиФільтрToolStripMenuItem.Name = "знятиФільтрToolStripMenuItem";
            this.знятиФільтрToolStripMenuItem.Size = new System.Drawing.Size(177, 22);
            this.знятиФільтрToolStripMenuItem.Text = "Зняти фільтр";
            this.знятиФільтрToolStripMenuItem.Click += new System.EventHandler(this.знятиФільтрToolStripMenuItem_Click);
            // 
            // сортуванняToolStripMenuItem
            // 
            this.сортуванняToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.встановитиСортуванняToolStripMenuItem,
            this.знятиСортуванняToolStripMenuItem,
            this.сортуванняПоГРУПІToolStripMenuItem});
            this.сортуванняToolStripMenuItem.Name = "сортуванняToolStripMenuItem";
            this.сортуванняToolStripMenuItem.Size = new System.Drawing.Size(84, 20);
            this.сортуванняToolStripMenuItem.Text = "Сортування";
            // 
            // встановитиСортуванняToolStripMenuItem
            // 
            this.встановитиСортуванняToolStripMenuItem.Name = "встановитиСортуванняToolStripMenuItem";
            this.встановитиСортуванняToolStripMenuItem.Size = new System.Drawing.Size(203, 22);
            this.встановитиСортуванняToolStripMenuItem.Text = "Встановити сортування";
            this.встановитиСортуванняToolStripMenuItem.Click += new System.EventHandler(this.встановитиСортуванняToolStripMenuItem_Click);
            // 
            // знятиСортуванняToolStripMenuItem
            // 
            this.знятиСортуванняToolStripMenuItem.Name = "знятиСортуванняToolStripMenuItem";
            this.знятиСортуванняToolStripMenuItem.Size = new System.Drawing.Size(203, 22);
            this.знятиСортуванняToolStripMenuItem.Text = "Зняти сортування";
            this.знятиСортуванняToolStripMenuItem.Click += new System.EventHandler(this.знятиСортуванняToolStripMenuItem_Click);
            // 
            // сортуванняПоГРУПІToolStripMenuItem
            // 
            this.сортуванняПоГРУПІToolStripMenuItem.Name = "сортуванняПоГРУПІToolStripMenuItem";
            this.сортуванняПоГРУПІToolStripMenuItem.Size = new System.Drawing.Size(203, 22);
            this.сортуванняПоГРУПІToolStripMenuItem.Text = "Сортування по ГРУПІ";
            this.сортуванняПоГРУПІToolStripMenuItem.Click += new System.EventHandler(this.сортуванняПоГРУПІToolStripMenuItem_Click);
            // 
            // пошукToolStripMenuItem
            // 
            this.пошукToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.пошукПоНазвіToolStripMenuItem});
            this.пошукToolStripMenuItem.Name = "пошукToolStripMenuItem";
            this.пошукToolStripMenuItem.Size = new System.Drawing.Size(58, 20);
            this.пошукToolStripMenuItem.Text = "Пошук";
            // 
            // пошукПоНазвіToolStripMenuItem
            // 
            this.пошукПоНазвіToolStripMenuItem.Name = "пошукПоНазвіToolStripMenuItem";
            this.пошукПоНазвіToolStripMenuItem.Size = new System.Drawing.Size(167, 22);
            this.пошукПоНазвіToolStripMenuItem.Text = "Пошук по НАЗВІ";
            this.пошукПоНазвіToolStripMenuItem.Click += new System.EventHandler(this.пошукПоНазвіToolStripMenuItem_Click);
            // 
            // DGStorageSum
            // 
            this.DGStorageSum.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.DGStorageSum.Location = new System.Drawing.Point(3, 3);
            this.DGStorageSum.Name = "DGStorageSum";
            this.DGStorageSum.ReadOnly = true;
            this.DGStorageSum.Size = new System.Drawing.Size(794, 165);
            this.DGStorageSum.TabIndex = 0;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Control;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.splitContainer1);
            this.MainMenuStrip = this.menuStrip1;
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.splitContainer1.Panel1.ResumeLayout(false);
            this.splitContainer1.Panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.splitContainer1)).EndInit();
            this.splitContainer1.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.DGStorage)).EndInit();
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.DGStorageSum)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.SplitContainer splitContainer1;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Button buttonAddRowToTable;
        private System.Windows.Forms.Label label6;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox tbCount;
        private System.Windows.Forms.TextBox tbPrice;
        private System.Windows.Forms.TextBox tbMaker;
        private System.Windows.Forms.TextBox tbName;
        private System.Windows.Forms.TextBox tbGroup;
        private System.Windows.Forms.DataGridView DGStorage;
        private System.Windows.Forms.DataGridView DGStorageSum;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem файлToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem записатиToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem зчитатиToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem фільтрToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem встановитиФільтрToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem знятиФільтрToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem сортуванняToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem пошукToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem пошукПоНазвіToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem встановитиСортуванняToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem знятиСортуванняToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem сортуванняПоГРУПІToolStripMenuItem;
    }
}

