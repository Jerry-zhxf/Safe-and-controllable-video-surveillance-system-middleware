#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "childrenwindow1.h"
#include "childrenwindow2.h"
#include <windows.h>
#include <QTime>
#include <QTimer>


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    connect(ui->pushButton,SIGNAL(clicked(bool)),this,SLOT(pushButton_clicked()));
    connect(ui->pushButton_2,SIGNAL(clicked(bool)),this,SLOT(pushButton1_clicked()));
    connect(ui->pushButton_3,SIGNAL(clicked(bool)),this,SLOT(pushButton2_clicked()));
    connect(ui->pushButton_4,SIGNAL(clicked(bool)),this,SLOT(pushButton3_clicked()));
    w1=NULL;
    w2=NULL;

}

MainWindow::~MainWindow()
{
    delete ui;
}

//生成密钥
void MainWindow::pushButton_clicked(){
        ui->textEdit->setText("正在生成密钥");
        Sleep(5000);
        ui->textEdit->append("生成成功");
}

//解密文件
void MainWindow::pushButton1_clicked(){
    if(w1==NULL){
       w1=new childrenWindow1(NULL);
    }
    w1->show();

}
//发送证书请求
void MainWindow::pushButton2_clicked(){
    if(w2==NULL){
       w2=new ChildrenWindow2(NULL);
    }
    w2->show();
}

//退出
void MainWindow::pushButton3_clicked(){
    this->close();
}

void sleep(unsigned int msec)
{
QTime dieTime = QTime::currentTime().addMSecs(msec);
while( QTime::currentTime() < dieTime )
QCoreApplication::processEvents(QEventLoop::AllEvents, 100);
}
void Delay_MSec(unsigned int msec)
{
    QEventLoop loop;//定义一个新的事件循环
    QTimer::singleShot(msec, &loop, SLOT(quit()));//创建单次定时器，槽函数为事件循环的退出函数
    loop.exec();//事件循环开始执行，程序会卡在这里，直到定时时间到，本循环被退出
}



void MainWindow::sendData1(QString data)
{
    ui->textEdit->setText(data);      //在textEdit中显示传递的数据
    ui->textEdit->append("解密中");
    Delay_MSec(5000);
    ui->textEdit->append("解密成功");
}

void MainWindow::sendData2(QString data)
{
    ui->textEdit->setText(data);      //在textEdit中显示传递的数据
    ui->textEdit->append("发送中");
    Delay_MSec(5000);
    ui->textEdit->append("发送成功");
}
