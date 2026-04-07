import 'package:flutter/material.dart';
import 'package:mobile/widgets/button.dart';
import 'package:mobile/widgets/input.dart';

class ProfileScreen extends StatelessWidget {
  final emailController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return SafeArea(
        child:
        SingleChildScrollView(
          child:
            Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Padding(
                    padding: const EdgeInsets.fromLTRB(16, 100, 16, 0),
                    child: Column(
                      children: [
                        CircleAvatar(
                          radius: 50,
                          backgroundImage: AssetImage('assets/profile.jpg'), // Replace with your profile image
                        ),
                        SizedBox(height: 16),
                        Text('John Doe', style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold)),
                        SizedBox(height: 8),
                        Input(controller: emailController, label: 'Email'),
                        TextFormField(
                          obscureText: true,
                          decoration: const InputDecoration(
                            labelText: 'Password',
                          ),
                        ),
                      ],
                    )
                )
              ],
          ),
        )
     );
  }
}