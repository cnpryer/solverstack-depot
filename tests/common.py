from app import __version__

from typing import List


ENDPOINT: str = f"/api/{__version__}/depot"
REQUEST_TYPES: List[str] = [
    "audio/aac",
    "application/x-abiword",
    "application/x-freearc",
    "video/x-msvideo",
    "application/vnd.amazon.ebook",
    "application/octet-stream",
    "image/bmp",
    "application/x-bzip",
    "application/x-bzip2",
    "application/x-csh",
    "text/css",
    "text/csv",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "application/vnd.ms-fontobject",
    "application/epub+zip",
    "application/gzip",
    "image/gif",
    "text/html",
    "image/vnd.microsoft.icon",
    "text/calendar",
    "application/java-archive",
    "image/jpeg",
    "text/javascript, per the following specifications:",
    "audio/midi",
    "text/javascript",
    "audio/mpeg",
    "video/mpeg",
    "application/vnd.apple.installer+xml",
    "application/vnd.oasis.opendocument.presentation",
    "application/vnd.oasis.opendocument.spreadsheet",
    "application/vnd.oasis.opendocument.text",
    "audio/ogg",
    "video/ogg",
    "application/ogg",
    "audio/opus",
    "font/otf",
    "image/png",
    "application/pdf",
    "application/x-httpd-php",
    "application/vnd.ms-powerpoint",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "application/vnd.rar",
    "application/rtf",
    "application/x-sh",
    "image/svg+xml",
    "application/x-shockwave-flash",
    "application/x-tar",
    "image/tiff",
    "video/mp2t",
    "font/ttf",
    "text/plain",
    "application/vnd.visio",
    "audio/wav",
    "audio/webm",
    "video/webm",
    "image/webp",
    "font/woff",
    "font/woff2",
    "application/xhtml+xml",
    "application/vnd.ms-excel",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/xml ",
    "application/vnd.mozilla.xul+xml",
    "application/zip",
    "video/3gpp",
    "video/3gpp2",
    "application/x-7z-compressed",
]
