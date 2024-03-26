# Sign and Encryption of file 
In this you will get code for encryption and sign your file as well as sign verification and decryption of file.

## Commands execution step 

Step1 :  `python3 enc_key.py` <br />
It will generate and export a Fernet Key for encryption of file which have name 'enc_key.txt'.<br /><br />
Step2 :  `python3 key_generator.py` <br />
It will generate private and public key and export it with name 'public_key.pem' and 'private_key.pem'<br /><br />
Step3 :  `python3 enc_and_sign.py`<br />
   It will ask for file name to be encrypted and then encrypted file will be created with name 'enc_<file_name>'
   Then it will ask for file to sign(enc_<file_name>) then provide encrypted file to sign <br /><br />
Step4 :  `python3 verify_and_decrypt`<br />
   It will ask for file for sign verification and if provided it will give us a new file for decryption.


<b>Note:</b> This code will generate unique keys signature everytime you can't use anything twice
