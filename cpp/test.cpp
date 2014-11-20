#include "pd_zmq_client.hpp"
#include "pd_db_connector.hpp"
#include <iostream>

int main(){

  // Set precision of cout stream
  std::cout.precision(14);
  
  // Instantiate a zmq connector class
  PowerDataConnector pd = PowerDataConnector("tcp://192.168.1.113:5556");
  PDDBConnector dbConn = PDDBConnector("localhost", "logger", "l0gg3r");

  // Connect to server
  try {
    pd.connect();
  }
  catch(zmqpp::exception &e){
    std::cout << "Exception thrown: " << e.what() << std::endl;
  }
    
  
  std::string text;

  // Test Receive methods
  while(true){

    // Plain text receive from socket
    std::cout << "Testing receive(text) method: " << std::endl;
    pd.receive(text);
    std::cout << "Received: " << text << std::endl;

    // Receive text to vector of doubles method
    std::cout << "Testing receiveToVector() method: " << std::endl;
    std::vector<double> dVector = pd.receiveToVector();
    
    // Have to iterate the vector to print it in c++
    for (std::vector<double>::const_iterator i = dVector.begin(); i != dVector.end(); ++i){
      std::cout << *i << '\n';
    }

  }

  return 0;

}
