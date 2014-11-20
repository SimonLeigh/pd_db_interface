#include "pd_db_connector.hpp"

PDDBConnector::PDDBConnector(const std::string &url, 
                                const std::string &user, 
                                const std::string &pass) : 
  url(url), user(user), pass(pass), driver( sql::mysql::get_driver_instance() ) {}

int PDDBConnector::connectAndSetDb(const std::string &database){
  try {
    // Connect
    this->con.reset(this->driver->connect(this->url,this->user,this->pass));
    // Set DB
    this->con->setSchema(database);
    // Set statement
    this->pStmt.reset(this->con->prepareStatement(STATEMENT));
  }
  catch (sql::SQLException &e){
    std::cout << "# ERR: SQLException in " << __FILE__;
    std::cout << "(" << __FUNCTION__ << ") on line " << __LINE__ << std::endl;
    /* Use what() (derived from std::runtime_error) to fetch the error message */
    std::cout << "# ERR: " << e.what();
    std::cout << " (MySQL error code: " << e.getErrorCode();
    std::cout << ", SQLState: " << e.getSQLState() << " )" << std::endl;

    return CONNECT_FAILURE;
  }
  
  return CONNECT_SUCCESS;
}

int PDDBConnector::sendUpdate(std::vector<double> &values){

  /* Iterate vector and set pStmt values */
  for(unsigned int i=0; i < values.size(); i++){
    this->pStmt->setDouble(i+1, values[i]);
  }

  /* Commit to DB */
  try {
    this->pStmt->execute();
  }
  catch (sql::SQLException &e){
    std::cout << "# ERR: SQLException in " << __FILE__;
    std::cout << "(" << __FUNCTION__ << ") on line " << __LINE__ << std::endl;
    /* Use what() (derived from std::runtime_error) to fetch the error message */
    std::cout << "# ERR: " << e.what();
    std::cout << " (MySQL error code: " << e.getErrorCode();
    std::cout << ", SQLState: " << e.getSQLState() << " )" << std::endl;
    return CONNECT_FAILURE;
  }

  return CONNECT_SUCCESS;
}
