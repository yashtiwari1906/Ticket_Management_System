import { useNavigate, Link } from 'react-router-dom';
import Base from "../core/Base";

const Booked = () =>{

    const navigate = useNavigate();

    const toHome = () =>{
        navigate("/");
    }


    return(
        <Base title = "Confirmation Page" description = "Your Ticket has been booked succesfully, Go back to home page">
            <button onClick={toHome} className="btn btn-success offset-sm-6 btn-block">Home</button>
        </Base>
    )
}



export default Booked;