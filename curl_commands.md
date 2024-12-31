`curl` is another powerful command-line tool used for transferring data with URLs, supporting a wide range of protocols such as HTTP, HTTPS, FTP, FTPS, SCP, SFTP, LDAP, and more. It’s very flexible and can be used for a variety of purposes including testing APIs, downloading files, and interacting with web services.

Here’s a comprehensive overview of the most common and advanced `curl` commands:

---

### **Basic Syntax:**

```bash
curl [options] [URL]
```

### **Common `curl` Commands and Options:**

#### **1. Download a File:**

```bash
curl -O http://example.com/file.zip
```

The `-O` option downloads the file and saves it with its original name.

#### **2. Download a File with a Different Name:**

```bash
curl -o newname.zip http://example.com/file.zip
```

The `-o` option allows you to specify the output file name.

#### **3. Download Multiple Files (using URLs from a file):**

```bash
curl -O -J -L -K urls.txt
```

The `-K` option allows you to specify a file (`urls.txt`) that contains a list of URLs to download.

#### **4. Follow Redirects:**

```bash
curl -L http://example.com
```

The `-L` option tells `curl` to follow any HTTP redirects (i.e., if the server responds with a redirect code, `curl` will automatically follow it).

#### **5. Resume a Download:**

```bash
curl -C - -O http://example.com/file.zip
```

The `-C -` option resumes a download from where it left off, and `-O` saves it with its original name.

#### **6. Show Progress Information:**

```bash
curl -# http://example.com/file.zip
```

The `-#` option enables a progress bar for better visibility on the download status.

---

### **Advanced Usage of `curl`**

#### **1. Sending Data with HTTP POST:**

```bash
curl -X POST -d "name=John&age=30" http://example.com/api
```

The `-X POST` option specifies that the request is a POST, and `-d` allows you to include data (form data or JSON) in the request body.

#### **2. Sending JSON with POST Request:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name":"John", "age":30}' http://example.com/api
```

Here, `-H` specifies the HTTP header (`Content-Type: application/json`), and `-d` sends the JSON payload.

#### **3. Sending Custom Headers:**

```bash
curl -H "Authorization: Bearer token_value" http://example.com/api
```

The `-H` option is used to send custom headers, such as an `Authorization` header for Bearer token-based authentication.

#### **4. Handling HTTP Authentication (Basic):**

```bash
curl -u username:password http://example.com/api
```

The `-u` option is used to send HTTP Basic Authentication credentials (`username:password`).

#### **5. Sending Data with PUT:**

```bash
curl -X PUT -d '{"name":"John"}' -H "Content-Type: application/json" http://example.com/api/resource
```

This sends a PUT request to update data, including a JSON payload in the request body.

#### **6. Uploading Files:**

```bash
curl -F "file=@filename.jpg" http://example.com/upload
```

The `-F` option allows you to upload a file (in this case, `filename.jpg`) as part of a form submission.

#### **7. Download Multiple Files Simultaneously:**

```bash
curl -O http://example.com/file1.zip -O http://example.com/file2.zip
```

You can specify multiple URLs after the `curl` command to download multiple files at once.

#### **8. Show Response Headers Only (without body):**

```bash
curl -I http://example.com
```

The `-I` option fetches only the HTTP headers from the URL.

#### **9. Verbose Output (Debugging):**

```bash
curl -v http://example.com
```

The `-v` (verbose) option gives detailed output, including request headers, response headers, and other debugging information.

#### **10. Save Cookies to a File:**

```bash
curl -c cookies.txt http://example.com
```

The `-c` option saves the cookies sent by the server into a file (`cookies.txt`).

#### **11. Load Cookies from a File:**

```bash
curl -b cookies.txt http://example.com
```

The `-b` option allows you to send cookies from a file in subsequent requests.

#### **12. Download with HTTP/2:**

```bash
curl --http2 http://example.com
```

This enables HTTP/2 for the request, which can result in faster loading times for websites that support the protocol.

#### **13. Specify Request Timeout:**

```bash
curl --max-time 30 http://example.com
```

The `--max-time` option allows you to specify the maximum time (in seconds) to wait for the server to respond. Here, the request will timeout after 30 seconds.

#### **14. Use Proxy:**

```bash
curl -x http://proxy.example.com:8080 http://example.com
```

The `-x` option specifies a proxy server. In this case, `http://proxy.example.com:8080` is the proxy.

