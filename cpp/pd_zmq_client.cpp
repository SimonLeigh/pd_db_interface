#include "pd_zmq_client.hpp"
#include <iostream>

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
  std::cout << "Opening connection to : " << this->host << "..." << std::endl;
  return this->socket.connect(this->host);

}

/* Receive a string from socket */
void PowerDataConnector::receive(std::string &text){
  this->socket.receive(text);
}

