## Pydantic fields
- I used 'int' for book id because it represents a number which is an identifier.
- I used 'str' for book title and author because they represent a text value
- I used 'date' for borrow_date and retur,_date because they represent a real date calendar
- The return_date is optional because a book may not be returned

## Validation rules 

-The 'id' field uses gt=0 to ensure that id has to be positive
- The 'title' field uses min_length and max_lenght to avoid empty and long titles
- The 'author' field uses min_lenght to make sure of valid names
- The 'year' field uses a range between 1500 and 2100 to avaoid invalid years

## Async

The async endpoint uses await asynchio.sleep(1) to handle a request while other is waiting.

## Database

I used @contextmanager to manage the database connection automatically. It opens the connection when needed and closes it after use, which avoids forgetting to close it manually.

The parameter check_same_thread=False allows multiple requests to use the database safely in FastAPI, since FastAPI can handle concurrent requests.

With the old list, all data was lost when the server restarted because it was stored in memory. With SQLite, the data is saved in a file, so it persists even after restarting the server.