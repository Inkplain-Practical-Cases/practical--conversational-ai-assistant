"""Read-only allowlisted customer lookup service; side effects forbidden in STEP-4."""
DEMO_STATUS={"order-1":"shipped","order-2":"processing"}
def lookup_order_status(order_id:str,tenant_id:str)->dict[str,str]:
    """Retrieve synthetic status only for an explicitly provided tenant scope."""
    if not tenant_id:raise PermissionError("Tenant ownership missing")
    if order_id not in DEMO_STATUS:raise LookupError("Unknown order")
    return {"order_id":order_id,"status":DEMO_STATUS[order_id],"tenant_id":tenant_id}

def invoke_allowlisted_tool(name:str,arguments:dict,tenant_id:str)->dict:
    """Allow only read-only status tool; never route arbitrary model-provided names."""
    if name!="lookup_order_status":raise PermissionError("Tool not allowed")
    if set(arguments)!={"order_id"}:raise ValueError("Unexpected tool arguments")
    return lookup_order_status(arguments["order_id"],tenant_id)
