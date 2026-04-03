import 'package:flutter/material.dart';
import 'package:mobile/screens/actions.dart';
import 'package:mobile/screens/summary.dart';
import 'package:mobile/screens/profile.dart';

class BottomMenu extends StatefulWidget {
  const BottomMenu({super.key});

  @override
  _BottomMenuState createState() => _BottomMenuState();
}

class _BottomMenuState extends State<BottomMenu> {
    int _currentIndex = 1; // Active index for the bottom navigation bar

    // List of screens corresponding to each tab in the bottom navigation bar
    late final List<Widget> _screens;

    @override
    void initState() {
      super.initState();
      _screens = [
        ProfileScreen(),
        ActionsScreen(
          onNavigateToSummary: (index) {
            setState(() {
              _currentIndex = index;
            });
          },
        ),
        SummaryScreen(name: 'seba', email: 'sdada', country: 'Polska', onback: () {
          setState(() {
            _currentIndex = 0; // Navigate back to the Profile screen
          });
        }),
      ];
    }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body:
      IndexedStack(
        index: _currentIndex,
        children: _screens,
      ),
      bottomNavigationBar: BottomNavigationBar(
        currentIndex: _currentIndex,
        onTap: (index) {
          setState(() {
            _currentIndex = index;
          });
        },
        items: const[
          BottomNavigationBarItem(icon: Icon(Icons.person), label: 'Profile'),
          BottomNavigationBarItem(icon: Icon(Icons.add_circle), label: 'Actions'),
          BottomNavigationBarItem(icon: Icon(Icons.settings), label: 'Settings'),
        ],
        backgroundColor: Colors.green,
        selectedItemColor: Colors.white,
        unselectedItemColor: Colors.white70,
      ),
    );
  }
}