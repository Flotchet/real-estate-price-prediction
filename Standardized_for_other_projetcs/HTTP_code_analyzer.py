import functools

@functools.lru_cache(maxsize=None)
def status_to_text_summarized(status_code: int) -> str:

    """
    Convert a status code to a text message.
    take int as an entry
    return str as an output
    """
    # Convert a status code to a text message.

    status_dict = {
        # infos response
        100: "Continue",
        101: "Switching Protocols",
        102: "Processing",
        103: "Early Hints",
        # success response
        200: "OK",
        201: "Created",
        202: "Accepted",
        203: "Non-Authoritative Information",
        204: "No Content",
        205: "Reset Content",
        206: "Partial Content",
        207: "Multi-Status",
        208: "Already Reported",
        226: "IM Used",
        # redirection response
        300: "Multiple Choices",
        301: "Moved Permanently",
        302: "Found",
        303: "See Other",
        304: "Not Modified",
        305: "Use Proxy",
        306: "Switch Proxy",
        307: "Temporary Redirect",
        308: "Permanent Redirect",
        # client error response
        400: "Bad Request",
        401: "Unauthorized",
        402: "Payment Required",
        403: "Forbidden",
        404: "Not Found",
        405: "Method Not Allowed",
        406: "Not Acceptable",
        407: "Proxy Authentication Required",
        408: "Request Timeout",
        409: "Conflict",
        410: "Gone",
        411: "Length Required",
        412: "Precondition Failed",
        413: "Payload Too Large",
        414: "URI Too Long",
        415: "Unsupported Media Type",
        416: "Range Not Satisfiable",
        417: "Expectation Failed",
        418: "I'm a teapot",
        421: "Misdirected Request",
        422: "Unprocessable Entity",
        423: "Locked",
        424: "Failed Dependency",
        425: "Too Early",
        426: "Upgrade Required",
        428: "Precondition Required",
        429: "Too Many Requests",
        431: "Request Header Fields Too Large",
        451: "Unavailable For Legal Reasons",
        # server error response
        500: "Internal Server Error",
        501: "Not Implemented",
        502: "Bad Gateway",
        503: "Service Unavailable",
        504: "Gateway Timeout",
        505: "HTTP Version Not Supported",
        506: "Variant Also Negotiates",
        507: "Insufficient Storage",
        508: "Loop Detected",
        510: "Not Extended",
        511: "Network Authentication Required"
    }
    # find if the status code is in the keys
    if status_code in status_dict.keys():
        return str(status_code) + ": " + status_dict[status_code]
    else:
        return str(status_code) + ": Unknown or unofficial status code"

def stts(status_code: int) -> str:
    """
    Short for status_to_text_sumarized,
    take int as an entry
    return str of the http code as an output
    """
    # Convert a status code to a text message.
    return status_to_text_summarized(status_code)


