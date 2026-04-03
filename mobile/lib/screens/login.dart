import 'dart:async';

import 'package:flutter/material.dart';
import 'package:mobile/screens/bottomMenu.dart';
import '../widgets/button.dart';
import '../widgets/input.dart';

import 'home.dart';

class LoginScreen extends StatelessWidget {
  final emailController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Login")),
      body: SingleChildScrollView(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            Input(controller: emailController, label: 'Email'),
            TextFormField(
              obscureText: true,
              decoration: const InputDecoration(
                labelText: 'Password',
              ),
            ),
            SizedBox(height: 16),
            Button(
              text: 'Zaloguj',
              onPressed: () {
                Navigator.pushReplacement(
                  context,
                  MaterialPageRoute(builder: (context) => BottomMenu()),
                );
              },
            ),
          ],
        ),
      ),
    );
  }
}