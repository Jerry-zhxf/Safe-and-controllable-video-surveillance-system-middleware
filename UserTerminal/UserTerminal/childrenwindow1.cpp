#include "mainwindow.h"
#include "childrenwindow1.h"
#include "ui_childrenwindow1.h"
#include <QFileDialog>

childrenWindow1::childrenWindow1(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::childrenWindow1)
{
    ui->setupUi(this);
    connect(ui->toolButton,SIGNAL(clicked(bool)),this,SLOT(open1()));
    connect(ui->toolButton_2,SIGNAL(clicked(bool)),this,SLOT(open2()));
    connect(ui->pushButton_3,SIGNAL(clicked(bool)),this,SLOT(pushButton_clicked()));
}

childrenWindow1::~childrenWindow1()
{
    delete ui;
}

void childrenWindow1::open1(){
    QString fileName = QFileDialog::getOpenFileName(this,
                                                    tr("Open"), ".",
                                                    tr("txt files (*)"));
    if (!fileName.isEmpty())
        ui->lineEdit->setText(fileName);
}
void childrenWindow1::open2(){
    QString fileName = QFileDialog::getOpenFileName(this,
                                                    tr("Open"), ".",
                                                    tr("txt files (*)"));
    if (!fileName.isEmpty())
        ui->lineEdit_2->setText(fileName);
}
void childrenWindow1::pushButton_clicked(){
    MainWindow *w = new MainWindow;
    w->sendData1(ui->lineEdit->text()+"\n"+ui->lineEdit_2->text());    //直接调用public函数将本页面中lineEdit的数据传递过去
    w->show();
}
