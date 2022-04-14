import React, { Component } from "react";
import {Route, Routes } from "react-router-dom";
import Home from "./components/Home";
import Signup from "./components/signup/Signup";
import Login from "./components/login/Login";
import Homepage from "./components/homepage/Homepage";
import Root from "./Root";

class App extends Component {
  render() {
    return (
      <div>
        <Root>
          <Routes>
            <Route path="/signup" element={<Signup/>}/>
            <Route path="/login" element={<Login/>}/>
            <Route path="/homepage" element={<Homepage/>}/>
            <Route exact path="/" element={<Home/>}/>
          </Routes>
        </Root>
      </div>
    );
  }
}

export default App;
