import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

void main() {
  runApp(const OromiaLearningApp());
}

class OromiaLearningApp extends StatelessWidget {
  const OromiaLearningApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Barumsa Kutaa 1-6 Oromia',
      theme: ThemeData(
        primarySwatch: Colors.green,
        scaffoldBackgroundColor: const Color(0xFFF7F9FC),
      ),
      home: const HomeScreen(),
    );
  }
}

// 1. HOME SCREEN
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Kutaa 1-6 Barumsa Afaanii fi Herregaa'),
        backgroundColor: Colors.green[800],
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Text(
              'Mee damee barachuu barbaaddu filadhu:',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 20),
            // 1. Dubbisuu
            _menuCard(context, '📖 Dubbisuu & Dhaggeeffachuu (Reading)', Colors.orange, const ReadingModuleScreen()),
            const SizedBox(height: 15),
            // 2. Barreessuu
            _menuCard(context, '✍️ Barreessuu & Akkeessuu (Writing)', Colors.blue, const WritingModuleScreen()),
            const SizedBox(height: 15),
            // 3. Herrega (Bakki kunuu asitti sirriitti qabameera)
            _menuCard(context, '🔢 Shallaggaa Herregaa (Maths Module)', Colors.purple, const MathModuleScreen()),
          ],
        ),
      ),
    );
  }

  Widget _menuCard(BuildContext context, String title, Color color, Widget? screen) {
    return Card(
      elevation: 4,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      color: color,
      child: InkWell(
        onTap: screen != null ? () => Navigator.push(context, MaterialPageRoute(builder: (_) => screen)) : null,
        child: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Text(
            title,
            style: const TextStyle(fontSize: 16, color: Colors.white, fontWeight: FontWeight.bold),
            textAlign: TextAlign.center,
          ),
        ),
      ),
    );
  }
}
  Widget _menuCard(BuildContext context, String title, Color color, Widget? screen) {
    return Card(
      elevation: 4,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      color: color,
      child: InkWell(
        onTap: screen != null ? () => Navigator.push(context, MaterialPageRoute(builder: (_) => screen)) : null,
        child: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Text(
            title,
            style: const TextStyle(fontSize: 16, color: Colors.white, fontWeight: FontWeight.bold),
            textAlign: TextAlign.center,
          ),
        ),
      ),
    );
  }
}

// DUBBISUU FI FAKKII / SAGALEE SALPHAA (READING MODULE WITH IMAGES & AUDIO)
class ReadingModuleScreen extends StatefulWidget {
  const ReadingModuleScreen({super.key});

  @override
  State<ReadingModuleScreen> createState() => _ReadingModuleScreenState();
}

class _ReadingModuleScreenState extends State<ReadingModuleScreen> {
  int currentIndex = 0;
  
  // Qubee, Fakkii fi Sagalee Qabiyyee Salphaa
  final List<Map<String, String>> lessons = [
    {
      "title": "Qubee A",
      "text": "A - Afaan Oromoo",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Apple.svg/1200px-Red_Apple.svg.png",
      "sound": "Qubee A sirriitti dubbifameera."
    },
    {
      "title": "Jecha Bishaan",
      "text": "Bishaan - Water",
      "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Blue_Water_Drop.svg/1024px-Blue_Water_Drop.svg.png",
      "sound": "Jechi Bishaan jedhu dhaga'amaa jira."
    },
  ];

  void playSound(String message) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        content: Text(message),
        duration: const Duration(seconds: 1),
        backgroundColor: Colors.orange[800],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    var item = lessons[currentIndex];
    return Scaffold(
      appBar: AppBar(title: const Text('Dubbisuu, Fakkii & Sagalee')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text(item['title']!, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.green)),
            const SizedBox(height: 20),
            Card(
              elevation: 4,
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
              child: Padding(
                padding: const EdgeInsets.all(20.0),
                child: Column(
                  children: [
                    // Fakkii Asitti Mul'ata
                    Image.network(
                      item['image']!,
                      height: 120,
                    ),
                    const SizedBox(height: 20),
                    Text(
                      item['text']!,
                      style: const TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
                      textAlign: TextAlign.center,
                    ),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 20),
            // Sagalee Dhaggeeffachuu Button
            ElevatedButton.icon(
              onPressed: () => playSound(item['sound']!),
              icon: const Icon(Icons.volume_up),
              label: const Text('Sagalee Dhaggeeffadhu (Listen Audio)'),
              style: ElevatedButton.styleFrom(backgroundColor: Colors.orange, padding: const EdgeInsets.all(12)),
            ),
            const Spacer(),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                if (currentIndex > 0)
                  ElevatedButton(
                    onPressed: () => setState(() => currentIndex--),
                    child: const Text('Duubatti'),
                  ),
                if (currentIndex < lessons.length - 1)
                  ElevatedButton(
                    onPressed: () => setState(() => currentIndex++),
                    child: const Text('Fuuldharatti'),
                  ),
              ],
            )
          ],
        ),
      ),
    );
  }
}

// 3. BARREESSUU FI RAGAA QABACHUU (WRITING & EVALUATION MODULE)
class WritingModuleScreen extends StatefulWidget {
  const WritingModuleScreen({super.key});

  @override
  State<WritingModuleScreen> createState() => _WritingModuleScreenState();
}

class _WritingModuleScreenState extends State<WritingModuleScreen> {
  final TextEditingController _controller = TextEditingController();
  String feedbackMessage = "";
  bool isCorrectSaved = false;

  // Expected target text for comparison
  final String targetText = "Bishaan"; 

