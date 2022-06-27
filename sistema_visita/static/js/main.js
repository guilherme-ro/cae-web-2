const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function() {
  $('#message').fadeOut('slow');
}, 3000);

mybutton = document.getElementById("myBtn");

window.onscroll = function() {
  scrollFunction()
};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

/*function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}*/

$('#myBtn').on("click", function (e) {

  e.preventDefault();

  const href = $(this).attr("href");
  
  $("html, body").animate({ scrollTop: $(href).offset().top }, 800);
});

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function handleCredentialResponse(response) {
  const data = jwt_decode(response.credential)
  //console.log(data.given_name);
  
    axios.post('google', data) // 4
     .then(res => {
        //var message = res
        //console.log(data);
        //console.log(message);
        window.location.replace('dashboard');
    })
     .catch(errors => console.log(errors)) // 6

}

window.onload = function () {
  google.accounts.id.initialize({
    client_id: "572685342659-m5dqrbotcgktnoqrcluogvj09v8bmjb4.apps.googleusercontent.com",
    callback: handleCredentialResponse
  });

  google.accounts.id.renderButton(
    document.getElementById("buttonDiv"),
    { theme: "outline", size: "large" }  // customization attributes
  );
  google.accounts.id.prompt(); // also display the One Tap dialog
}


