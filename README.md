
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://opensource.org/licenses/MIT)

This ymodem implementation is tested to work against the USART IAP protocol from ST (https://www.st.com/en/embedded-software/x-cube-iap-usart.html)
The python script can be used to send a binary file to an ST microcontroller.

## Usage
python3 upload.py flashfile.bin [serialDevice] [baudrate]

e.g.:
python3 upload.py flashfile.bin /dev/ttyS1 500000

The upload script sends a single character to initiate the transfer. Depending on your project you might need to change this behaviour.


## License 
[MIT License](https://opensource.org/licenses/MIT)
