# This is an origin request function


def lambda_handler(event, context):
    request = event["Records"][0]["cf"]["request"]
    headers = request["headers"]

    """
    Based on the value of the CloudFront-Viewer-Country header, generate an
    HTTP status code 302 (Redirect) response, and return a country-specific
    URL in the Location header.
    NOTE: 1. You must configure your distribution to cache based on the
            CloudFront-Viewer-Country header. For more information, see
            https://docs.aws.amazon.com/console/cloudfront/cache-on-selected-headers
          2. CloudFront adds the CloudFront-Viewer-Country header after the viewer
            request event. To use this example, you must create a trigger for the
            origin request event.
    """

    url = "https://example.com/"
    viewer_country = headers.get("cloudfront-viewer-country")
    if viewer_country:
        country_code = viewer_country[0]["value"]
        if country_code == "TW":
            url = "https://tw.example.com/"
        elif country_code == "US":
            url = "https://us.example.com/"

    response = {
        "status": "302",
        "statusDescription": "Found",
        "headers": {"location": [{"key": "Location", "value": url}]},
    }

    return response
