# KYC Issuer (this document is WORK IN PROGRESS)


This Issuers implements the following protocols:

* [DIF DIDComm Messaging V2](https://identity.foundation/didcomm-messaging/spec/)
* [Out-of-Band Messages 2.0](https://identity.foundation/didcomm-messaging/spec/#out-of-band-messages)
* [Routing Protocol 2.0](https://identity.foundation/didcomm-messaging/spec/#routing-protocol-20)
* [Peer DID Method Specification](https://identity.foundation/peer-did-method-spec/)
* [HTTPS Transport](https://identity.foundation/didcomm-messaging/spec/#https)
* [Trust Ping Protocol 2.0](https://identity.foundation/didcomm-messaging/spec/#trust-ping-protocol-20)
* [Discover Features Protocol 2.0](https://identity.foundation/didcomm-messaging/spec/#discover-features-protocol-20)
* [WACI PEx Issue Credential Protocol 3.0](https://didcomm.org/issue-credential/3.0/): only a subset was implemented, request-credential --> issue-credential
* [Shorten URL Protocol 1.0]()

### ToDo's
Pending features and known issues and missings can be found at the [issues]([issues](https://github.com/roots-id/didcomm-mediator/issues)) section in this repository.
Note that this mediator is currently a **Proof of Concept**. Several `TODO`'s still pending in the code.

### Significant libraries
DIDComm and Peer DID were implemented with the help of the following amazing libraries from SICPA:
* [sicpa-dlab/didcomm-python](https://github.com/sicpa-dlab/didcomm-python)
* [sicpa-dlab/peer-did-python](https://github.com/sicpa-dlab/peer-did-python)

## RootsID Cloud instance live!
We have deployed an instance of the mediator in the cloud for testing, demoing, and learning.
Your identity wallet can scan the following Out of Band invitation QR code and request mediation:

![QR Code](https://mediator.rootsid.cloud/oob_qrcode)

Or scan the small QR code (OOB D) that redirect to the big one:

![Small QR Code](https://mediator.rootsid.cloud/oob_small_qrcode)


### Installation
```
python -m venv ./venv 
source ./venv/bin/activate
pip install requirements.txt
```
### Mongo DB
This mediator use [MongoDB](https://www.mongodb.com) as Data Base. You need to have it installed before running. One installaton option is with docker as:
```
docker pull mongo
docker run --name mongo_example -d mongo
```

### Envirnomental varables
The following environmental variables are needed. Change the values as your need:
```
export DB_URL=mongodb://localhost:27017
export PUBLIC_URL=http://127.0.0.1:8000
export ROTATE_OOB=0  // rotate OOB at startup if set
export MONGODB_USER=XXXXXX
export MONGODB_PASSWORD=yyyyy
export WOLFRAM_ALPHA_API_ID=ZZZZZZ // only for basicmessage demo (https://www.wolframalpha.com)
```

### Runing the agent
```
uvicorn main:app --reload
```

## Build docker
```
docker build -f ./Dockerfile . --platform=linux/amd64 -t rodopincha/didcomm-mediator
docker push rodopincha/didcomm-mediator 
docker run -p 8000:8000 rodopincha/didcomm-mediator
```

## ATALA Prism Credential Issuer
In order to issue Prism Credentials you need Java 11 and download Prism SDK (need a Prism SDK password from IOG). This agent use JPype as a wrapper to access Java classes from Python. 

1- Export your Prism SDK Password: `export PRISM_SDK_PASSWORD="ghp_..."`

2- Download anx extract the JVM SDK
```
curl "https://maven.pkg.github.com/input-output-hk/atala-prism-sdk/io/iohk/atala/prism-cli/v1.4.1/prism-cli-v1.4.1.zip" -H "Authorization: Bearer ${PRISM_SDK_PASSWORD}" -L -O
unzip prism-cli-v1.4.1.zip
```
3- Export JAVA_HOME and ATALA_PRISM_JARS as follows:
```
export JAVA_HOME=<java_home_directory>
export ATALA_PRISM_JARS="<working_dir>/prism-cli-v1.4.1/lib"
```
4- Export Prism Issuer switch
```
export PRISM_ISSUER=1
```
