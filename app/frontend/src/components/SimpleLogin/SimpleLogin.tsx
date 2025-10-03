import React, { useState, useContext } from "react";
import { DefaultButton, TextField, MessageBar, MessageBarType } from "@fluentui/react";
import { useTranslation } from "react-i18next";
import { LoginContext } from "../../loginContext";
import styles from "./SimpleLogin.module.css";

export const SimpleLogin = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");
    const { setLoggedIn } = useContext(LoginContext);
    const { t } = useTranslation();

    const handleLogin = () => {
        if (username === "demo" && password === "Offix2025!") {
            setLoggedIn(true);
            setError("");
        } else {
            setError("Invalid username or password");
        }
    };

    const handleKeyPress = (e: React.KeyboardEvent) => {
        if (e.key === "Enter") {
            handleLogin();
        }
    };

    return (
        <div className={styles.loginContainer}>
            <div className={styles.loginCard}>
                <h2 className={styles.title}>Login</h2>
                {error && (
                    <MessageBar messageBarType={MessageBarType.error} className={styles.errorMessage}>
                        {error}
                    </MessageBar>
                )}
                <div className={styles.form}>
                    <TextField
                        label="Username"
                        value={username}
                        onChange={(_, newValue) => setUsername(newValue || "")}
                        onKeyPress={handleKeyPress}
                        className={styles.input}
                    />
                    <TextField
                        label="Password"
                        type="password"
                        value={password}
                        onChange={(_, newValue) => setPassword(newValue || "")}
                        onKeyPress={handleKeyPress}
                        className={styles.input}
                    />
                    <DefaultButton
                        text="Login"
                        onClick={handleLogin}
                        className={styles.loginButton}
                    />
                </div>
            </div>
        </div>
    );
};

