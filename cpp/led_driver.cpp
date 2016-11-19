/* Writen with love by Putz 2016. */

#include <iostream>
#include <errno.h>
// #include <wiringPiSPI.h>
#include <unistd.h>

using namespace std;

/* Constants */
unsigned char * data;
int a_totalShiftRegisters = 72;
static const int CHANNEL = 1;

/* Helpers */
int getRegisterPin(int outputPin) {
  return outputPin % 8;
}

int getRegisterNumber(int outputPin) {
  return outputPin / 8;
}

void set(int outputPin) {
  int registerPin = getRegisterPin(outputPin);
  int registerNumber = getRegisterNumber(outputPin);
  data[registerNumber] |= 1 << registerPin;
}

void clear(int outputPin) {
  int registerPin = getRegisterPin(outputPin);
  int registerNumber = getRegisterNumber(outputPin);
  data[registerNumber] &= ~(1 << registerPin);
}

int main()
{
	cout << "Starting up!" << endl;
	data = new unsigned char[a_totalShiftRegisters]();
	int dataSize = a_totalShiftRegisters * sizeof(unsigned char);

	int fd = wiringPiSPISetup(CHANNEL, 500000);
	cout << "Init result: " << fd << endl;

	// Reset pin state
	for (int i = 0; i < 575; i++) {
		clear(i);
	}

	for (int i = 0; i < 575; i++) {
		set(i);
		wiringPiSPIDataRW(CHANNEL, data, dataSize);
		usleep(500000);
	}

	return 0;
}
