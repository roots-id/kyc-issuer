""" Basic Message Protocol 2.0 """
from didcomm.message import Message, FromPrior
import uuid
from didcomm.pack_encrypted import pack_encrypted, PackEncryptedConfig, PackEncryptedResult
from didcomm.common.resolvers import ResolversConfig
from didcomm.unpack import UnpackResult
from importlib_metadata import metadata
from didcomm_v2.peer_did import get_secret_resolver
from didcomm_v2.peer_did import DIDResolverPeerDID
import datetime
import urllib.parse
import requests
import os

async def process_basic_message(unpack_msg: UnpackResult, remote_did, local_did, from_prior: FromPrior):
    """ Response to Basic message with same message """
    question = urllib.parse.quote(unpack_msg.message.body["content"])

    if "WOLFRAM_ALPHA_API_ID" in os.environ:
        answer = requests.get("http://api.wolframalpha.com/v1/result?i="+question+"&appid="+os.environ["WOLFRAM_ALPHA_API_ID"]).text
    else: 
        answer = "No Wolfram Apha API ID in server"
    response_message = Message(
        id=str(uuid.uuid4()),
        thid=unpack_msg.message.id if not unpack_msg.message.thid else unpack_msg.message.thid,
        type="https://didcomm.org/basicmessage/2.0/message",
        body={"content": answer},
        custom_headers = [{
        "sent_time": int(datetime.datetime.now().timestamp())            
                      }],
        from_prior = from_prior
    )
    response_packed = await pack_encrypted(
        resolvers_config=ResolversConfig(
            secrets_resolver=get_secret_resolver(),
            did_resolver=DIDResolverPeerDID()
        ),
        message=response_message,
        frm=local_did,
        to=remote_did,
        sign_frm=None,
        pack_config=PackEncryptedConfig(protect_sender_id=False)
    )
    return response_packed.packed_msg
