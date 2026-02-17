import React from 'react';

function FraudAlert({ isFraud }) {
    return (
        <div>
            {isFraud ? (
                <p style={{ color: 'red' }}>Fraudulent Transaction Detected!</p>
            ) : (
                <p style={{ color: 'green' }}>Transaction is Legitimate.</p>
            )}
        </div>
    );
}

export default FraudAlert;