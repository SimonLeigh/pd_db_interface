#include "pd_zmq_client.hpp"
#include <iostream>
#include <sstream>
#include <stdexcept>

/* Constructor
 * Initialises socket as subscribe type. 
*/
PowerDataConnector::PowerDataConnector(const std::string endpoint) : 
  host(endpoint), 
  type(zmqpp::socket_type::subscribe), 
  socket(zmqpp::socket(context,type)) {
  // Set subscription to all messages
  this->socket.set(zmqpp::socket_option::subscribe,"");
}

/* Connect socket to server */
void PowerDataConnector::connect(){
  std::cout << "Opening connection to : " \
            << this->host << "..." << std::endl;
  return this->socket.connect(this->host);

}

/* Receive a string from socket */
void PowerDataConnector::receive(std::string &text){
  this->socket.receive(text);
}

/* Receive from the socket and place into vector */
std::vector<double> PowerDataConnector::receiveToVector(){

  std::string rawText;
  std::vector<double> values;
  char delimiter = ' ';

  /* Receive the raw text in format
   * Time active apparent voltage
   */
  this->socket.receive(rawText);

  /* Split rawText into doubles and insert into vector */
  std::stringstream ss(rawText);
  std::string item;

  /* Iterate stringstream extracting items 
   * The third input to getline is delimiter
   */
  while(std::getline(ss,item, delimiter)){
    values.push_back(convertToDouble(item));
  }
  
  return values;

}

double PowerDataConnector::convertToDouble(const std::string &s){
  std::istringstream i(s);
  double x;
  if (!(i >> x)){
    throw std::runtime_error("Error converting: " + s);
  }
  return x;
}

