#include <zmqpp/zmqpp.hpp>
//#include <zmqpp/socket_types.hpp>
#include <string>
#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
  const string endpoint = "tcp://192.168.1.113:5556";

  // initialize the 0MQ context
  zmqpp::context context;

  // generate a push socket
  zmqpp::socket_type type = zmqpp::socket_type::subscribe;
  zmqpp::socket socket (context, type);
  zmqpp::socket_option option = zmqpp::socket_option::subscribe;

  socket.set(option, "");
  // open the connection
  cout << "Opening connection to " << endpoint << "..." << endl;
  socket.connect(endpoint);

  // send a message
  cout << "Sending text and a number..." << endl;
  zmqpp::message message;
  string text;
  // compose a message from a string and a number

  while(true){
    socket.receive(text);
  
    cout << "Received message : " << text << endl;
  }

}
