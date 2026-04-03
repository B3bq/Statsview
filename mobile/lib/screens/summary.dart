import 'package:flutter/material.dart';

class SummaryScreen extends StatelessWidget {
  final String name;
  final String email;
  final String country;
  final VoidCallback onback;

  const SummaryScreen({
    required this.name,
    required this.email,
    required this.country,
    required this.onback,
  });

  @override
  Widget build(BuildContext context) {
    return SafeArea(
        child:
          SingleChildScrollView(
            child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              IconButton(
                icon: Icon(Icons.arrow_back),
                onPressed: onback,
              ),
              SizedBox(height: 16),
              Text('Name: $name', style: TextStyle(fontSize: 18)),
              SizedBox(height: 8),
              Text('Email: $email', style: TextStyle(fontSize: 18)),
              SizedBox(height: 8),
              Text('Country: $country', style: TextStyle(fontSize: 18)),
            ],
          ),
          )
      );
  }
}