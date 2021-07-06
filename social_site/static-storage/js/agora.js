function reply() {
    //Disable submit button if there is no message in the reply form
    if(document.getElementById("content").value==="") {
      document.getElementById('reply-button').disabled = true;
    }
    else {
      document.getElementById('reply-button').disabled = false;
    }
  }

function display_discussions(){
  //Turn active the discussions tab and display matches in discussions
  document.getElementById("search-discussions").classList.add('select');
  document.getElementById("search-posts").classList.remove('select');
  document.getElementById("search-users").classList.remove('select');
  document.getElementById("discussions").classList.remove('d-none');
  document.getElementById("posts").classList.add('d-none');
  document.getElementById("users").classList.add('d-none');
}

function display_posts(){
  //Turn active the post tab and display matches in post
  document.getElementById("search-posts").classList.add('select');
  document.getElementById("search-discussions").classList.remove('select');
  document.getElementById("search-users").classList.remove('select');
  document.getElementById("posts").classList.remove('d-none');
  document.getElementById("discussions").classList.add('d-none');
  document.getElementById("users").classList.add('d-none');
}

function display_users(){
  //Turn active the users tab and display matches in users
  document.getElementById("search-users").classList.add('select');
  document.getElementById("search-discussions").classList.remove('select');
  document.getElementById("search-posts").classList.remove('select');
  document.getElementById("users").classList.remove('d-none');
  document.getElementById("discussions").classList.add('d-none');
  document.getElementById("posts").classList.add('d-none');
}