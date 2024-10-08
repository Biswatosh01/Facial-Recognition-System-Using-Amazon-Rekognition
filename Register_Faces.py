import pandas as pd
import boto3
from botocore.exceptions import ClientError

credential = pd.read_csv("titan_accessKeys.csv")
access_key_id = credential['Access key ID'][0]
secret_access_key = credential['Secret access key'][0]

client = boto3.client('rekognition',region_name='ap-south-1', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)


def add_face_to_collection(source_img_bytes,image_name,COLLECTION_NAME):

    try:
        lst = []
        print('Adding face...')
        request = {
            'Bytes': source_img_bytes
        }
        response = client.index_faces(CollectionId=COLLECTION_NAME, Image=request,
                                         ExternalImageId=image_name, QualityFilter='AUTO', DetectionAttributes=['ALL'])
        face_record = response['FaceRecords']
        if len(face_record) == 0:
            lst.append("No faces found")
            lst.append("Registration Not completed")
            return lst
        else:

            print('Result for: ' + image_name)
            lst.append('Result for: ' + image_name)
            print('Face indexed: ')
            lst.append('Face indexed with ID ')
            print('Person name: ' + face_record[0]['Face']['ExternalImageId'])
            lst.append('Person name: ' + face_record[0]['Face']['ExternalImageId'])
            print('------------------------------------------------------------------------------------------------------------')
            lst.append("Succefully Registered face" )
            return lst
    except ClientError as e:
        lst=[]
        # lst.append(str(e))
        lst.append(("Do not give space for person name and Not Registerd face please try agian"))
        print(lst)
        return lst