---

### **Security and Authentication**

#### **1. Disable SSL Verification (useful for testing or insecure connections):**

```bash
curl -k https://example.com
```

The `-k` or `--insecure` option skips SSL certificate verification (use with caution).

#### **2. Use SSL Client Certificate for Authentication:**

```bash
curl --cert cert.pem --key key.pem https://example.com
```

If the server requires a client certificate, use `--cert` for the certificate and `--key` for the private key.

#### **3. Set Up HTTP Digest Authentication:**

```bash
curl --digest -u username:password http://example.com/api
```

Use `--digest` for HTTP Digest Authentication instead of basic auth.

#### **4. Use a Bearer Token for Authentication:**

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" http://example.com
```

This sends a Bearer token for API authentication in the header.

---

### **Advanced Options**

#### **1. Download a Website Recursively (like `wget`):**

```bash
curl -O -L -J -r http://example.com
```

Although `curl` doesn't support recursive downloading natively like `wget`, you can use other utilities in combination to achieve a similar effect. Alternatively, use `wget` for recursion.

#### **2. Using FTP (Download from FTP):**

```bash
curl -u username:password ftp://ftp.example.com/file.zip -O
```

Use `curl` for FTP downloads by specifying the FTP server URL and optionally including a username and password.

#### **3. Show Only the Body (Hide Headers):**

```bash
curl -s http://example.com
```

The `-s` (silent) option hides the progress meter and any additional headers, only showing the response body.

#### **4. Download File in Background:**

Unlike `wget`, `curl` doesn't have a built-in background option (`-b` in `wget`). However, you can run it in the background using `&`:

```bash
curl -O http://example.com/file.zip &
```

#### **5. Uploading Multiple Files:**

```bash
curl -F "file1=@file1.jpg" -F "file2=@file2.png" http://example.com/upload
```

Upload multiple files in one request.

#### **6. Use `curl` with Proxy Authentication:**

```bash
curl -x http://proxy.example.com:8080 --proxy-user username:password http://example.com
```

You can authenticate via a proxy using the `--proxy-user` option.

---

### **Example Use Cases**

1. **Download a File:**

   ```bash
   curl -O http://example.com/file.zip
   ```

2. **Fetch an API with JSON Data:**

   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"username": "john", "password": "1234"}' http://example.com/api/login
   ```

3. **Test API with Authentication:**

   ```bash
   curl -u username:password http://example.com/api
   ```

4. **Get HTTP Response Headers Only:**

   ```bash
   curl -I http://example.com
   ```

5. **Check HTTP Status Code:**

   ```bash
   curl -o /dev/null -s -w "%{http_code}" http://example.com
   ```

   This will show just the HTTP status code of the response (e.g., `200`, `404`).

---

### **References**

