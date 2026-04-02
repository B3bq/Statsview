import 'package:flutter/material.dart';
import '../widgets/button.dart';
import '../widgets/input.dart';

import 'home.dart';

class LoginScreen extends StatelessWidget {
  final emailController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Login")),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            Input(controller: emailController, label: 'Email'),
            SizedBox(height: 16),
            Button(text: 'Zaloguj', onPressed: () {
              // Tu można dodać logikę logowania
              Navigator.pushReplacement(context, MaterialPageRoute(builder: (context) => HomeScreen()));
            }
            ),
          ],
        ),
      ),
    );
  }
}