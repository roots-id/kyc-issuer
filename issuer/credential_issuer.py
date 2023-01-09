""" Credential Issuer """
from didcomm.message import Message, FromPrior
import uuid
from didcomm.unpack import UnpackResult
from db_utils import get_issuer_did
import datetime
from didcomm.message import Attachment, AttachmentDataJson
from blockchains.prism import issue_prism_credential
from .dataseers import seersScan
import json



async def issue_credential(unpack_msg: UnpackResult, remote_did, local_did, from_prior: FromPrior):
    # 1-Validate credential request
    # TODO validate if attachements and add multiple attachments
    credential_attachment = unpack_msg.message.attachments[0]
    selfie_attachment = unpack_msg.message.attachments[1]
    card_id_attachment = unpack_msg.message.attachments[2]
    # TODO throw error if format is not supported
    # TODO validate options
    #if attachment.format == "aries/ld-proof-vc-detail@v1.0":
    if True:
        vc_detail = credential_attachment.data.json
        credential_requested = vc_detail["credential"]
        
        # THIS IS FOR DEMO PURPOSES
        issuer_did = get_issuer_did()
        credential = {
            "id": str(uuid.uuid4()),
            "name": credential_requested["name"],
            "issuer": {
                "id": issuer_did,
                "name": "RootsID"
            },
            "issuanceDate": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "credentialSubject": {
                "id": credential_requested["credentialSubject"]["id"],
                "name": credential_requested["credentialSubject"]["first_name"] + " " + credential_requested["credentialSubject"]["first_name"],
                "first_name": credential_requested["credentialSubject"]["first_name"],
                "last_name": credential_requested["credentialSubject"]["last_name"],
                "email": credential_requested["credentialSubject"]["last_name"],
                "image": "https://www.dataseers.ai/wp-content/uploads/Logo_DataSeers1920-1.png",
            }
        }

        # 2- Call dataseers
        seer_scan_result = await seersScan(
            credential_requested["credentialSubject"],
            selfie_attachment.data.json["base64"]["value"],
            card_id_attachment.data.json["base64"]["value"]
        )

        credential["credentialSubject"]["verificationResult"]  = seer_scan_result["result"]
        credential["credentialSubject"]["verificationSummary"]  = seer_scan_result["verification_summary"]
        credential["credentialSubject"]["imageMetricsResult"]  = seer_scan_result["image_metrics_result"]
        # 3 - Call Prism or sign credential (TODO)
        # prism_credential_info = await issue_prism_credential(issuer_did, holder_did,credential)
        # holder_signed_credential = prism_credential_info.getCredentialsAndProofs()[0].getSignedCredential()
        # holder_credential_merkle_proof = prism_credential_info.getCredentialsAndProofs()[0].getInclusionProof()
        
        
        credential["proof"] = {
            "type": "EcdsaSecp256k1Signature2019",
            "created": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "verificationMethod": issuer_did,
            "proofPurpose": "assertionMethod",
            "proofValue": "abcd", #str(holder_signed_credential.getCanonicalForm()),
            "proofHash": "abcd", #json.loads(str(holder_credential_merkle_proof.encode()))["hash"],
            "proofBatchId": "abcd" #str(prism_credential_info.getBatchId().getId())
        } 

               

         # 4- Respond with issue-credential
    
        response_message = Message(
        id=str(uuid.uuid4()),
        type="https://didcomm.org/issue-credential/3.0/issue-credential",
        body=unpack_msg.message.body,
        from_prior = from_prior,
        attachments = [
        Attachment(
                id=str(uuid.uuid4()),
                media_type= "application/json",
                format= "aries/ld-proof-vc-detail@v1.0",
                data=AttachmentDataJson(json=credential)
                )
            ]
        )
        return response_message
    else:
        # TODO RETURN ERROR
        return "ERROR"