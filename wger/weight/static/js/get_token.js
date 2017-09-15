var url = window.location.href;
var origin = window.location.origin;

try {
    var accessToken = url.split("#")[1].split("=")[1].split("&")[0];
    window.location.replace(origin + "/en/weight/fitbit/" + accessToken);
} catch (err) {
    console.log(err);
}
