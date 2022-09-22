import React, {useState} from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import LoginPage from './LoginPage';
import HomePage from './HomePage';

function App() {

    const [accessLevel, setAccessLevel] = useState("");

    if (accessLevel === "" || accessLevel === "invalid") {
        return (<LoginPage setAccessLevel={setAccessLevel}/>);
    } else {
        return (<HomePage setAccessLevel={setAccessLevel} accessLevel={accessLevel}/>);
    };
}

export default App;