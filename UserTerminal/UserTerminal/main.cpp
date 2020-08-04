#include "mainwindow.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    w.setWindowTitle("用户终端");//设置窗体标题
    w.show();
    QIcon *ico = new QIcon(":/logo/favicon_64x64.ico");
    a.setWindowIcon(*ico);

    return a.exec();
}
