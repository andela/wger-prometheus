var url = window.location.href;

try{
    var access_token = url.split('#')[1].split('=')[1].split('&')[0];
    var origin = window.location.origin;
    window.location.replace(origin + '/en/weight/fitbit/' + access_token);
} catch(err){
    console.log(err);
}




