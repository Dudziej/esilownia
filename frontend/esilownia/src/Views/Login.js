import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import LoginForm from "../components/Login/Login_form"

function Login() {

  return (
    <div className="Login">
      <div class="container">
        <div class="row d-flex justify-content-center my-5">
            <LoginForm></LoginForm>
        </div>
      </div>
    </div>
  );
}

export default Login;
