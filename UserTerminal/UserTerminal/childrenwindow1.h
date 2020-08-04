#ifndef CHILDRENWINDOW1_H
#define CHILDRENWINDOW1_H

#include <QMainWindow>

namespace Ui {
class childrenWindow1;
}

class childrenWindow1 : public QMainWindow
{
    Q_OBJECT

public:
    explicit childrenWindow1(QWidget *parent = 0);
    ~childrenWindow1();


private slots:
    void open1();
    void open2();
    void pushButton_clicked();


private:
    Ui::childrenWindow1 *ui;
};

#endif // CHILDRENWINDOW1_H
