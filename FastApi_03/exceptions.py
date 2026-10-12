from fastapi.responses import JSONResponse
from fastapi import Request

class PincodeNotFoundError(Exception):
    def __init__(self, pincode:str):
        self.pincode = pincode

class InvalidPincodeError(Exception):
    def __init__(self,pincode:str , reason:str = "Invalid pincode format"):
        self.pincode = pincode
        self.reason = reason

# custome handler

async def pincode_not_found_handler(request:Request,exc:PincodeNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error":"pincode_not_found",
            "message":f"No location for pincode {exc.pincode}",
            "pincode":exc.pincode
        }
    )

async def invalid_pincod_handler(request:Request,exc:InvalidPincodeError):
    return JSONResponse(
        status_code=404,
        content={
            "error":"invalid_pincode",
            "message":f"Pincode '{exc.pincode}' is invlid:{exc.reason}",
            "pincode":exc.pincode
        }
    )