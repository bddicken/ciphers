
INSTALL_DIR = ./bin
HOME_DIR = ./

all:
	rm -rf $(INSTALL_DIR)
	mkdir $(INSTALL_DIR)
	chmod 777 $(HOME_DIR)/src/main.py
	ln -s ../$(HOME_DIR)/src/main.py $(INSTALL_DIR)/cipher

clean:
	rm -rf bin
	rm -rf src/*.pyc
