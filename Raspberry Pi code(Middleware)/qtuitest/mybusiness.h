#ifndef MYBUSINESS_H
#define MYBUSINESS_H

#include <QObject>

class MyBusiness : public QObject
{
    Q_OBJECT
public:
    explicit MyBusiness(QObject *parent = 0);

    QStringList getFileList(QString address);

signals:
    void fileListResult(QStringList result);

public slots:
};

#endif // MYBUSINESS_H
