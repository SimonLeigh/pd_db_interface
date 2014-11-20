#include "pd_zmq_client.hpp"
#include <iostream>

int main(){

  std::cout.precision(14);
  
  PowerDataConnector pd = PowerDataConnector("tcp://192.168.1.113:5556");
  
  try {
    pd.connect();
  }
  catch(zmqpp::exception &e){
    std::cout << "Exception thrown: " << e.what() << std::endl;
  }
    
  
  std::string text;
  while(true){
    std::cout << "Testing receive(text) method: " << std::endl;
    pd.receive(text);
    std::cout << "Received: " << text << std::endl;

    std::cout << "Testing receiveToVector() method: " << std::endl;
    std::vector<double> dVector = pd.receiveToVector();
    
    for (std::vector<double>::const_iterator i = dVector.begin(); i != dVector.end(); ++i){
      std::cout << *i << '\n';
    }

  }
  return 0;

}