- [curl official documentation](https://curl.se/docs/)
- To get help on options, use:
  ```bash
  curl --help
  ```

Let me know if you need more detailed examples or have specific use cases in mind!

The `curl` command is a versatile tool used to transfer data from or to a server using various protocols, such as HTTP, HTTPS, FTP, SFTP, and more. It is widely used in scripting, debugging, and automation tasks. Here’s an in-depth guide to the most common and advanced `curl` commands and options:

### **Basic Syntax**

```bash
curl [options] [URL]
```

### **Common `curl` Commands and Options**

#### **1. Basic GET Request (Default Behavior)**

```bash
curl http://example.com
```

By default, `curl` sends a GET request to the provided URL and outputs the response to the terminal.

#### **2. Save Response to a File (`-o` or `-O`)**

- **Save to a specific file:**

  ```bash
  curl -o filename.html http://example.com
  ```

  Saves the content to `filename.html`.

- **Save with the same name as the remote file:**
  ```bash
  curl -O http://example.com/file.zip
  ```
  Downloads the file and saves it with the same name as the remote file.

#### **3. Send POST Request**

To send a POST request with data:

```bash
curl -X POST -d "key1=value1&key2=value2" http://example.com/form
```

Here, `-d` specifies the data to be sent in the body of the request. You can also use `-F` for sending form data.

#### **4. Send JSON in POST Request**

To send JSON data in a POST request:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"key1": "value1", "key2": "value2"}' http://example.com/api
```

- `-H`: Sets the request header (in this case, `Content-Type: application/json`).
- `-d`: Sends the data in the body.

#### **5. Follow Redirects (`-L`)**

If the URL redirects to another location, `curl` will follow the redirects using the `-L` option.

```bash
curl -L http://example.com
```

#### **6. Show Request and Response Headers (`-v` or `--verbose`)**

To see the detailed request and response headers:

```bash
curl -v http://example.com
```

This outputs both the headers and the body of the response.

#### **7. Include Response Headers in Output (`-i`)**

To include the HTTP response headers in the output, use the `-i` option:

```bash
curl -i http://example.com
```

This prints both headers and content, useful for debugging.

#### **8. Set Custom User-Agent (`-A`)**

To set a custom `User-Agent` header (mimicking a specific browser or bot):

```bash
curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36" http://example.com
```

#### **9. Send Custom Headers (`-H`)**

To add custom headers to a request:

```bash
curl -H "Authorization: Bearer your-token" http://example.com/api
```

#### **10. Include Cookies in Requests (`-b` and `-c`)**

- **Send cookies:**

  ```bash
  curl -b "name=value" http://example.com
  ```

- **Store cookies in a file (`-c`):**
  ```bash
  curl -c cookies.txt http://example.com
  ```

#### **11. Download Files in the Background (`-s` and `-S`)**

To download files silently (without showing progress) and still show errors if any occur:

```bash
curl -sS -O http://example.com/file.zip
```

#### **12. Basic Authentication (`-u`)**

To send a request with Basic Authentication:

```bash
curl -u username:password http://example.com/secure
```

`curl` will encode the username and password as a base64 string in the `Authorization` header.

#### **13. FTP Upload (`-T`)**

To upload a file to an FTP server:

```bash
curl -T localfile.txt ftp://ftp.example.com/remotefile.txt
```

This uploads `localfile.txt` to the FTP server at the specified path.

#### **14. HTTP Authentication (Digest, NTLM)**

- **Digest Authentication:**

  ```bash
  curl --digest -u username:password http://example.com
  ```

- **NTLM Authentication:**
  ```bash
  curl --ntlm -u username:password http://example.com
  ```

---

### **Advanced `curl` Options**

#### **1. Uploading Multiple Files**

You can upload multiple files at once using `-F` for form-based data:

```bash
curl -F "file1=@file1.txt" -F "file2=@file2.jpg" http://example.com/upload
```

#### **2. Show Only HTTP Response Code (`-w`)**

To output only the HTTP status code, you can use `-w`:

```bash
curl -w "%{http_code}" -o /dev/null -s http://example.com
```

- `-o /dev/null`: Discards the response body.
- `-s`: Silent mode (suppresses progress output).
- `%{http_code}`: The HTTP status code of the response.

#### **3. Limit Download Speed (`--limit-rate`)**

To limit the download speed to 100 KB/s:

```bash
curl --limit-rate 100k -O http://example.com/file.zip
```

#### **4. Download a Range of Bytes (`-r`)**

To download only a specific byte range from a file:

```bash
curl -r 0-499 http://example.com/file.zip -O
```

This downloads the first 500 bytes of the file.

#### **5. Timeout (`-m`, `--max-time`)**

To set a maximum time for the request to complete:

```bash
curl --max-time 30 http://example.com
```

This will time out the request if it takes longer than 30 seconds.

#### **6. Make an HTTPS Request Without Verifying the Certificate (`-k` or `--insecure`)**

If you are testing a server with an invalid SSL certificate, use the `-k` option to disable SSL certificate verification:

```bash
curl -k https://example.com
```

#### **7. HTTP/2 Support**

To force `curl` to use HTTP/2:

```bash
curl --http2 https://example.com
```

#### **8. Send Data from a File (`-d` with `@`)**

To send data from a file instead of specifying it inline:

```bash
curl -X POST -d @data.json http://example.com/api
```

This sends the contents of `data.json` as the body of the POST request.

#### **9. Show Only Response Headers (`-I`)**

To show only the headers of the response without downloading the content:

```bash
curl -I http://example.com
```

#### **10. Follow Redirects with Limit (`--max-redirs`)**

If you want to limit the number of redirects to follow, you can use `--max-redirs`:

```bash
curl -L --max-redirs 3 http://example.com
```

This will follow up to 3 redirects before stopping.

---

### **Examples of Complex `curl` Commands**

#### **1. Perform a GET Request with Multiple Headers**

```bash
curl -H "Authorization: Bearer token" -H "Accept: application/json" http://example.com/api
```

#### **2. Upload a File and Send JSON with Additional Headers**

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer token" -F "file=@file.txt" http://example.com/upload
```

