import 'package:flutter/material.dart';
import 'package:mobile/widgets/dropdown.dart';

class AddingScreen extends StatelessWidget {
  final List<String> items = ['Football', 'Basketball', 'Volleyball', 'Handball', 'Counter-Strike', 'League of Legends'];
  final VoidCallback onback;

  AddingScreen({required this.onback});

  @override
  Widget build(BuildContext context) {
    return SafeArea(
      child: Stack(
        children: [
          Positioned(
            top: 16,
            left: 16,
            child: IconButton(
              icon: Icon(Icons.arrow_back),
              onPressed: onback,
            ),
          ),

          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 24.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                SizedBox(height: 80),

                Text(
                  'Add From Existing',
                  textAlign: TextAlign.center,
                  style: TextStyle(fontSize: 18),
                ),

                SizedBox(height: 24),

                DropdownButtonFormField<String>(
                  value: 'Football',
                  isExpanded: true,
                  items: items.map((item) {
                    return DropdownMenuItem(
                      value: item,
                      child: Text(item),
                    );
                  }).toList(),
                  onChanged: (newValue) {
                    print('Selected: $newValue');
                  },
                  icon: Icon(Icons.arrow_drop_down),
                ),

                SizedBox(height: 16),

                DropdownButtonFormField<String>(
                  value: 'Basketball',
                  isExpanded: true,
                  items: items.map((item) {
                    return DropdownMenuItem(
                      value: item,
                      child: Text(item),
                    );
                  }).toList(),
                  onChanged: (newValue) {},
                  icon: Icon(Icons.arrow_drop_down),
                ),

                SizedBox(height: 16),

                DropdownButtonFormField<String>(
                  value: 'Volleyball',
                  isExpanded: true,
                  items: items.map((item) {
                    return DropdownMenuItem(
                      value: item,
                      child: Text(item),
                    );
                  }).toList(),
                  onChanged: (newValue) {},
                  icon: Icon(Icons.arrow_drop_down),
                ),

                SizedBox(height: 32),

                ElevatedButton(
                  onPressed: () {},
                  child: Text("Add"),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}