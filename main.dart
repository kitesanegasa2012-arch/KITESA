import 'package:flutter/material.dart';

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

// 1. HOME SCREEN (DAMEELEE HUNDA QABATE)
class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Barumsa Kutaa 1-6 Afaan Oromoo & Herrega'),
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
            _menuCard(context, '📖 Dubbisuu & Dhaggeeffachuu (Reading)', Colors.orange, const ReadingModuleScreen()),
            const SizedBox(height: 15),
            _menuCard(context, '✍️ Barreessuu & Qormaata (Writing)', Colors.blue, const WritingModuleScreen()),
            const SizedBox(height: 15),
            _menuCard(context, '🔢 Shallaggaa Herregaa (Maths Module)', Colors.purple, const MathModuleScreen()),
          ],
        ),
      ),
    );
  }

  Widget _menuCard(BuildContext context, String title, Color color, Widget screen) {
    return Card(
      elevation: 4,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      color: color,
      child: InkWell(
        onTap: () => Navigator.push(context, MaterialPageRoute(builder: (_) => screen)),
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

// 2. DUBBISUU FI DHAGGEEFFACHUU (READING MODULE)
class ReadingModuleScreen extends StatefulWidget {
  const ReadingModuleScreen({super.key});

  @override
  State<ReadingModuleScreen> createState() => _ReadingModuleScreenState();
}

class _ReadingModuleScreenState extends State<ReadingModuleScreen> {
  int currentIndex = 0;
  
  final List<Map<String, String>> lessons = [
    {
      "title": "Qubee A",
      "text": "A - Afaan",
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
      SnackBar(content: Text(message), duration: const Duration(seconds: 1), backgroundColor: Colors.orange[800]),
    );
  }

  @override
  Widget build(BuildContext context) {
    var item = lessons[currentIndex];
    return Scaffold(
      appBar: AppBar(title: const Text('Dubbisuu fi Dhaggeeffachuu')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            LinearProgressIndicator(value: (currentIndex + 1) / lessons.length),
            const SizedBox(height: 20),
            Text(item['title']!, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.green)),
            const SizedBox(height: 10),
            Card(
              elevation: 4,
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
              child: Padding(
                padding: const EdgeInsets.all(20.0),
                child: Column(
                  children: [
                    Image.network(item['image']!, height: 120),
                    const SizedBox(height: 20),
                    Text(item['text']!, style: const TextStyle(fontSize: 24, fontWeight: FontWeight.bold), textAlign: TextAlign.center),
                  ],
                ),
              ),
            ),
            const SizedBox(height: 20),
            ElevatedButton.icon(
              onPressed: () => playSound(item['sound']!),
              icon: const Icon(Icons.volume_up),
              label: const Text('Sagalee Dhaggeeffadhu'),
              style: ElevatedButton.styleFrom(backgroundColor: Colors.orange, padding: const EdgeInsets.all(12)),
            ),
            const Spacer(),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                if (currentIndex > 0)
                  ElevatedButton(onPressed: () => setState(() => currentIndex--), child: const Text('Duubatti')),
                if (currentIndex < lessons.length - 1)
                  ElevatedButton(onPressed: () => setState(() => currentIndex++), child: const Text('Fuuldharatti')),
              ],
            )
          ],
        ),
      ),
    );
  }
}

// 3. BARREESSUU FI QORMAATA (WRITING MODULE)
class WritingModuleScreen extends StatefulWidget {
  const WritingModuleScreen({super.key});

  @override
  State<WritingModuleScreen> createState() => _WritingModuleScreenState();
}

class _WritingModuleScreenState extends State<WritingModuleScreen> {
  final TextEditingController _controller = TextEditingController();
  String feedbackMessage = "";
  Color feedbackColor = Colors.blue;
  int currentQuestionIndex = 0;
  int score = 0;
  bool isAnswered = false;

  final List<Map<String, dynamic>> writingQuestions = [
    {"prompt": "Jecha 'Bishaan' jedhu qubee sirriidhaan asitti barreessi:", "answer": "bishaan"},
    {"prompt": "Jecha 'Afaan' jedhu qubee meeqaani (kamii) eegala? (Fkn: a)", "answer": "a"},
  ];

  void checkUserAnswer() {
    if (isAnswered) return;
    setState(() {
      var currentQ = writingQuestions[currentQuestionIndex];
      String userAnswer = _controller.text.trim().toLowerCase();
      if (userAnswer == currentQ['answer']) {
        score += 10;
        feedbackMessage = "🎉 Jabaadhu! Galchiifteetta, sirriidha!";
        feedbackColor = Colors.green;
        isAnswered = true;
      } else {
        feedbackMessage = "❌ Dogoggora qaba! Mee irra deebi'iitii yaali.";
        feedbackColor = Colors.red;
      }
    });
  }

