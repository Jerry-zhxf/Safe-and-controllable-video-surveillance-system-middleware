#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "mybusiness.h"
#include <QtConcurrent>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

    QStringList getFileList(QString address);

    void updateFileListUI(QStringList result);

private slots:
    void on_pushButton_clicked();

    void on_pushButtonSync_clicked();

private:
    Ui::MainWindow *ui;

    MyBusiness m_myBusiness;
};

#endif // MAINWINDOW_H
