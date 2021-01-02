from zeep import Client

# create the client upon conection to the SOAP webservice
myClient = Client("http://www.soapclient.com/xml/soapresponder.wsdl")

# now lets invoke the service passing parameters

part1 = '"This is the first part"' 
part2 = '"This is another part"' 

# each part will be sent as a parameter to the webservice

response = myClient.service.Method1(bstrParam1=part1, bstrParam2=part2)

print(response)