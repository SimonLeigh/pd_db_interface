#include "pd_zmq_client.hpp"
#include "pd_db_connector.hpp"
#include <iostream>

int main(){
  
  // Instantiate a zmq connector class
  PowerDataConnector pd = PowerDataConnector("tcp://192.168.1.113:5556");
  PDDBConnector db = PDDBConnector("localhost", "logger", "l0gg3r");

  // Connect to zmq server
  try {
    pd.connect();
  }
  catch(zmqpp::exception &e){
    std::cout << "Exception thrown: " << e.what() << std::endl;
  }

  // Connect to DB
  db.connectAndSetDb("kinetica_power_data");

  // Receive Data
  while(true){

    // Receive text to vector of doubles method
    std::vector<double> dVector = pd.receiveToVector();

    // Add to database
    db.sendUpdate(dVector);
   
  }

  return 0;

}