#### **3. Download a Website and Store Cookies**

```bash
curl -c cookies.txt -L http://example.com
```

#### **4. Perform a GET Request and Write Response to a File**

```bash
curl -o response.html http://example.com
```

#### **5. Download and Save a File Only if It's Newer Than Local File**

```bash
curl -z localfile.txt -O http://example.com/file.zip
```

This downloads `file.zip` only if the remote file is newer than `localfile.txt`.

---

### **References**

To view the complete list of options for `curl`, you can check its manual by running:

```bash
man curl
```

Or visit the official documentation: [curl Manual](https://curl.se/docs/manual.html).

These are just a subset of the features `curl` offers. Let me know if you need further details or more examples on specific use cases!

Sure! Let’s dive even deeper into the `curl` command and its features. Here, we’ll cover advanced commands, use cases, and the specific options available for various protocols and scenarios. This guide will give you a comprehensive understanding of how to use `curl` for a wide range of tasks.

### **Advanced `curl` Features and Use Cases**

#### **1. Sending POST Data (Form and JSON)**

- **Basic POST with URL-encoded Data:**

  ```bash
  curl -X POST -d "key1=value1&key2=value2" http://example.com
  ```

  The `-d` option sends data as `application/x-www-form-urlencoded` (typical for web forms).

- **Sending JSON Data:**
  To send JSON, you must set the `Content-Type` header to `application/json`:

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"key1":"value1","key2":"value2"}' http://example.com/api
  ```

- **Form Data (e.g., file upload):**
  You can also send form data, including files, with `-F`:
  ```bash
  curl -X POST -F "name=John" -F "file=@file.txt" http://example.com/upload
  ```

#### **2. Sending Data from a File**

Instead of including data inline with `-d`, you can read the data from a file:

```bash
curl -X POST -d @data.txt http://example.com/api
```

Here, `data.txt` contains the POST data.

- **For JSON:**
  ```bash
  curl -X POST -H "Content-Type: application/json" -d @data.json http://example.com/api
  ```

#### **3. Handling Cookies**

- **Sending Cookies:**
  You can include cookies with your request by using the `-b` option:

  ```bash
  curl -b "name=value" http://example.com
  ```

- **Save Cookies to a File:**
  You can save cookies to a file, which can be reused in later requests:

  ```bash
  curl -c cookies.txt http://example.com
  ```

- **Load Cookies from a File:**
  To use cookies from a previous session stored in `cookies.txt`:
  ```bash
  curl -b cookies.txt http://example.com
  ```

#### **4. FTP (File Transfer Protocol)**

- **Download File from FTP Server:**

  ```bash
  curl -u username:password ftp://ftp.example.com/file.txt -O
  ```

- **Upload File to FTP Server:**

  ```bash
  curl -u username:password -T file.txt ftp://ftp.example.com/upload/
  ```

- **List Files on FTP Server:**
  To list files on the FTP server without downloading them:
  ```bash
  curl -u username:password ftp://ftp.example.com/ --list-only
  ```

#### **5. Using Proxies**

You can configure `curl` to route your traffic through a proxy server.

- **Use HTTP Proxy:**

  ```bash
  curl -x http://proxy.example.com:8080 http://example.com
  ```

- **Use Proxy with Authentication:**

  ```bash
  curl -x http://proxy.example.com:8080 -U username:password http://example.com
  ```

- **Using SOCKS Proxy:**
  ```bash
  curl --socks5 socks5://proxy.example.com:1080 http://example.com
  ```

#### **6. Handling Redirects**

- **Follow Redirects (`-L`):**
  If the server returns a `3xx` redirect status, you can use the `-L` option to follow the redirect:

  ```bash
  curl -L http://example.com
  ```

- **Limit Redirects (`--max-redirs`):**
  You can limit the number of redirects `curl` follows:
  ```bash
  curl -L --max-redirs 5 http://example.com
  ```

#### **7. Verbose Output for Debugging (`-v` or `--verbose`)**

To see detailed information about the request and response, such as headers and data:

```bash
curl -v http://example.com
```

This is especially useful for debugging.

#### **8. Limiting Download Speed**

To limit the download speed (e.g., 500KB/s):

```bash
curl --limit-rate 500k -O http://example.com/largefile.zip
```

This helps control bandwidth usage.

#### **9. Sending Custom Headers**

You can send custom headers with your request using the `-H` option:

```bash
curl -H "Authorization: Bearer token" -H "Accept: application/json" http://example.com/api
```

#### **10. Timeout Settings**

- **Set Connection Timeout:**
  To set the maximum time allowed for connecting to the server:

  ```bash
  curl --connect-timeout 10 http://example.com
  ```

- **Set Total Timeout:**
  To set the maximum time allowed for the entire operation (connection + data transfer):
  ```bash
  curl --max-time 30 http://example.com
  ```

#### **11. Downloading Specific Byte Ranges**

If you want to download specific parts of a file, you can use the `-r` option:

```bash
curl -r 0-499 http://example.com/largefile.zip -O
```

This command downloads only the first 500 bytes of the file.

#### **12. HTTP Methods (GET, POST, PUT, DELETE, etc.)**

You can specify which HTTP method to use with `-X`:

- **GET:**

  ```bash
  curl -X GET http://example.com
  ```

- **PUT (for updating a resource):**

  ```bash
  curl -X PUT -d '{"key":"value"}' -H "Content-Type: application/json" http://example.com/api/resource
  ```

- **DELETE (for removing a resource):**
  ```bash
  curl -X DELETE http://example.com/api/resource
  ```

#### **13. Downloading Files with `-O` (Save File as Remote Name)**

To download files and save them with the same name as they have on the server:

```bash
curl -O http://example.com/file.zip
```

#### **14. Show Only Response Code**

If you want to only output the HTTP response code (useful for scripting):

```bash
curl -w "%{http_code}" -o /dev/null -s http://example.com
```

Here:

- `-o /dev/null`: Discards the body content.
- `-w "%{http_code}"`: Prints the HTTP status code.

#### **15. Using `curl` with HTTP/2 or HTTP/3**

- **Force HTTP/2:**

  ```bash
  curl --http2 https://example.com
  ```

- **Force HTTP/3 (QUIC):**
  ```bash
  curl --http3 https://example.com
  ```

#### **16. Debugging with `--trace` or `--trace-ascii`**

For very detailed output that includes all raw data sent and received:

- **Trace (binary):**

  ```bash
  curl --trace trace.txt http://example.com
  ```

- **Trace (ASCII):**
  ```bash
  curl --trace-ascii trace.txt http://example.com
  ```

This will dump the entire session, including headers and data, into a file (`trace.txt`).

#### **17. Using `curl` for API Testing (RESTful APIs)**

To test RESTful APIs, you can use `curl` with various methods (GET, POST, PUT, DELETE):

- **GET request to fetch data:**

  ```bash
  curl -H "Authorization: Bearer token" https://api.example.com/v1/resources
  ```

- **POST request to create a resource:**

  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"name":"New Resource"}' https://api.example.com/v1/resources
  ```

