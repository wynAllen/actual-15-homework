<!DOCTYPE html>
<html class="">
  <head>
    <meta charset="utf-8">
    <title>Account Management</title>
    <meta name="viewport" content="width=device-width">
    <meta name="description" content="">
    <link rel="icon" href="http://www.51reboot.com/images/favicon.ico">
  </head>
  <body>
    <div id="container">
      <div id="tip" class=" notification">
        <p>
          
        </p>
      </div>
      <div id="body">
          <link rel="stylesheet" href="{{url_for('static', filename='login.css')}}">

<div id="login-register-page" class="form-container register">
  <div class="tabs register">
    <a class="tab register" href="/register/">
      <span>New to JS Bin</span>
      Register
    </a>
    <a class="tab login" href="/login">
      <span>Existing users</span>
      Login
    </a>
  </div>
  <div class="info "><p></p></div>
  <form action="/register/" method="post" class="register">
    <div>
      <label for="signup-username">Username</label>
      <input name="username" id="signup-username" type="text" required pattern="[a-zA-Z0-9_\-]+" oninput="setCustomValidity('')" oninvalid="setCustomValidity('Only numbers, letters, underscore and dash are allowed in the username')">
    </div>
    <div>
      <label for="signup-passwd">Password</label>
      <input name="password" id="signup-key" type="password" required>
    </div>
    <div>
      <label for="signup-gender">Gender</label>
      <input name="sex" id="signup-key" type="text" placeholder="0:female 1:male" required>
    </div>
    <div>
      <label for="signup-age">Age</label>
      <input name="age" id="signup-key" type="text" required pattern="[0-9]{1,3}" oninput="setCustomValidity('')" oninvalid="setCustomValidity('Only numbers are allowed in the age')">
    </div>
    <div>
      <label for="signup-phone">Phone</label>
      <input name="phone" id="signup-key" type="text" required>
    </div>
    <div>
      <label for="signup-email">Email address</label>
      <input name="email" id="signup-email" type="email" required>
    </div>
    <div>
      <label for="signup-role">Role</label>
      <input name="role" id="signup-key" type="text" placeholder="0:admin 1:user" required>
    </div>
    <div class="submit">
      <input type="submit" value="Register">
    </div>    
    <span style='color:red'>{{ res['msg'] }}</span>
  </form>

  <form action="https://jsbin.com/login" method="post" class="login" id="login">
    <div>
      <label for="login-username">Email address or username</label>
      <input name="username" id="login-username" type="text" required value="">
    </div>
    <div>
      <label for="login-key">Password</label>
      <input name="key" id="login-key" type="password" required>
    </div>
    <div class="submit">
      <input type="submit" value="Log in">
      <a id="lostpass" class="lostpass" href="https://jsbin.com/forgot">I've forgotten my password</a>
    </div>    <input type="hidden" name="_csrf" value="48W9ht9e-m5js8pZsqL4NmE0qaUzUNHFblLs">
    <input type="hidden" name="referrer" value="">
  </form>

</div>


  </body>
</html>