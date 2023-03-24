import { Link } from "react-router-dom";

const Header = () => {
    return (
        <Link to="/" >
            <div className="app-header">           
                <h1>My Notes</h1>           
            </div>
        </Link>
    )
}

export default Header;