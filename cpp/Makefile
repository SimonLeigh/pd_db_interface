CXXFLAGS=-O0 -g -std=c++11 -Wall -Bdynamic
LDLIBS=-lzmqpp -lzmq -lmysqlcppconn

zmq_client:	
	g++ $(CXXFLAGS) zmq_client.cpp -o zmq_client $(LDLIBS)

mysqlclient:
	g++ $(CXXFLAGS) mysql_example.cpp -o mysql_client $(LDLIBS)
