import React from "react";
import { Link } from "react-router-dom"
import "./nav.css"



function Nav(){

    const linkStyle = {
        textDecoration: "none"
    }




    return (
        <div classname = "nav">
            <Link className ='AboutMe' to="/" style={linkStyle}><button>Home</button></Link>
            <Link className ='BuyCars' to="/cars" style={linkStyle}><button>Buy Cars</button></Link>
            <Link className ='SellCars' to="/SellCars" style={linkStyle}><button>Sell Cars</button></Link>
            {/* <Link className ='AboutMe' to="/" style={linkStyle}>About me</Link>
            <Link className ='BuyCars' to="/Cars" style={linkStyle}>Buy Cars</Link>
            <Link className ='SellCars' to="/SellCars" style={linkStyle}>Sell Cars</Link> */}
        </div>
    )
}

export default Nav;