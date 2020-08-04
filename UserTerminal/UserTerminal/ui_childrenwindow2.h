/********************************************************************************
** Form generated from reading UI file 'childrenwindow2.ui'
**
** Created by: Qt User Interface Compiler version 5.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CHILDRENWINDOW2_H
#define UI_CHILDRENWINDOW2_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QToolButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_ChildrenWindow2
{
public:
    QWidget *centralwidget;
    QLabel *label;
    QLabel *label_2;
    QLineEdit *lineEdit;
    QLabel *label_3;
    QLineEdit *lineEdit_2;
    QPushButton *pushButton_3;
    QToolButton *toolButton;
    QToolButton *toolButton_2;

    void setupUi(QMainWindow *ChildrenWindow2)
    {
        if (ChildrenWindow2->objectName().isEmpty())
            ChildrenWindow2->setObjectName(QStringLiteral("ChildrenWindow2"));
        ChildrenWindow2->resize(768, 371);
        ChildrenWindow2->setStyleSheet(QString::fromUtf8("font: 9pt \"\345\276\256\350\275\257\351\233\205\351\273\221\";"));
        centralwidget = new QWidget(ChildrenWindow2);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        label = new QLabel(centralwidget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(80, 100, 201, 21));
        label_2 = new QLabel(centralwidget);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(320, 20, 141, 41));
        lineEdit = new QLineEdit(centralwidget);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));
        lineEdit->setGeometry(QRect(300, 90, 291, 41));
        label_3 = new QLabel(centralwidget);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(80, 180, 201, 21));
        lineEdit_2 = new QLineEdit(centralwidget);
        lineEdit_2->setObjectName(QStringLiteral("lineEdit_2"));
        lineEdit_2->setGeometry(QRect(300, 170, 291, 41));
        pushButton_3 = new QPushButton(centralwidget);
        pushButton_3->setObjectName(QStringLiteral("pushButton_3"));
        pushButton_3->setGeometry(QRect(320, 270, 131, 40));
        toolButton = new QToolButton(centralwidget);
        toolButton->setObjectName(QStringLiteral("toolButton"));
        toolButton->setGeometry(QRect(620, 100, 62, 27));
        toolButton_2 = new QToolButton(centralwidget);
        toolButton_2->setObjectName(QStringLiteral("toolButton_2"));
        toolButton_2->setGeometry(QRect(620, 180, 62, 27));
        ChildrenWindow2->setCentralWidget(centralwidget);

        retranslateUi(ChildrenWindow2);

        QMetaObject::connectSlotsByName(ChildrenWindow2);
    } // setupUi

    void retranslateUi(QMainWindow *ChildrenWindow2)
    {
        ChildrenWindow2->setWindowTitle(QApplication::translate("ChildrenWindow2", "MainWindow", Q_NULLPTR));
        label->setText(QApplication::translate("ChildrenWindow2", "\350\257\267\350\276\223\345\205\245\345\257\206\351\222\245\346\226\207\344\273\266\350\267\257\345\276\204", Q_NULLPTR));
        label_2->setText(QApplication::translate("ChildrenWindow2", "\345\217\221\351\200\201\350\257\201\344\271\246\350\257\267\346\261\202", Q_NULLPTR));
        label_3->setText(QApplication::translate("ChildrenWindow2", "\350\257\267\350\276\223\345\205\245CA\344\270\255\345\277\203\345\234\260\345\235\200", Q_NULLPTR));
        pushButton_3->setText(QApplication::translate("ChildrenWindow2", "\347\241\256\345\256\232", Q_NULLPTR));
        toolButton->setText(QApplication::translate("ChildrenWindow2", "...", Q_NULLPTR));
        toolButton_2->setText(QApplication::translate("ChildrenWindow2", "...", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class ChildrenWindow2: public Ui_ChildrenWindow2 {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CHILDRENWINDOW2_H
