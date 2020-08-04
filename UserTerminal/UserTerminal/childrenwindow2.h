#ifndef CHILDRENWINDOW2_H
#define CHILDRENWINDOW2_H

#include <QMainWindow>

namespace Ui {
class ChildrenWindow2;
}

class ChildrenWindow2 : public QMainWindow
{
    Q_OBJECT

public:
    explicit ChildrenWindow2(QWidget *parent = 0);
    ~ChildrenWindow2();

private slots:
    void open3();
    void open4();
    void pushButton_clicked();

private:
    Ui::ChildrenWindow2 *ui;
};

#endif // CHILDRENWINDOW2_H