- **PUT request to update a resource:**

  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"name":"Updated Resource"}' https://api.example.com/v1/resources/1
  ```

- **DELETE request to remove a resource:**
  ```bash
  curl -X DELETE -H "Authorization: Bearer token" https://api.example.com/v1/resources/1
  ```

---

### **Examples of Complex `curl` Commands**

#### **1. Full Example: Upload File with Authentication and JSON Payload**

```bash
curl -X POST -H "Authorization: Bearer token" -H "Content-Type: multipart/form-data" \
-F "file=@file.txt" -F "metadata={\"description\":\"File upload\"}" \
https://example.com/upload
```

Here, a file and some JSON metadata are uploaded, using Bearer authentication.

#### **2. Fetch Data and Save Response Headers and Body Separately**

```bash
curl -D headers.txt -o response.html http://example.com
```

- `-D headers.txt`: Saves the response headers in `headers.txt`.
- `-o response.html`: Saves the body content in `response.html`.

#### **3. Perform Multiple Requests in Parallel with `curl` and `xargs`**

```bash
cat urls.txt | xargs -n 1 -P 4 curl -O
```

This command downloads multiple files concurrently (up to 4 at a time) from a list of URLs in `urls.txt`.

#### **4. Send a POST Request with a File from stdin**

```bash
curl -X POST -d @- http://example.com/api < data.txt
```

Here, data from `data.txt` is sent as a POST request, using standard input.

---

### **References and Resources**

- **curl Manual:** [curl Documentation](https://curl.se/docs/manual.html)
- **curl Command Line Help:** Run `man curl` or `curl --help` in your terminal for all options and detailed usage.

This guide covers advanced usage of `curl`, but there are still many more options available. Let me know if you'd like additional examples or explanations!

`curl` is another powerful command-line tool used for transferring data to or from a server using various network protocols, including HTTP, HTTPS, FTP, and others. It's widely used for interacting with web APIs, downloading/uploading files, and debugging network services. Below, I'll cover everything you need to know about `curl` commands, from basic usage to advanced options and practical examples.

---

## **1. Basic Syntax**

```
curl [options] [URL]
```

- **[options]**: Modify `curl`'s behavior.
- **[URL]**: The URL of the server you want to interact with (e.g., `https://example.com`).

