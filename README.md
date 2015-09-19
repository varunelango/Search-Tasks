
A lightweight RESTful API for searching photos in Flickr.

Overview
=======

This is the official repository of the my RESTful API which is used to search photos on flickr using the official Flickr Search API. 

This API is written in Python, and uses the [Flask](http://flask.pocoo.org/) micro web-framework, which has a bundled WSGI server.

Requirements
=======

* Python 2.7.x 
* Python FLask 

Setup
=======

I suggest first creating a virtual environment via [virtualenv](https://virtualenv.pypa.io/en/latest/) before installing the below requirements. Otherwise, they'll be installed globally. 

To run the app on port 5000 (default), type:

```bash
$ python app.py
```

API Documentation
=======

All of the API route (Flask) implementations can be found in the `app.py` file.

---
### GET Photos
---

Returns a JSON which has all the photo information related to the particular search term from Flickr.

* **URL**

  `/search/<term>`

* **Method:**
  
  `GET`
  
*  **URL Params**

   **Required:**
 
     `*term*`

   **Optional:**
 
     None

* **Data Params**

  **Required:**
    
    None

  **Optional:**
    
    None

* **Success Response:**

  * **Code:** 200 <br />
  * **Content:**
      
      ```json
      [
    	{"photos":{"page":1,"pages":139137,"perpage":2,"total":"278273","photo":[{"id":"21530907282","owner":"120418906@N08","secret":"1afab0f31f","server":"5702","farm":6,"title":"692","ispublic":1,"isfriend":0,"isfamily":0},{"id":"21515800366","owner":"132493097@N02","secret":"a4ceff0de2","server":"5770","farm":6,"title":"_K5_1640","ispublic":1,"isfriend":0,"isfamily":0}]},"stat":"ok"}
	   ]
      ``` 

* **Sample Call:**

  ```bash
    curl -H "Content-Type: application/json" http://localhost:5000/search/tiger
  ```

---
### GET Photos by limit
---

Returns a JSON which has all the photo information for a particular term with a specified limit on the number of photos.

* **URL**

`/search/<term>/<limit>`

* **Method:**

`GET`

*  **URL Params**

**Required:**

 `*term*`
 
 `*limit*`

**Optional:**

 None

* **Data Params**

**Required:**

None

**Optional:**

None

* **Success Response:**

* **Code:** 200 <br />
* **Content:**
  
  ```json
  [
   {"photos":{"page":1,"pages":139137,"perpage":2,"total":"278273","photo":[{"id":"21530907282","owner":"120418906@N08","secret":"1afab0f31f","server":"5702","farm":6,"title":"692","ispublic":1,"isfriend":0,"isfamily":0},{"id":"21515800366","owner":"132493097@N02","secret":"a4ceff0de2","server":"5770","farm":6,"title":"_K5_1640","ispublic":1,"isfriend":0,"isfamily":0}]},"stat":"ok"}
   ]
  ``` 

* **Sample Call:**

```bash
curl -H "Content-Type: application/json" http://localhost:5000/search/tiger/2
```


---
### GET photos by limit and page
---

Returns a JSON which has all the photo information for a particular term with a specified limit on the number of photos in the specified number of pages. Here we have set the default number of page to 1

* **URL**

`/search/<term>/<limit>/page`

* **Method:**

`GET`

*  **URL Params**

**Required:**

`*term*`

`*limit*`

**Optional:**

None

* **Data Params**

**Required:**

None

**Optional:**

None

* **Success Response:**

* **Code:** 200 <br />
* **Content:**

```json
[
{"photos":{"page":1,"pages":139137,"perpage":2,"total":"278273","photo":[{"id":"21530907282","owner":"120418906@N08","secret":"1afab0f31f","server":"5702","farm":6,"title":"692","ispublic":1,"isfriend":0,"isfamily":0},{"id":"21515800366","owner":"132493097@N02","secret":"a4ceff0de2","server":"5770","farm":6,"title":"_K5_1640","ispublic":1,"isfriend":0,"isfamily":0}]},"stat":"ok"}
]
``` 

* **Sample Call:**

```bash
curl -H "Content-Type: application/json" http://localhost:5000/search/tiger/2/page