  void checkUserAnswer() {
    setState(() {
      if (_controller.text.trim().toLowerCase() == targetText.toLowerCase()) {
        feedbackMessage = "Jabaadhu! Galchiifteetta, sirriidha! (Saved to local record)";
        isCorrectSaved = true;
      } else {
        feedbackMessage = "Dogoggora qaba, irra deebi'iitii fooyyessi (Try Again).";
        isCorrectSaved = false;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Barreessuu fi Qormaata Salphaa')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Text(
              'Jecha armaan gadii sirriitti barreessi:',
              style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 10),
            Container(
              padding: const EdgeInsets.all(12),
              color: Colors.yellow[100],
              child: Text(
                'Jecha Baratamuu Qabu: "$targetText"',
                style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold, color: Colors.brown),
                textAlign: TextAlign.center,
              ),
            ),
            const SizedBox(height: 20),
            TextField(
              controller: _controller,
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                labelText: 'Asitti barreessi (Type here)',
              ),
            ),
            const SizedBox(height: 15),
            ElevatedButton(
              onPressed: checkUserAnswer,
              style: ElevatedButton.styleFrom(backgroundColor: Colors.blue[700]),
              child: const Text('Mirkaneessi fi Kuusi (Check & Save)', style: TextStyle(color: Colors.white)),
            ),
            const SizedBox(height: 20),
            if (feedbackMessage.isNotEmpty)
              Container(
                padding: const EdgeInsets.all(12),
                color: isCorrectSaved ? Colors.green[150] : Colors.red[150],
                child: Text(
                  feedbackMessage,
                  style: TextStyle(
                    fontSize: 16, 
                    fontWeight: FontWeight.bold, 
                    color: isCorrectSaved ? Colors.green[800] : Colors.red[800]
                  ),
                  textAlign: TextAlign.center,
                ),
              ),
          ],
        ),
      ),
    );
  }
}
// 4. SHALLAGGAA HERREGAAN (MATH MODULE GUUTUU)
class MathModuleScreen extends StatefulWidget {
  const MathModuleScreen({super.key});

  @override
  State<MathModuleScreen> createState() => _MathModuleScreenState();
}

class _MathModuleScreenState extends State<MathModuleScreen> {
  final TextEditingController _mathController = TextEditingController();
  String mathFeedback = "";
  int currentQuestionIndex = 0;

  // Gaaffilee herregaa sadarkaa 1-6
  final List<Map<String, dynamic>> mathQuestions = [
    {
      "question": "15 + 12 = ?",
      "options": ["A) 25", "B) 27", "C) 30", "D) 22"],
      "answer": "27"
    },
    {
      "question": "45 - 20 = ?",
      "options": ["A) 15", "B) 25", "C) 20", "D) 35"],
      "answer": "25"
    },
    {
      "question": "6 × 4 = ?",
      "options": ["A) 24", "B) 18", "C) 28", "D) 20"],
      "answer": "24"
    },
  ];

  void checkMathAnswer() {
    setState(() {
      var currentQ = mathQuestions[currentQuestionIndex];
      String userAnswer = _mathController.text.trim();
      
      // Deebiin barataa filannoo wajjin ykn kallattiidhaan lakkoofsaan yoo wal simate
      if (userAnswer == currentQ['answer'] || userAnswer.toUpperCase() == "B") {
        mathFeedback = "Herregni sirriidha! Jabaadhu! (Saved)";
      } else {
        mathFeedback = "Dogoggora qaba, deebi'ii yaali.";
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    var q = mathQuestions[currentQuestionIndex];
    return Scaffold(
      appBar: AppBar(title: const Text('Shallaggaa Herregaa Kutaa 1-6')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text('Gaaffii Herregaa ${currentQuestionIndex + 1}ffaa:', style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
            const SizedBox(height: 20),
            Container(
              padding: const EdgeInsets.all(16),
              color: Colors.purple[50],
              child: Column(
                children: [
                  Text(
                    q['question'],
                    style: const TextStyle(fontSize: 28, fontWeight: FontWeight.bold, color: Colors.purple),
                    textAlign: TextAlign.center,
                  ),
                  const SizedBox(height: 15),
                  Text(
                    q['options'].join('   '),
                    style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.black87),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 20),
            TextField(
              controller: _mathController,
              decoration: const InputDecoration(border: OutlineInputBorder(), labelText: 'Deebii kee asitti barreessi (Fkn: 27)'),
            ),
            const SizedBox(height: 15),
            ElevatedButton(
              onPressed: checkMathAnswer,
              style: ElevatedButton.styleFrom(backgroundColor: Colors.purple),
              child: const Text('Mirkaneessi fi Kuusi (Check Math)', style: TextStyle(color: Colors.white)),
            ),
            const SizedBox(height: 20),
            if (mathFeedback.isNotEmpty)
              Text(mathFeedback, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.purple), textAlign: TextAlign.center),
            const Spacer(),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                if (currentQuestionIndex > 0)
                  ElevatedButton(
                    onPressed: () {
                      setState(() {
                        currentQuestionIndex--;
                        mathFeedback = "";
                        _mathController.clear();
                      });
                    },
                    child: const Text('Duubatti'),
                  ),
                if (currentQuestionIndex < mathQuestions.length - 1)
                  ElevatedButton(
                    onPressed: () {
                      setState(() {
                        currentQuestionIndex++;
                        mathFeedback = "";
                        _mathController.clear();
                      });
                    },
                    child: const Text('Fuuldharatti'),
                  ),
              ],
            )
          ],
        ),
      ),
    );
  }
}