---

## **2. Basic Commands**

### **A. Download a File**

To download a file using `curl`, you can specify the URL and use the `-O` option to save the file with the same name as the remote file.

```bash
curl -O https://example.com/file.zip
```

This will download the file `file.zip` from the specified URL and save it in the current directory.

### **B. Download a File with a Different Filename**

To download a file and specify a custom filename, use the `-o` option:

```bash
curl -o myfile.zip https://example.com/file.zip
```

This downloads the file and saves it as `myfile.zip` locally.

### **C. Download a File in the Background**

To download files in the background (so that the terminal isn’t blocked), you can use `&` to run the `curl` command in the background:

```bash
curl -O https://example.com/file.zip &
```

Alternatively, use `-s` (silent mode) to suppress output and avoid terminal clutter while downloading in the background.

### **D. Resume an Interrupted Download**

If the download gets interrupted, you can resume it by using the `-C -` option:

```bash
curl -C - -O https://example.com/largefile.zip
```

This resumes the download from where it left off, using the same filename (`largefile.zip`).

---

## **3. HTTP Request Methods**

### **A. Get Request (Default)**

By default, `curl` sends a **GET** request to the specified URL:

```bash
curl https://example.com
```

This retrieves the content of the URL and displays it in the terminal.

### **B. POST Request**

