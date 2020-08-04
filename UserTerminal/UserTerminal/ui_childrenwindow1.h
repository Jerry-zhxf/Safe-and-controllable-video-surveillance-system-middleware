/********************************************************************************
** Form generated from reading UI file 'childrenwindow1.ui'
**
** Created by: Qt User Interface Compiler version 5.8.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_CHILDRENWINDOW1_H
#define UI_CHILDRENWINDOW1_H

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

class Ui_childrenWindow1
{
public:
    QWidget *centralwidget;
    QLabel *label;
    QLineEdit *lineEdit;
    QLabel *label_2;
    QLabel *label_3;
    QLineEdit *lineEdit_2;
    QPushButton *pushButton_3;
    QToolButton *toolButton;
    QToolButton *toolButton_2;

    void setupUi(QMainWindow *childrenWindow1)
    {
        if (childrenWindow1->objectName().isEmpty())
            childrenWindow1->setObjectName(QStringLiteral("childrenWindow1"));
        childrenWindow1->resize(800, 404);
        childrenWindow1->setStyleSheet(QString::fromUtf8("font: 9pt \"\345\276\256\350\275\257\351\233\205\351\273\221\";"));
        centralwidget = new QWidget(childrenWindow1);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        label = new QLabel(centralwidget);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(90, 110, 221, 21));
        lineEdit = new QLineEdit(centralwidget);
        lineEdit->setObjectName(QStringLiteral("lineEdit"));
        lineEdit->setGeometry(QRect(350, 100, 301, 41));
        label_2 = new QLabel(centralwidget);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(90, 210, 221, 21));
        label_3 = new QLabel(centralwidget);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(340, 40, 101, 31));
        lineEdit_2 = new QLineEdit(centralwidget);
        lineEdit_2->setObjectName(QStringLiteral("lineEdit_2"));
        lineEdit_2->setGeometry(QRect(350, 200, 301, 41));
        pushButton_3 = new QPushButton(centralwidget);
        pushButton_3->setObjectName(QStringLiteral("pushButton_3"));
        pushButton_3->setGeometry(QRect(320, 310, 131, 40));
        toolButton = new QToolButton(centralwidget);
        toolButton->setObjectName(QStringLiteral("toolButton"));
        toolButton->setGeometry(QRect(680, 110, 62, 27));
        toolButton_2 = new QToolButton(centralwidget);
        toolButton_2->setObjectName(QStringLiteral("toolButton_2"));
        toolButton_2->setGeometry(QRect(680, 210, 62, 27));
        childrenWindow1->setCentralWidget(centralwidget);

        retranslateUi(childrenWindow1);

        QMetaObject::connectSlotsByName(childrenWindow1);
    } // setupUi

    void retranslateUi(QMainWindow *childrenWindow1)
    {
        childrenWindow1->setWindowTitle(QApplication::translate("childrenWindow1", "MainWindow", Q_NULLPTR));
        label->setText(QApplication::translate("childrenWindow1", "\350\257\267\350\276\223\345\205\245\344\273\243\350\247\243\345\257\206\347\232\204\346\226\207\344\273\266\345\220\215", Q_NULLPTR));
        label_2->setText(QApplication::translate("childrenWindow1", "\350\257\267\350\276\223\345\205\245\350\247\243\345\257\206\345\257\206\351\222\245\346\226\207\344\273\266\345\220\215", Q_NULLPTR));
        label_3->setText(QApplication::translate("childrenWindow1", "\350\247\243\345\257\206\346\226\207\344\273\266", Q_NULLPTR));
        pushButton_3->setText(QApplication::translate("childrenWindow1", "\347\241\256\345\256\232", Q_NULLPTR));
        toolButton->setText(QApplication::translate("childrenWindow1", "...", Q_NULLPTR));
        toolButton_2->setText(QApplication::translate("childrenWindow1", "...", Q_NULLPTR));
    } // retranslateUi

};

namespace Ui {
    class childrenWindow1: public Ui_childrenWindow1 {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_CHILDRENWINDOW1_H
