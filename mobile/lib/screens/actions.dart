import 'package:flutter/material.dart';
import 'package:mobile/widgets/button.dart';
import 'package:mobile/screens/adding.dart';
import 'package:mobile/screens/summary.dart';

enum ActionView { menu, adding, summary }

class ActionsScreen extends StatefulWidget {
  final Function(int) onNavigateToSummary;

  const ActionsScreen({required this.onNavigateToSummary});

  @override
  State<ActionsScreen> createState() => _ActionsScreenState();
}

class _ActionsScreenState extends State<ActionsScreen> {
  ActionView currentView = ActionView.menu;

  @override
  Widget build(BuildContext context) {
    switch (currentView) {
      case ActionView.menu:
        return _buildMenu();
      case ActionView.adding:
        return AddingScreen(onback: (){
          setState(() {
            currentView = ActionView.menu;
          });
        },);
      case ActionView.summary:
        return SummaryScreen(
          name: 'seba',
          email: 'test',
          country: 'PL',
          onback: () {
            setState(() {
              currentView = ActionView.menu;
            });
          },
        );
    }
  }

  Widget _buildMenu() {
    return SafeArea(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Button(
            text: 'Add From Existing',
            onPressed: () {
              setState(() {
                currentView = ActionView.adding;
              });
            },
          ),
          Button(
            text: 'Summary',
            onPressed: () {
              setState(() {
                currentView = ActionView.summary;
              });
            },
          ),
        ],
      )
    );
  }
}