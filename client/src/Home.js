import React from "react";
import './Home.css';
import { Link } from "react-router-dom"

function Home(){
    
    return (
        <div>
            {/* <h1>Welcome To New York Customs</h1> */}
            <div className ="bg1">
                <img src = 'https://cdn.discordapp.com/attachments/1089204086718611576/1091061555162009680/New_York_Customs_5.png'/>
                <img src = 'https://cdn.discordapp.com/attachments/1089204086718611576/1091036479666540554/New_York_Customs_1.png'/>
                <img src = 'https://cdn.discordapp.com/attachments/1089204086718611576/1091036549052911667/New_York_Customs_2.png'/>
                <img src = 'https://cdn.discordapp.com/attachments/1089204086718611576/1091036608893026414/New_York_Customs_3.png'/>
                <img src = 'https://cdn.discordapp.com/attachments/1089204086718611576/1091036698483372122/New_York_Customs_4.png'/>
            </div>
        </div>
    )
}

export default Home;