You can send a **POST** request to submit data to a server (commonly used for forms or API interactions). Use the `-d` flag followed by the data you want to send:

```bash
curl -X POST -d "name=John&age=30" https://example.com/form
```

This sends a POST request with the form data `name=John&age=30` to the specified URL.

### **C. Sending JSON Data with a POST Request**

When interacting with APIs, you often need to send JSON data in a POST request. Use the `-H` flag to set the `Content-Type` header to `application/json` and `-d` to send JSON data:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "John", "age": 30}' https://api.example.com/user
```

### **D. PUT Request**

For updating resources, you can use the `-X PUT` option to send a **PUT** request:

```bash
curl -X PUT -d '{"name": "John", "age": 31}' -H "Content-Type: application/json" https://api.example.com/user/1
```

This sends a PUT request to update the user's data on the server.

### **E. DELETE Request**

To delete a resource, use the `-X DELETE` option to send a **DELETE** request:

```bash
curl -X DELETE https://api.example.com/user/1
```

---

## **4. Sending Headers**

### **A. View Response Headers**

To view only the **HTTP response headers** from the server, use the `-I` (uppercase i) option:

```bash
curl -I https://example.com
```

This will display the headers returned by the server without downloading the body.

### **B. Send Custom Headers**

If you need to send custom headers (such as `Authorization` or `User-Agent`), use the `-H` flag:

```bash
curl -H "Authorization: Bearer my_token" https://api.example.com/resource
```

This sends a request with the `Authorization` header set to `Bearer my_token`.

### **C. Set User-Agent**

Some websites require a specific **User-Agent** string to be sent with the request. You can set this header with `-H`:

```bash
curl -H "User-Agent: Mozilla/5.0" https://example.com
```

---

## **5. Authentication**

### **A. Basic Authentication**

For basic authentication (i.e., username and password), use the `-u` option:

```bash
curl -u username:password https://example.com/protected-resource
```

This sends the `username:password` as part of the HTTP Basic Authentication.

### **B. Bearer Token Authentication**

For **Bearer Token** authentication (commonly used for APIs), you can use the `-H` flag to send the `Authorization` header:

```bash
curl -H "Authorization: Bearer your_token" https://api.example.com/data
```

---

## **6. Downloading Multiple Files**

### **A. Download Multiple Files**

You can download multiple files by providing multiple URLs:

```bash
curl -O https://example.com/file1.zip -O https://example.com/file2.zip
```

Alternatively, you can specify a text file containing URLs, one per line, and download all the files listed in the text file:

```bash
curl -O -K urls.txt
```

Where `urls.txt` contains:

```
https://example.com/file1.zip
https://example.com/file2.zip
```

### **B. Download Files in Parallel**

To download multiple files in parallel, you can use `xargs`:

```bash
cat urls.txt | xargs -n 1 -P 4 curl -O
```

This command will download all the files in `urls.txt` in parallel, up to 4 at a time.

---

## **7. Handling Timeouts and Retries**

### **A. Set Timeout**

To set a connection timeout or maximum download time, use the `--connect-timeout` and `--max-time` options:

```bash
curl --connect-timeout 10 --max-time 60 https://example.com
```

This sets a 10-second connection timeout and a 60-second maximum download time.

### **B. Retry Failed Requests**

To retry a request if it fails, use the `--retry` option:

```bash
curl --retry 5 https://example.com/file.zip
```

This will retry the download up to 5 times if it fails.

---

## **8. SSL/TLS and Security Options**

### **A. Disable SSL Verification**

Sometimes you may encounter SSL certificate issues (self-signed certificates, etc.). Use the `-k` or `--insecure` option to ignore SSL verification:

```bash
curl -k https://example.com
```

This tells `curl` to not validate SSL certificates, which may be useful for testing or interacting with internal services.

### **B. Specify a Certificate**

To use a specific SSL certificate when making a request, use the `--cert` option:

```bash
curl --cert mycert.pem https://example.com
```

### **C. View SSL/TLS Details**

To view the SSL/TLS handshake and certificate information, use the `-v` (verbose) option:

```bash
curl -v https://example.com
```

This will show detailed information about the request, including SSL certificate details.

---

## **9. Advanced Features**

### **A. Following Redirects**

If a URL returns a redirect (e.g., 301 or 302), use the `-L` option to follow the redirect:

```bash
curl -L https://example.com/redirect
```

This will automatically follow the redirect and download the final resource.

### **B. Limit Download Speed**

To limit the download speed, use the `--limit-rate` option:

```bash
curl --limit-rate 500k -O https://example.com/largefile.zip
```

This will limit the download speed to 500 KB/s.

### **C. Upload a File**

To upload a file to a server using `curl`, use the `-F` option for a form submission (similar to how a form would submit a file):

```bash
curl -F "file=@localfile.txt" https://example.com/upload
```

This uploads the file `localfile.txt` to the server under the form field `file`.

### **D. Upload a File with PUT**

You can use a **PUT** request to upload a file to a server:

```bash
curl -X PUT --data-binary @file.txt https://example.com/upload
```

This sends the contents of `file.txt` to the server.

---

## **10. Debugging and Verbose Output**

### **A. Verbose Output**

For debugging or understanding how `curl` works behind the scenes, use the `-v` (verbose) option:

```bash
curl -v https://example.com
```

This provides detailed output of the request, including headers and SSL information.

### **B. Silent Mode**

If you want to suppress all output (including progress and error messages), use the `-s` option:

```

