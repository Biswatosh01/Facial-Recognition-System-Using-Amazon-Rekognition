# Facial-Recognition-Using-Amazon-Rekognition

Use python 3.11

# Steps to run code

1 Create aws account if not created yet.
  Link - for creation - https://aws.amazon.com/
  
2 Create a **user** using IAM management Console in aws account with one Policy named as **AmazonRekognitionFullAccess**
  After creating user it will provide a csv file which contains credentials . 
  
  csv file name - <user_accessKeys>.csv
  
3 Download csv file and copy that file to Face-recognition-using-Amazon-Rekognition Directory

4 Install all library mentioned in requiremets.txt

5 Replace the path of the <user_accessKeys>.csv file with your accessKey.csv file in Create_Collection.py, Face_recognize.py, Register_Faces.py

6 Run app.py file



# Solution Architecture
![flow](https://user-images.githubusercontent.com/49396196/147386515-9649f377-3195-401c-9c1e-87d1e5fc8fde.png)
