namespace lab11_demo
{
    partial class FormFilterAndSort
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
            this.BtnFilterAndSearch = new System.Windows.Forms.Button();
            this.TBFilterAndSearch = new System.Windows.Forms.TextBox();
            this.SuspendLayout();
            // 
            // BtnFilterAndSearch
            // 
            this.BtnFilterAndSearch.Location = new System.Drawing.Point(144, 38);
            this.BtnFilterAndSearch.Name = "BtnFilterAndSearch";
            this.BtnFilterAndSearch.Size = new System.Drawing.Size(106, 23);
            this.BtnFilterAndSearch.TabIndex = 0;
            this.BtnFilterAndSearch.Text = "Enter";
            this.BtnFilterAndSearch.UseVisualStyleBackColor = true;
            this.BtnFilterAndSearch.Click += new System.EventHandler(this.BtnFilterAndSearch_Click);
            // 
            // TBFilterAndSearch
            // 
            this.TBFilterAndSearch.Location = new System.Drawing.Point(43, 12);
            this.TBFilterAndSearch.Name = "TBFilterAndSearch";
            this.TBFilterAndSearch.Size = new System.Drawing.Size(309, 20);
            this.TBFilterAndSearch.TabIndex = 1;
            // 
            // FormFilterAndSort
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(396, 69);
            this.Controls.Add(this.TBFilterAndSearch);
            this.Controls.Add(this.BtnFilterAndSearch);
            this.Name = "FormFilterAndSort";
            this.Text = "FormFilterAndSort";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button BtnFilterAndSearch;
        private System.Windows.Forms.TextBox TBFilterAndSearch;
    }
}