bash
curl -s https://example.com > output.txt
```

This will download the file silently and save it to `output.txt`.

---

## **Summary of Key `curl` Options**

| Option                   | Description                                                 |
| ------------------------ | ----------------------------------------------------------- |
| `-O`                     | Save the file with the same name as the remote file.        |
| `-o <filename>`          | Save the file with a custom filename.                       |
| `-L`                     | Follow redirects.                                           |
| `-I`                     | Show only HTTP headers.                                     |
| `-X <method>`            | Specify HTTP method (e.g., `POST`, `GET`, `PUT`, `DELETE`). |
| `-d <data>`              | Send data with a POST request.                              |
| `-H <header>`            | Set custom headers.                                         |
| `-u <username:password>` | HTTP Basic Authentication.                                  |
| `-F <field@file>`        | Upload a file (form submission).                            |
| `-v`                     | Verbose output (for debugging).                             |
| `-s`                     | Silent mode (no progress or error output).                  |
| `-k`                     | Ignore SSL certificate verification.                        |
| `--retry <num>`          | Retry failed requests up to `num` times.                    |
| `--limit-rate <speed>`   | Limit download/upload speed.                                |
| `-C -`                   | Resume an interrupted download.                             |
| `-T <file>`              | Upload a file with a PUT request.                           |

---

### **Conclusion**

`curl` is an extremely flexible and powerful tool for working with URLs and interacting with web servers. Whether you’re downloading files, sending data, or debugging web requests, `curl` can handle a wide variety of tasks. Its rich set of options makes it a go-to tool for developers, system administrators, and anyone working with network protocols.

Let me know if you need more details on any specific command or have additional questions!
