#ifndef PD_MYSQL_CLIENT_H
#define PD_MYSQL_CLIENT_H

/*
  Include directly the different
  headers from cppconn/ and mysql_driver.h + mysql_util.h
  (and mysql_connection.h). This will reduce your build time!
*/
#include "mysql_connection.h"
#include "mysql_driver.h"

#include <cppconn/driver.h>
#include <cppconn/exception.h>
#include <cppconn/resultset.h>
#include <cppconn/statement.h>
#include <cppconn/prepared_statement.h>

/* Standard C++ includes */
#include <string>
#include <vector>

#define STATEMENT "INSERT into scpm_measurements(unix_time,active_power,apparent_power,voltage) VALUES (?, ?, ?, ?)"
#define CONNECT_FAILURE -1
#define CONNECT_SUCCESS 1

class PDDBConnector {
public:
  PDDBConnector(const std::string &url, const std::string &user, const std::string &pass);
  int connectAndSetDb(const std::string &database);
  int sendUpdate(std::vector<double> &values);
private:
  const std::string url;
  const std::string user;
  const std::string pass;
  sql::Driver * driver;
  std::shared_ptr< sql::Connection > con;
  std::shared_ptr< sql::PreparedStatement > pStmt;
};

#endif

