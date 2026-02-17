import React, { useState } from 'react';
import axios from 'axios';
import FraudAlert from './FraudAlert';

function Dashboard() {
    const [transaction, setTransaction] = useState({});
    const [fraudResult, setFraudResult] = useState(null);

    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setTransaction({ ...transaction, [name]: value });
    };

    const handleSubmit = async () => {
        try {
            const response = await axios.post('http://localhost:8000/predict', { transaction_data: transaction });
            setFraudResult(response.data.is_fraud);
        } catch (error) {
            console.error('Error:', error);
        }
    };

    return (
        <div>
            <h2>Transaction Input</h2>
            <form>
                <input type="text" name="amount" placeholder="Amount" onChange={handleInputChange} />
                <input type="text" name="location" placeholder="Location" onChange={handleInputChange} />
                <button type="button" onClick={handleSubmit}>Submit</button>
            </form>
            {fraudResult !== null && <FraudAlert isFraud={fraudResult} />}
        </div>
    );
}

export default Dashboard;