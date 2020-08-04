#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QStringListModel>
#include <QDebug>


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    //前台接收数据并展示
    connect(&m_myBusiness,&MyBusiness::fileListResult,this,&MainWindow::updateFileListUI);
}

MainWindow::~MainWindow()
{
    delete ui;
}

QStringList MainWindow::getFileList(QString address)
{
    return m_myBusiness.getFileList(address);
}

void MainWindow::updateFileListUI(QStringList result)
{
    QStringListModel * model = new QStringListModel(this);

    model->setStringList(result);

    ui->listView->setModel(model);
}

void MainWindow::on_pushButton_clicked()
{
    qDebug() << "MainWindow on_pushButton_clicked Thread" <<QThread::currentThreadId();

    QtConcurrent::run(this,&MainWindow::getFileList,QString("E:\\"));
}

void MainWindow::on_pushButtonSync_clicked()
{
    qDebug() << "MainWindow on_pushButtonSync_clicked Thread" <<QThread::currentThreadId();

    QStringList result;

    //查询数据库获取数据
    for(int i = 0; i < 10;i++)
    {
       result.insert(i,QString::number(i)+ ".txt");

       QThread::sleep(1);
    }

    QStringListModel * model = new QStringListModel(this);

    model->setStringList(result);

    ui->listView->setModel(model);
}
