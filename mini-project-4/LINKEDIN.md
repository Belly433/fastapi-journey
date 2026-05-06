## Post Text
I completed a real-time polling application using FastAPI, REST APIs, WebSockets, and Docker.
In this project, users can create polls, vote in real time, and instantly see vote updates without refreshing the page. I implemented both REST endpoints and WebSocket communication to better understand the difference between normal HTTP requests and persistent real-time connections.

I faced one challenge which was testing real-time updates accross multiple clients. At the beginning, I had trouble keeping multiple WebSocket connections open at the same time, but I solved it by testing with Postman and an online WebSocket client together. It helped me to verify that votes were synchronized correctly to all connected clients.
I also containerized the application using Docker and tested the API inside the container environment.

This project helped me to understand better real-time systems.
#FastAPI #WebSockets #BackendDevelopment #Python

## Public URL

https://www.linkedin.com/posts/belly-dynella-sabushimike-351bb13b2_fastapi-websockets-backenddevelopment-ugcPost-7457696139262193664-PTbl?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGTpp60BgZpAlMfytMw31YExYkXcHxbC_G4