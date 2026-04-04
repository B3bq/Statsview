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

    Widget _buildItem(IconData icon, String label, int index) {
      final isSelected = _currentIndex == index;

      return AnimatedContainer(
        duration: const Duration(milliseconds: 250),
        padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
        decoration: BoxDecoration(
          color: isSelected ? Colors.white.withOpacity(0.2) : Colors.transparent,
          borderRadius: BorderRadius.circular(16),
        ),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              icon,
              color: isSelected ? Colors.white : Colors.white70,
            ),
            const SizedBox(height: 4),
            Text(
              label,
              style: TextStyle(
                fontSize: 12,
                color: isSelected ? Colors.white : Colors.white70,
                fontWeight: isSelected ? FontWeight.bold : FontWeight.normal,
              ),
            ),
          ],
        ),
      );
    }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body:
      IndexedStack(
        index: _currentIndex,
        children: _screens,
      ),
      bottomNavigationBar: Theme(
        data: Theme.of(context).copyWith(
          splashFactory: NoSplash.splashFactory,
          splashColor: Colors.transparent,
          highlightColor: Colors.transparent,
        ),
        child: BottomNavigationBar(
          currentIndex: _currentIndex,
          onTap: (index) {
            setState(() {
              _currentIndex = index;
            });
          },
          items: [
            BottomNavigationBarItem(icon: _buildItem(Icons.account_circle, 'Profile', 0), label: 'Profile'),
            BottomNavigationBarItem(icon: _buildItem(Icons.add_circle, 'Actions', 1), label: 'Actions'),
            BottomNavigationBarItem(icon: _buildItem(Icons.settings, 'Settings', 2), label: 'Settings'),
          ],
          backgroundColor: Colors.green.shade600,
          elevation: 10,
          selectedItemColor: Colors.white,
          unselectedItemColor: Colors.white70,
          showSelectedLabels: false,
          showUnselectedLabels: false,
          type: BottomNavigationBarType.fixed,
        ),
      )
    );
  }
}