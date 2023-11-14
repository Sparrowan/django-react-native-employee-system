// HomeScreen.js
import React, { useEffect, useState } from 'react';
import { View, Text, Button, AsyncStorage } from 'react-native';

const HomeScreen = ({ navigation }) => {
  const [username, setUsername] = useState('');

  useEffect(() => {
    // Fetch user details or data from AsyncStorage
    const getUserData = async () => {
      const token = await AsyncStorage.getItem('token');
      // Make an API call to fetch user details using the token
      // Example:
      // const user = await fetchUserData(token);
      // setUsername(user.username);
    };

    getUserData();
  }, []);

  const handleLogout = async () => {
    // Remove token from AsyncStorage on logout
    await AsyncStorage.removeItem('token');
    navigation.navigate('Login');
  };

  return (
    <View>
      <Text>Welcome, {username}</Text>
      <Button title="Logout" onPress={handleLogout} />
    </View>
  );
};

export default HomeScreen;