  void nextQuestion() {
    setState(() {
      if (currentQuestionIndex < writingQuestions.length - 1) {
        currentQuestionIndex++;
        feedbackMessage = "";
        _controller.clear();
        isAnswered = false;
      } else {
        feedbackMessage = "🏆 Gaaffiin dhumateera! Qabxii waliigalaa kee: $score";
        feedbackColor = Colors.blue;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    var q = writingQuestions[currentQuestionIndex];
    return Scaffold(
      appBar: AppBar(title: const Text('Barreessuu fi Qormaata')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text('Gaaffii: ${currentQuestionIndex + 1} / ${writingQuestions.length}', style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
                Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(color: Colors.green[100], borderRadius: BorderRadius.circular(8)),
                  child: Text('Qabxii: $score', style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.green[800])),
                ),
              ],
            ),
            const SizedBox(height: 20),
            Container(
              padding: const EdgeInsets.all(16),
              color: Colors.blue[50],
              child: Text(q['prompt'], style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.blue), textAlign: TextAlign.center),
            ),
            const SizedBox(height: 20),
            TextField(
              controller: _controller,
              decoration: const InputDecoration(border: OutlineInputBorder(), labelText: 'Deebii kee asitti barreessi'),
            ),
            const SizedBox(height: 15),
            ElevatedButton(
              onPressed: checkUserAnswer,
              style: ElevatedButton.styleFrom(backgroundColor: Colors.blue[700], padding: const EdgeInsets.all(12)),
              child: const Text('Mirkaneessi (Check)', style: TextStyle(color: Colors.white, fontSize: 16)),
            ),
            const SizedBox(height: 20),
            if (feedbackMessage.isNotEmpty)
              Container(
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(color: feedbackColor.withOpacity(0.1), borderRadius: BorderRadius.circular(8)),
                child: Text(feedbackMessage, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: feedbackColor), textAlign: TextAlign.center),
              ),
            const Spacer(),
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                if (currentQuestionIndex > 0)
                  ElevatedButton(
                    onPressed: () {
                      setState(() {
                        currentQuestionIndex--;
                        feedbackMessage = "";
                        _controller.clear();
                        isAnswered = false;
                      });
                    },
                    child: const Text('Duubatti'),
                  ),
                ElevatedButton(
                  onPressed: nextQuestion,
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.green[700]),
                  child: Text(currentQuestionIndex < writingQuestions.length - 1 ? 'Fuuldharatti' : 'Xumuruu'),
                ),
              ],
            )
          ],
        ),
      ),
    );
  }
}

// 4. SHALLAGGAA HERREGAAN (MATH MODULE)
class MathModuleScreen extends StatefulWidget {
  const MathModuleScreen({super.key});

  @override
  State<MathModuleScreen> createState() => _MathModuleScreenState();
}

class _MathModuleScreenState extends State<MathModuleScreen> {
  final TextEditingController _mathController = TextEditingController();
  String mathFeedback = "";
  Color feedbackColor = Colors.purple;
  int currentQuestionIndex = 0;
  int score = 0;
  bool isAnswered = false;

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
    if (isAnswered) return;
    setState(() {
      var currentQ = mathQuestions[currentQuestionIndex];
      String userAnswer = _mathController.text.trim();
      if (userAnswer == currentQ['answer'] || userAnswer.toUpperCase() == "B" && currentQ['answer'] == "27" || userAnswer.toUpperCase() == "A" && currentQ['answer'] == "24") {
        score += 10;
        mathFeedback = "🎉 Jabaadhu! Herregni sirriidha!";
        feedbackColor = Colors.green;
        isAnswered = true;
      } else {
        mathFeedback = "❌ Dogoggora qaba! Mee irra deebi'iitii yaali.";
        feedbackColor = Colors.red;
      }
    });
  }

  void nextQuestion() {
    setState(() {
      if (currentQuestionIndex < mathQuestions.length - 1) {
        currentQuestionIndex++;
        mathFeedback = "";
        _mathController.clear();
        isAnswered = false;
      } else {
        mathFeedback = "🏆 Galatoomi! Qabxii herregaa waliigalaa: $score";
        feedbackColor = Colors.blue;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    var q = mathQuestions[currentQuestionIndex];
    return Scaffold(
      appBar: AppBar(title: const Text('Shallaggaa Herregaa & Qabxii')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text('Gaaffii: ${currentQuestionIndex + 1} / ${mathQuestions.length}', style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
                Container(
                  padding: const EdgeInsets.all(8),
                  decoration: BoxDecoration(color: Colors.purple[100], borderRadius: BorderRadius.circular(8)),
                  child: Text('Qabxii: $score', style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.purple[800])),
                ),
              ],
            ),
            const SizedBox(height: 20),
            Container(
              padding: const EdgeInsets.all(16),
              color: Colors.purple[50],
              child: Column(
                children: [
                  Text(q['question'], style: const TextStyle(fontSize: 28, fontWeight: FontWeight.bold, color: Colors.purple), textAlign: TextAlign.center),
                  const SizedBox(height: 15),
                  Text(q['options'].join('   '), style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.black87)),
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
              style: ElevatedButton.styleFrom(backgroundColor: Colors.purple, padding: const EdgeInsets.all(12)),
              child: const Text('Mirkaneessi (Check Math)', style: TextStyle(color: Colors.white, fontSize: 16)),
            ),
            const SizedBox(height: 20),
            if (mathFeedback.isNotEmpty)
              Container(
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(color: feedbackColor.withOpacity(0.1), borderRadius: BorderRadius.circular(8)),
                child: Text(mathFeedback, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: feedbackColor), textAlign: TextAlign.center),
              ),
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
                        isAnswered = false;
                      });
                    },
                    child: const Text('Duubatti'),
                  ),
                ElevatedButton(
                  onPressed: nextQuestion,
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.green[700]),
                  child: Text(currentQuestionIndex < mathQuestions.length - 1 ? 'Fuuldharatti' : 'Xumuruu'),
                ),
              ],
            )
          ],
        ),
      ),
    );
  }
}
