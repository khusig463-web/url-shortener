function copyURL() {

    const url = document.getElementById("shortUrl");

    navigator.clipboard.writeText(url.value);

    alert("Short URL copied!");
}