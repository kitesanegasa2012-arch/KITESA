import 'package:flutter/material.dart';

void main() {
  runApp(const HiikaWayApp());
}

class HiikaWayApp extends StatelessWidget {
  const HiikaWayApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Hiika way (HW)',
      theme: ThemeData(
        primarySwatch: Colors.green,
        scaffoldBackgroundColor: const Color(0xFFF7F9FC),
      ),
      home: const NameInputScreen(),
    );
  }
}

// 0. MAQAA BARATAA GALCHUU (NAME INPUT SCREEN & CLASS LIST - MAX 80)
class NameInputScreen extends StatefulWidget {
  const NameInputScreen({super.key});

  @override
  State<NameInputScreen> createState() => _NameInputScreenState();
}

class _NameInputScreenState extends State<NameInputScreen> {
  final TextEditingController _nameController = TextEditingController();
  final TextEditingController _idController = TextEditingController();
  
  // Barattoota daree keessatti hanga 80 galmaa'an qabachuuf
  final List<Map<String, String>> registeredStudents = [];

  void addStudent() {
    String name = _nameController.text.trim();
    String id = _idController.text.trim();

    if (name.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Mee maqaa barataa barreessi!')),
      );
      return;
    }

    if (registeredStudents.length >= 80) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Daree tokko keessatti barataan 80 guutameera!')),
      );
      return;
    }

    setState(() {
      registeredStudents.add({
        'id': id.isEmpty ? '${registeredStudents.length + 1}' : id,
        'name': name,
      });
      _nameController.clear();
      _idController.clear();
    });
  }

  void proceedToHome(Map<String, String> student) {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (_) => HomeScreen(studentName: student['name']!)),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Hiika way (HW) - Galmee Daree (Hanga 80)'),
        backgroundColor: Colors.green[800],
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const Text(
              'Galmee Barattoota Daree (Max 80)',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.green),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 10),
            Row(
              children: [
                Expanded(
                  flex: 2,
                  child: TextField(
                    controller: _nameController,
                    decoration: const InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Maqaa Barataa',
                      prefixIcon: Icon(Icons.person),
                    ),
                  ),
                ),
                const SizedBox(width: 10),
                Expanded(
                  flex: 1,
                  child: TextField(
                    controller: _idController,
                    decoration: const InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'ID (Lakk)',
                    ),
                  ),
                ),
                const SizedBox(width: 10),
                ElevatedButton(
                  onPressed: addStudent,
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.green[800], padding: const EdgeInsets.all(16)),
                  child: const Text('Galchi', style: TextStyle(color: Colors.white)),
                ),
              ],
            ),
            const SizedBox(height: 10),
            Text(
              'Barattoota Galmaa\'an: ${registeredStudents.length} / 80',
              style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14),
            ),
            const Divider(),
            Expanded(
              child: registeredStudents.isEmpty
                  xml: const Center(child: Text('Ammaaf barataan galmaa\'e hin jiru. Maqaa galchaa!'))
                  : ListView.builder(
                      itemCount: registeredStudents.length,
                      itemBuilder: (context, index) {
                        var st = registeredStudents[index];
                        return Card(
                          child: ListTile(
                            leading: CircleAvatar(child: Text(st['id']!)),
                            title: Text(st['name']!, style: const TextStyle(fontWeight: FontWeight.bold)),
                            trailing: ElevatedButton(
                              style: ElevatedButton.styleFrom(backgroundColor: Colors.orange[800]),
                              onPressed: () => proceedToHome(st),
                              child: const Text('Barachuu Jalqabi', style: TextStyle(color: Colors.white)),
                            ),
                          ),
                        );
                      },
                    ),
            ),
          ],
        ),
      ),
    );
  }
}

// 1. HOME SCREEN (MAQAA BARATAA FILATAMEEN KAN DHUFU)
class HomeScreen extends StatelessWidget {
  final String studentName;
  const HomeScreen({super.key, required this.studentName});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Hiika way (HW) - $studentName'),
        backgroundColor: Colors.green[800],
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text(
              'Baga nagaan dhufte, $studentName! Damee barachuu barbaaddu filadhu:',
              style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
              textAlign: TextAlign.center,
            ),
            const SizedBox(height: 20),
            _menuCard(context, '📖 Dubbisuu & Dhaggeeffachuu (Reading)', Colors.orange, ReadingModuleScreen(studentName: studentName)),
            const SizedBox(height: 15),
            _menuCard(context, '✍️ Barreessuu & Qormaata (Writing)', Colors.blue, WritingModuleScreen(studentName: studentName)),
            const SizedBox(height: 15),
            _menuCard(context, '🔢 Shallaggaa Herregaa (Maths Module)', Colors.purple, MathModuleScreen(studentName: studentName)),
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
  final String studentName;
  const ReadingModuleScreen({super.key, required this.studentName});

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
      SnackBar(content: Text('${widget.studentName}, $message'), duration: const Duration(seconds: 1), backgroundColor: Colors.orange[800]),
    );
  }

  @override
  Widget build(BuildContext context) {
    var item = lessons[currentIndex];
    return Scaffold(
      appBar: AppBar(title: Text('Dubbisuu - ${widget.studentName}')),
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
  final String studentName;
  const WritingModuleScreen({super.key, required this.studentName});

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
        feedbackMessage = "🎉 Jabaadhu ${widget.studentName}! Galchiifteetta, sirriidha!";
        feedbackColor = Colors.green;
        isAnswered = true;
      } else {
        feedbackMessage = "❌ ${widget.studentName}, dogoggora qaba! Mee irra deebi'iitii yaali.";
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
        feedbackMessage = "🏆 Galatoomi ${widget.studentName}! Qabxii waliigalaa kee: $score";
        feedbackColor = Colors.blue;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    var q = writingQuestions[currentQuestionIndex];
    return Scaffold(
      appBar: AppBar(title: Text('Barreessuu - ${widget.studentName}')),
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
  final String studentName;
  const MathModuleScreen({super.key, required this.studentName});

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
  ];

  void checkMathAnswer() {
    if (isAnswered) return;
    setState(() {
      var currentQ = mathQuestions[currentQuestionIndex];
      String userAnswer = _mathController.text.trim();
      if (userAnswer == currentQ['answer'] || userAnswer.toUpperCase() == "B" && currentQ['answer'] == "27") {
        score += 10;
        mathFeedback = "🎉 Jabaadhu ${widget.studentName}! Herregni sirriidha!";
        feedbackColor = Colors.green;
        isAnswered = true;
      } else {
        mathFeedback = "❌ ${widget.studentName}, dogoggora qaba! Mee irra deebi'iitii yaali.";
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
        mathFeedback = "🏆 Galatoomi ${widget.studentName}! Qabxii herregaa waliigalaa: $score";
        feedbackColor = Colors.blue;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    var q = mathQuestions[currentQuestionIndex];
    return Scaffold(
      appBar: AppBar(title: Text('Herrega - ${widget.studentName}')),
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
                  Text(q['options'].join('    '), style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.black87)),
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
