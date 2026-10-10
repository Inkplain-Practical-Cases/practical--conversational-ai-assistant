from app.features.chat.services.authorized_tools import invoke_allowlisted_tool
import pytest
def test_scoped_tool_read():
    assert invoke_allowlisted_tool("lookup_order_status",{"order_id":"order-1"},"tenant-a")["status"]=="shipped"
def test_denied_tool():
    with pytest.raises(PermissionError):invoke_allowlisted_tool("delete_orders",{},"tenant-a")
