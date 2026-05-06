1. I used "connections" which is a Python dictionary to tack connected clients. When a client disconnects, WebSocketDisconnect removes it from the list. This action prevents the server from crashing if someone closes the browser or disconnects during voting. The app continues running normally for the other connected users.

2. I stored votes in memory because the project is small and using Python dictionary is faster than setting up a database. I noticed that after restarting the server, all votes disappeared and the the poll IDs started again from 1. To make this production-ready, I would replace in-memory storage with a database like MongoDB.

3. If two users vote at the same time, FastAPI can process both requests asynchronously.
I didn't implement advanced concurrency prote tion in this project. The risk is in a high-traffic situation, some votes might not update correctly.

4. The REST endpoint(POST/polls/{id}/vote) sends one request and receives one response. The WebSocket connection stays open continuously and pushes updates instantly to all connected clients. REST is better for simple actions and enough when live updates are not required, WebSocket is better for real-time updates without refreshing.