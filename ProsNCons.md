# SSE (Server Sent Event)

## Pro's
- SSE is transmitted over regular HTTP (pass threw firewall) ;
- Very simple to use ;
- No need to implement specific protocol like Websocket ;
- Requests can be redirected using HTTP 301 and 307 redirects as with normal HTTP requests ;
- Automatic reconnection ;
- When automatic reconnection is done, the last event ID received is sent to the server which can decide to send events from this point ;
- HTTP error handling standards ;
- Headers can be overriden with native SSE libraries (Java, Objective C...) ;
- Server load is lighter with SSE compare to websocket ;
- Save 75% to 95%  end-user battery than polling ;
- Available in HTTP/2 ;
- Good performance (**needs references or load test**) ;
- Easy to extend (broadcast...) ;
- Built-in Event names and ids support.

## Con's
- One way connection : the client initialize the connection but only the server send events ;
- A lot of client consume a considerable load of the server resources => need to load test ;
- client can be told to stop reconnecting using the HTTP 204 No Content response code so impossible to use this HTTP code to say "Nothing to send" ;
- Headers can not be override in javascript (EventSource API) ;
- Some browsers need polyfill : [caniuse](https://caniuse.com/#search=server%20sent%20event). Use the one recommended [here](https://apifriends.com/api-streaming/server-sent-events/) ;
- 6 parallel connections from browser (1024 for websocket).

## Resources
- [Specifications](https://html.spec.whatwg.org/multipage/server-sent-events.html#parsing-an-event-stream)
- [Load test example](https://www.blazemeter.com/blog/how-to-load-test-sse-services-with-jmeter/)
- [Resource to help comprehension](https://apifriends.com/api-streaming/server-sent-events/)
- [Yet another resource to help comprehension](https://apifriends.com/api-streaming/push-sse-vs-websockets/)
- [Yet another resource to improve comprehension](https://medium.com/conectric-networks/a-look-at-server-sent-events-54a77f8d6ff7)
- [Yet another resource to master SSE](https://building.lang.ai/our-journey-from-websockets-to-http-2-4d069c54effd)
- [Websocket VS SSE comparison](https://apifriends.com/api-streaming/push-sse-vs-websockets/)
- [Study about power saving client side](https://www.researchgate.net/publication/256453451_The_Comparison_of_Impacts_to_Android_Phone_Battery_between_Polling_Data_and_Pushing_Data)
- [How to choose between SSE, Websocket and Polling](https://blog.stanko.io/do-you-really-need-websockets-343aed40aa9b)