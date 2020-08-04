#include "mythread.h"
#include <QDebug>
#include <QMutex>

MyThread::MyThread()
{
    isStop = false;
}

void MyThread::closeThread()
{
    isStop = true;
}

void MyThread::run()
{

}
