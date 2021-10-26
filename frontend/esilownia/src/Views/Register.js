import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
import RegisterForm from "../components/Register/Register_form"

function Register() {

  return (
    <div className="Register">
      <div class="container">
        <div class="row d-flex justify-content-center my-5">
            <RegisterForm></RegisterForm>
        </div>
      </div>
    </div>
  );
}

export default Register;
