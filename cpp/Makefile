CXXFLAGS=-O0 -g -std=c++11 -Wall -Bdynamic
LDLIBS=-lzmqpp -lzmq -lmysqlcppconn

zmq_client:	
	g++ $(CXXFLAGS) zmq_client.cpp -o client $(LDLIBS)

mysqlclient:
	g++ $(CXXFLAGS) standalone_example.cpp -o mysql_client $(LDLIBS)
