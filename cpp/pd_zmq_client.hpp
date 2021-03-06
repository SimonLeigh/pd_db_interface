#ifndef PD_ZMQ_CLIENT_H
#define PD_ZMQ_CLIENT_H

#include <zmqpp/zmqpp.hpp>
#include <string>
#include <vector>

class PowerDataConnector {
public:
  PowerDataConnector(const std::string endpoint);
  void connect();
  void receive(std::string &text);
  std::vector<double> receiveToVector();
private:
  std::string host;
  zmqpp::context context;
  zmqpp::socket_type type;
  zmqpp::socket socket;
  double convertToDouble(const std::string &s);
};
  
#endif