@functools.lru_cache(maxsize=None)
def status_to_text_complete(status_code: int) -> dict[str:str]:

    status_dict = {


        #1xx infos response

        100: {"Response" : "Continue",
                "Explaination" :
        """
        This interim response indicates that everything so far is OK and that the
        client should continue the request, or ignore the response if the request
        is already finished.
        """},

        101: {"Response" : "Switching Protocols",
                "Explaination" :
        """
        This code is sent in response to an Upgrade request header from the client,
        and indicates the protocol the server is switching to.
        """},

        102: {"Response" : "Processing",
                "Explaination" :
        """
        This code indicates that the server has received and is processing the request,
        but no response is available yet.
        """},

        103: {"Response" : "Early Hints",
                "Explaination" :
        """
        This status code is primarily intended to be used with the Link header, letting
        the user agent start preloading resources while the server prepares a response.
        """},


        #2xx success response

        200: {"Response" : "OK",
                "Explaination" :
        """
        This response means that the server has received the request and is processing
        it, but no response is available yet.
        """},

        201: {"Response" : "Created",
                "Explaination" :
        """
        This response means that the server has received the request and has
        successfully created a new resource.
        """},

        202: {"Response" : "Accepted",
                "Explaination" :
        """
        This response means that the request has been accepted for processing, but the
        processing has not been completed.
        """},

        203: {"Response" : "Non-Authoritative Information",
                "Explaination" :
        """
        This response means that the request has been successfully processed, but is
        returning information that may be from another source.
        """},

        204: {"Response" : "No Content",
                "Explaination" :
        """
        This response means that the server has successfully processed the request,
        and that there is no content to send in the response payload body.
        """},

        205: {"Response" : "Reset Content",
                "Explaination" :
        """
        This response means that the server has successfully processed the request,
        and that the user agent should reset the document view which caused the request
        to be sent.
        """},

        206: {"Response" : "Partial Content",
                "Explaination" :
        """
        This response means that the server is sending partial content as a response
        to a partial GET request.
        """},

        207: {"Response" : "Multi-Status",
                "Explaination" :
        """
        This response code means that the server has fulfilled a request for the
        resource, and the response is a representation of the result of one or more
        instance-manipulations applied to the current instance.
        """},

        208: {"Response" : "Already Reported",
                "Explaination" :
        """
        This response code is used inside a <dav:propstat> response element to avoid
        repeatedly enumerating the internal members of multiple bindings to the same
        collection repeatedly.
        """},
        226: {"Response" : "IM Used",
                "Explaination" :
        """
        This response code is used when the client has asked for a specific resource
        in the past, and is not willing to accept any other version of the resource.
        """},


        #3xx redirection response

        300: {"Response" : "Multiple Choices",
                "Explaination" :
        """
        The request has more than one possible response. The user agent or user should
        choose one of them. (There is no standardized way of choosing one of the
        responses, but HTML links to the possibilities are recommended so the user can
        pick.)
        """},

        301: {"Response" : "Moved Permanently",
                "Explaination" :
        """
        This response means that the URI of the requested resource has been changed.
        Probably, the new URI would be given in the response.
        """},

        302: {"Response" : "Found",
                "Explaination" :
        """
        This response means that the URI of requested resource has been changed.
        Temporarily. New changes in the URI might be made in the future. Therefore,
        this same URI should be used by the client in future requests.
        """},

        303: {"Response" : "See Other",
                "Explaination" :
        """
        This response means that the server sent this response to direct the client
        to get the requested resource at another URI with a GET request.
        """},

        304: {"Response" : "Not Modified",
                "Explaination" :
        """
        This is used for caching purposes. It tells the client that the response has
        not been modified, so the client can continue to use the same cached version
        of the response.
        """},

        305: {"Response" : "Use Proxy",
                "Explaination" :
        """
        This response code is no longer used. It is just reserved currently. It was
        used in a previous version of the HTTP/1.1 specification.
        """},

        306: {"Response" : "Switch Proxy",
                "Explaination" :
        """
        This response code is no longer used. It is just reserved currently. It was
        used in a previous version of the HTTP/1.1 specification.
        """},

        307: {"Response" : "Temporary Redirect",
                "Explaination" :
        """
        This response code means that the URI of requested resource has been changed.
        Temporarily. New changes in the URI might be made in the future. Therefore,
        this same URI should be used by the client in future requests.
        """},

        308: {"Response" : "Permanent Redirect",
                "Explaination" :
        """
        This response code means that the URI of requested resource has been changed
        permanently. And the new URI would be given in the response.
        """},

        #4xx client error response

        400: {"Response" : "Bad Request",
                "Explaination" :
        """
        This response means that server could not understand the request due to invalid
        syntax.
        """},

        401: {"Response" : "Unauthorized",
                "Explaination" :
        """
        Although the HTTP standard specifies "unauthorized", semantically this response
        means "unauthenticated". That is, the client must authenticate itself to get
        the requested response.
        """},

        402: {"Response" : "Payment Required",
                "Explaination" :
        """
        This response code is reserved for future use. Initial aim for creating this
        code was using it for digital payment systems, however this is not used currently.
        """},

        403: {"Response" : "Forbidden",
                "Explaination" :
        """
        The client does not have access rights to the content; that is, it is unauthorized,
        so the server is refusing to give the requested resource. Unlike 401, the client's
        identity is known to the server.
        """},

        404: {"Response" : "Not Found",
                "Explaination" :
        """
        The server can not find the requested resource. In the browser, this means the
        URL is not recognized. In an API, this can also mean that the endpoint is valid
        but the resource itself does not exist. Servers may also send this response instead
        of 403 to hide the existence of a resource from an unauthorized client. This response
        code is probably the most famous one due to its frequent occurrence on the web.
        """},

        405: {"Response" : "Method Not Allowed",
                "Explaination" :
        """
        The request method is known by the server but has been disabled and cannot be used.
        For example, an API may forbid DELETE-ing a resource. The two mandatory methods,
        GET and HEAD, must never be disabled and should not return this error code.
        """},

        406: {"Response" : "Not Acceptable",
                "Explaination" :
        """
        This response is sent when the web server, after performing server-driven content
        negotiation, doesn't find any content that conforms to the criteria given by the user agent.
        """},

        407: {"Response" : "Proxy Authentication Required",
                "Explaination" :
        """
        This is similar to 401 but authentication is needed to be done by a proxy.

        Although the HTTP standard specifies "unauthorized", semantically this response
        means "unauthenticated". That is, the client must authenticate itself to get
        the requested response.
        """},

        408: {"Response" : "Request Timeout",
                "Explaination" :
        """
        This response is sent on an idle connection by some servers, even without any
        previous request by the client. It means that the server would like to shut down
        this unused connection. This response is used much more since some browsers,
        like Chrome, Firefox 27+, or IE9, use HTTP pre-connection mechanisms to speed
        up surfing. Also note that some servers merely shut down the connection without
        sending this message.
        """},

        409: {"Response" : "Conflict",
                "Explaination" :
        """
        This response is sent when a request conflicts with the current state of the server.
        """},

        410: {"Response" : "Gone",
                "Explaination" :
        """
        This response is sent when the requested content has been permanently deleted from
        server, with no forwarding address. Clients are expected to remove their caches
        and links to the resource. The HTTP specification intends this status code to be
        used for "limited-time, promotional services". APIs should not feel compelled to
        indicate resources that have been deleted with this status code.
        """},

        411: {"Response" : "Length Required",
                "Explaination" :
        """
        Server rejected the request because the Content-Length header field is not defined
        and the server requires it.
        """},

        412: {"Response" : "Precondition Failed",
                "Explaination" :
        """
        The client has indicated preconditions in its headers which the server does not meet.
        """},

        413: {"Response" : "Payload Too Large",
                "Explaination" :
        """
        Request entity is larger than limits defined by server; the server might close the
        connection or return an Retry-After header field.
        """},

        414: {"Response" : "URI Too Long",
                "Explaination" :
        """
        The URI requested by the client is longer than the server is willing to interpret.
        """},

        415: {"Response" : "Unsupported Media Type",
                "Explaination" :
        """
        The media format of the requested data is not supported by the server, so the server
        is rejecting the request.
        """},

        416: {"Response" : "Range Not Satisfiable",
                "Explaination" :
        """
        The range specified by the Range header field in the request can't be fulfilled; it's
        possible that the range is outside the size of the target URI's data.
        """},

        417: {"Response" : "Expectation Failed",
                "Explaination" :
        """
        This response code means the expectation indicated by the Expect request header
        field can't be met by the server.
        """},

        418: {"Response" : "I'm a teapot",
                "Explaination" :
        """
        The server refuses the attempt to brew coffee with a teapot.
        """},

        421: {"Response" : "Misdirected Request",
                "Explaination" :

        """
        The request was directed at a server that is not able to produce a response (for
        example because of connection reuse).
        """},

        422: {"Response" : "Unprocessable Entity",
                "Explaination" :
        """
        The request was well-formed but was unable to be followed due to semantic errors.
        """},

        423: {"Response" : "Locked",
                "Explaination" :
        """
        The resource that is being accessed is locked.
        """},

        424: {"Response" : "Failed Dependency",
                "Explaination" :

        """
        The request failed due to failure of a previous request.
        """},

        425: {"Response" : "Too Early",
                "Explaination" :
        """
        Indicates that the server is unwilling to risk processing a request that might be
        replayed.
        """},

        426: {"Response" : "Upgrade Required",
                "Explaination" :
        """
        The client should switch to a different protocol such as TLS/1.0, given in the Upgrade
        header field.
        """},

        428: {"Response" : "Precondition Required",
                "Explaination" :
        """
        The origin server requires the request to be conditional. Intended to prevent the
        'lost update' problem, where a client GETs a resource's state, modifies it, and PUTs
        it back to the server, when meanwhile a third party has modified the state on the
        server, leading to a conflict.
        """},

        429: {"Response" : "Too Many Requests",
                "Explaination" :
        """
        The user has sent too many requests in a given amount of time. Intended for use with
        rate-limiting schemes.
        """},

        431: {"Response" : "Request Header Fields Too Large",
                "Explaination" :
        """
        The server is unwilling to process the request because either an individual header
        field, or all the header fields collectively, are too large.
        """},

        451: {"Response" : "Unavailable For Legal Reasons",
                "Explaination" :
        """
        A server operator has received a legal demand to deny access to a resource or to a
        set of resources that includes the requested resource. The code 451 was chosen as a
        reference to the novel Fahrenheit 451 (see the Acknowledgements in the RFC).
        """},


        # 5xx Server Error

        500: {"Response" : "Internal Server Error",
                "Explaination" :
        """
        The server has encountered a situation it doesn't know how to handle.
        """},

        501: {"Response" : "Not Implemented",
                "Explaination" :
        """
        The request method is not supported by the server and cannot be handled. The only
        methods that servers are required to support (and therefore that must not return
        this code) are GET and HEAD.
        """},

        502: {"Response" : "Bad Gateway",
                "Explaination" :
        """
        This error response means that the server, while working as a gateway to get a
        response needed to handle the request, got an invalid response.
        """},

        503: {"Response" : "Service Unavailable",
                "Explaination" :
        """
        The server is not ready to handle the request. Common causes are a server that is
        down for maintenance or that is overloaded. Note that together with this response,
        a user-friendly page explaining the problem should be sent. This responses should
        be used for temporary conditions and the Retry-After: HTTP header should, if possible,
        contain the estimated time before the recovery of the service. The webmaster must
        also take care about the caching-related headers that are sent along with this
        response, as these temporary condition responses should usually not be cached.
        """},

        504: {"Response" : "Gateway Timeout",
                "Explaination" :
        """
        This error response is given when the server is acting as a gateway and cannot get
        a response in time.
        """},

        505: {"Response" : "HTTP Version Not Supported",
                "Explaination" :
        """
        The HTTP version used in the request is not supported by the server.
        """},

        506: {"Response" : "Variant Also Negotiates",
                "Explaination" :
        """
        Transparent content negotiation for the request results in a circular reference.
        """},

        507: {"Response" : "Insufficient Storage",
                "Explaination" :
        """
        The server is unable to store the representation needed to complete the request.
        """},

        508: {"Response" : "Loop Detected",
                "Explaination" :
        """
        The server detected an infinite loop while processing the request (sent in lieu of
        208 Already Reported).
        """},

        510: {"Response" : "Not Extended",
                "Explaination" :
        """
        Further extensions to the request are required for the server to fulfil it.
        """},

        511: {"Response" : "Network Authentication Required",
                "Explaination" :
        """
        The client needs to authenticate to gain network access. Intended for use by
        intercepting proxies used to control access to the network (e.g., "captive portals"
        used to require agreement to Terms of Service before granting full Internet access
        via a Wi-Fi hotspot).
        """},

        599: {"Response" : "Network Connect Timeout Error",
                "Explaination" :
        """
        This status code is not specified in any RFCs, but is used by some HTTP proxies to
        signal a network connect timeout behind the proxy to a client in front of the proxy.
        """}

    }

    # find if the status code is in the keys
    if status_code in status_dict.keys():
        return status_dict[status_code]
    else:
        return None

def sttc(status_code: int) -> dict[str:str]:

    """
    Short for status_to_text_complete,
    this function takes a status code and returns a dictionary
    with the response and explaination of the status code.
    """

    return status_to_text_complete(status_code)

def sttc_as_text(status_code: int) -> str:

    """
    Short for status_to_text_complete_as_text,
    this function takes a status code and returns a string
    with the response and explaination of the status code.
    """

    # get the dictionary
    status_dict = status_to_text_complete(status_code)

    # if the status code is not in the dictionary
    if status_dict == None:
        return "Status code not found"

    # get the response and explaination
    response = status_dict["Response"]
    explaination = status_dict["Explaination"]

    # return the response and explaination
    return f"""
    {str(status_code)}: {response}
    ---------------------------------
    {explaination}"""

def stt(status_code: int) -> str:

    """
    Short for status_to_text_complete_as_text,
    this function takes a status code and returns a string
    with the response and explaination of the status code.
    """

    return sttc_as_text(status_code)

def main():
    print("Running main function")
    print(sttc(200))
    print(stt(200))

if __name__ == "__main__":
    main()
