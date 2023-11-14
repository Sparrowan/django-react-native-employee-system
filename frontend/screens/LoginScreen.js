// LoginScreen.js
import React, { useState } from 'react';
import { View, TextInput, Button, AsyncStorage } from 'react-native';

const LoginScreen = ({ navigation }) => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    // Implement your authentication logic here
    // On successful login, save the token in AsyncStorage
    const token = 'YOUR_AUTH_TOKEN'; // Replace this with the actual token
    await AsyncStorage.setItem('token', token);
    navigation.navigate('Home');
  };

  return (
    <View>
      <TextInput
        placeholder="Username"
        value={username}
        onChangeText={(text) => setUsername(text)}
      />
      <TextInput
        placeholder="Password"
        secureTextEntry
        value={password}
        onChangeText={(text) => setPassword(text)}
      />
      <Button title="Login" onPress={handleLogin} />
    </View>
  );
};

export default LoginScreen;
