import 'package:flutter/material.dart';
import 'package:mobile/widgets/dropdown.dart';

class AddingScreen extends StatelessWidget {
  final List<String> items = ['Football', 'Basketball', 'Volleyball', 'Handball', 'Counter-Strike', 'League of Legends'];
  final VoidCallback onback;

  AddingScreen({required this.onback});

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child:
        SingleChildScrollView(
          child: Column(
              children: [
                IconButton(
                  icon: Icon(Icons.arrow_back),
                  onPressed: onback,
                ),
                Text('Add From Existing'),
                Dropdown(items: items, value: 'Football', onChanged: (String? newValue) {
                  print('Selected: $newValue');
                // Handle dropdown value change
                }),
              ],
          ),
      ),
    );
  }
}