import React, { useState } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import LoginPage from "./LoginPage";
import HomePage from "./HomePage";


function App() {
    return(
        <div>
            Yay you can see this change!
        </div>
    )
    // const [accessLevel, setAccessLevel] = useState("");
    //
    // // Maybe add the below access logic onto the backend to prevent against broken access control attacks.
    // if (accessLevel === "" || accessLevel === "invalid") {
    //     return (<LoginPage setAccessLevel={setAccessLevel}/>);
    // } else {
    //     return (<HomePage accessLevel={accessLevel} setAccessLevel={setAccessLevel}/>);
    // }
}

export default App;