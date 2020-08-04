#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "childrenwindow1.h"
#include "childrenwindow2.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();


public:
    void sendData1(QString data);    //在子窗口创建public函数用来获取传递的数据
    void sendData2(QString data);

private slots:
    void pushButton_clicked();
    void pushButton1_clicked();
    void pushButton2_clicked();
    void pushButton3_clicked();


private:
    Ui::MainWindow *ui;
    childrenWindow1 *w1;
    ChildrenWindow2 *w2;
};

#endif // MAINWINDOW_H
