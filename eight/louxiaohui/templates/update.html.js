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
      </div>
      <div id="body">
          <link rel="stylesheet" href="{{url_for('static', filename='login.css')}}">
<div id="login-register-page" class="form-container register">

  <div class="tabs register">
    <a class="tab register" href="/userlist">
        <br>
        <span>back to userlist page</span>
    </a>
  </div>

  <div class="info "><p></p></div>

  <form action="/update_user" method="post" class="register">
    <div>
      <label for="signup-username">Username</label>
      <input name="username" id="signup-username" type="text" value="{{ data.username }}" required pattern="[a-zA-Z0-9_\-]+" oninput="setCustomValidity('')" oninvalid="setCustomValidity('Only numbers, letters, underscore and dash are allowed in the username')">
    </div>
    <div>
      <label for="signup-passwd">Password</label>
      <input name="password" id="signup-passwd" type="password" required>
    </div>
    <div>
      <label for="signup-passwd">Input Password again</label>
      <input name="repwd" id="signup-key" type="password" required>
    </div>
    <div>
      <label for="signup-sex">Gender</label>
      <input name="sex" id="signup-key" type="text" value="{{ data.sex }}" required>
    </div>
    <div>
      <label for="signup-age">Age</label>
      <input name="age" id="signup-key" type="text" value="{{ data.age }}" required pattern="[0-9]{1,3}" oninput="setCustomValidity('')" oninvalid="setCustomValidity('Only numbers are allowed in the age')">
    </div>
    <div>
      <label for="signup-phone">Phone</label>
      <input name="phone" id="signup-key" type="text" value="{{ data.phone }}" required>
    </div>
    <div>
      <label for="signup-email">Email address</label>
      <input name="email" id="signup-email" type="email" value="{{ data.email }}" required>
    </div>
    <div>
      <label for="signup-role">Role</label>
      <input name="role" id="signup-key" type="text" value="{{ data.role }}" required>
    </div>
    <div class="submit">
      <input type="submit" value="Confirm">
    </div>    
    <span style='color:red'>{{ res['msg'] }}</span>
    <input type="hidden" name="_csrf" value="48W9ht9e-m5js8pZsqL4NmE0qaUzUNHFblLs">
    <input type="hidden" name="referrer" value="">
  </form>

  </body>
</html>