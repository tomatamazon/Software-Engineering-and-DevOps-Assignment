import React, { useState } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import LoginPage from './LoginPage';
import HomePage from './HomePage';

function App() {

    const [accessLevel, setAccessLevel] = useState("");

    const setAccessLevelFunc = (userPerms) => {
        console.log("userPerms is", userPerms)
        console.log(typeof(userPerms))
        console.log(typeof(accessLevel))
        setAccessLevel(userPerms)
    };

    // Maybe add the below access logic onto the backend to prevent against broken access control attacks.
    if (accessLevel === "" || accessLevel === "invalid") {
        // return (<LoginPage setAccessLevel={setAccessLevel}/>);
        return (<LoginPage accessLevel={accessLevel} setAccessLevel={setAccessLevel} setAccessLevelFunc={setAccessLevelFunc} />);
    } else {
        return (<HomePage accessLevel={accessLevel} setAccessLevel={setAccessLevel}/>);
    };
}

export default App;