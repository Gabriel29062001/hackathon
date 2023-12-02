import 'package:flutter/material.dart';


class YesNoPage extends StatefulWidget {
  @override
  _YesNoPageState createState() => _YesNoPageState();
}

class _YesNoPageState extends State<YesNoPage> {
  int a=0; // Variable a
  List<String> questions = ["Question1","Question2","Question3","Question4","Question5","Question6","Question7"];
  List<int> answers = [];

  
  int currentQuestion = 0;
  @override
  Widget build(BuildContext context) {
    
    return Scaffold(
      appBar: AppBar(
        title: Text('Answer by clicking on one of the two buttons'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Container(
              width: 1000,
              height: 400,
              color: Colors.blue,
              child: Center(
                child: Text(
                  questions[currentQuestion],
                  textAlign: TextAlign.center,
                  style: const  TextStyle(
                    fontSize: 38,
                    color: Colors.white,
                  ),
                ),
              ),
            ),
            const SizedBox(height: 50),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                ElevatedButton(
                  onPressed: () {
                    setState(() {
                      answers.add(1);
                      currentQuestion+=1;
                    });
                    print('Response: Yes');
                  },
                  style: ElevatedButton.styleFrom(
                    minimumSize: Size(250, 150),
                  ),
                  child: Text(
                    'Yes',
                    style: TextStyle(fontSize: 38),
                  ),
                ),
                SizedBox(width: 20),
                ElevatedButton(
                  onPressed: () {
                    setState(() {
                      answers.add(0);
                      currentQuestion+=1;
                    });
                    print('Response: No');
                  },
                  style: ElevatedButton.styleFrom(
                    minimumSize: Size(250, 150),
                  ),
                  child: Text(
                    'No',
                    style: TextStyle(fontSize: 38),
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

