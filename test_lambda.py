from lambda_function import handler

def test_handler():
    result = handler({}, {})
    assert result["statusCode"] == 200