import React from "react";
import "./header.css"


function Header(){
    return (
        <div className = "header">
            <h1>New York Customs</h1>
            <img className ="headerImg" src = "https://cdn.discordapp.com/attachments/1089204086718611576/1090366014799216690/New_York_3.png" alt = "logo" />
            <h2> We buy and sell cars </h2>
        </div>
    )
}

export default Header;