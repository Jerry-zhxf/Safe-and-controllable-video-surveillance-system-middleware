#include "mybusiness.h"
#include <QDebug>
#include <QThread>

MyBusiness::MyBusiness(QObject *parent) : QObject(parent)
{

}

QStringList MyBusiness::getFileList(QString address)
{
    qDebug() << "MyBusiness getFileList Thread" << QThread::currentThreadId();

    QStringList result;

    //查询数据库获取数据
    for(int i = 0; i < 10;i++)
    {
       result.insert(i,QString::number(i)+ ".txt");

       QThread::sleep(1);
    }

    //发送获取的数据
    emit fileListResult(result);

    return result;
}
