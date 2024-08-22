#given a paper id , it will return title and abstract

#extracting title and abstract from the document



from elsapy.elsclient import ElsClient #to establish a connection with thier database
from elsapy.elsdoc import FullDoc #full doc function used to retrieve abstarct
from metaphor_python import Metaphor #tell the best research papers
import re #regular expressions
import concurrent.futures # multi threading
# Initialize ElsClient
client = ElsClient('8587565025ca7f1e6e0a3f026b32f6eb')

# Create FullDoc object with the PII
pii_doc = FullDoc(sd_pii='S0378517323011638')

# Read the document
if pii_doc.read(client):
    print("Document title:", pii_doc.title)
    print("Abstract:", pii_doc.data['coredata']['dc:description'])

else:
    print("Failed to read document.")
