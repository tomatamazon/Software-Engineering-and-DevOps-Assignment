import React, { useState } from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import LoginPage from './LoginPage';
import HomePage from './HomePage';

function App() {

    // const accessLevel = "";
    //
    // const setAccessLevel = (userPerms) => {
    //     console.log("userPerms is", userPerms)
    // };
    
    const [accessLevel, setAccessLevel] = useState("");

    // Maybe add the below access logic onto the backend to prevent against broken access control attacks.
    if (accessLevel === "" || accessLevel === "invalid") {
        // return (<LoginPage setAccessLevel={setAccessLevel}/>);
        // return (<LoginPage accessLevel={accessLevel} setAccessLevel={setAccessLevel} />);
        return (
            <div>
                <p>Hi Marcel</p>
            </div>
        )
    } else {
        return (<HomePage accessLevel={accessLevel} setAccessLevel={setAccessLevel}/>);
    };
}

export default App;