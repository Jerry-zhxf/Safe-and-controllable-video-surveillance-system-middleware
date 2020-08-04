#include "mainwindow.h"
#include "childrenwindow2.h"
#include "ui_childrenwindow2.h"
#include <QFileDialog>

ChildrenWindow2::ChildrenWindow2(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::ChildrenWindow2)
{
    ui->setupUi(this);
    connect(ui->toolButton,SIGNAL(clicked(bool)),this,SLOT(open3()));
    connect(ui->toolButton_2,SIGNAL(clicked(bool)),this,SLOT(open4()));
}

ChildrenWindow2::~ChildrenWindow2()
{
    delete ui;
}

void ChildrenWindow2::open3(){
    QString fileName = QFileDialog::getOpenFileName(this,
                                                    tr("Open"), ".",
                                                    tr("txt files (*)"));
    if (!fileName.isEmpty())
        ui->lineEdit->setText(fileName);
}
void ChildrenWindow2::open4(){
    QString fileName = QFileDialog::getOpenFileName(this,
                                                    tr("Open"), ".",
                                                    tr("txt files (*)"));
    if (!fileName.isEmpty())
        ui->lineEdit_2->setText(fileName);
}

void ChildrenWindow2::pushButton_clicked(){
    MainWindow *w = new MainWindow;
    w->sendData2(ui->lineEdit->text()+"\n"+ui->lineEdit_2->text());    //直接调用public函数将本页面中lineEdit的数据传递过去
    w->show();
}
