#include "pd_zmq_client.hpp"
#include <iostream>

int main(){
  
  PowerDataConnector pd = PowerDataConnector("tcp://192.168.1.113:5556");
  
  try {
    pd.connect();
  }
  catch(zmqpp::exception &e){
    std::cout << "Exception thrown: " << e.what() << std::endl;
  }
    
  
  std::string text;
  while(true){
    pd.receive(text);
    std::cout << "Received: " << text << std::endl;
  }
  return 0;

}
