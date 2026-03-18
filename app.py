from flask import Flask, render_template, request, jsonify
import random
import json

app = Flask(__name__)


class MusicTheoryQuiz:

    def __init__(self):
        self.questions = [
            # ── Notes & Pitch ──────────────────────────────────────────────
            {
                "id": 1,
                "question": "How many lines does a standard musical staff have?",
                "options": {"A": "3", "B": "4", "C": "5", "D": "6"},
                "answer": "C",
                "explanation": "A standard staff (stave) always has exactly 5 lines and 4 spaces."
            },
            {
                "id": 2,
                "question": "What is the name of the symbol placed at the beginning of a staff to indicate pitch?",
                "options": {"A": "Time signature", "B": "Clef", "C": "Key signature", "D": "Bar line"},
                "answer": "B",
                "explanation": "A clef is placed at the beginning of the staff to define the pitch of the notes on each line and space."
            },
            {
                "id": 3,
                "question": "Which clef is most commonly used for piano treble (right hand)?",
                "options": {"A": "Bass clef", "B": "Alto clef", "C": "Treble clef", "D": "Tenor clef"},
                "answer": "C",
                "explanation": "The treble clef (G clef) is used for higher-pitched notes and is standard for the right hand in piano music."
            },
            {
                "id": 4,
                "question": "Which clef is most commonly used for piano bass (left hand)?",
                "options": {"A": "Treble clef", "B": "Alto clef", "C": "Tenor clef", "D": "Bass clef"},
                "answer": "D",
                "explanation": "The bass clef (F clef) is used for lower-pitched notes and is standard for the left hand in piano music."
            },
            {
                "id": 5,
                "question": "What does a ledger line do?",
                "options": {
                    "A": "Marks the end of a piece",
                    "B": "Extends the staff for notes above or below its range",
                    "C": "Indicates a change of tempo",
                    "D": "Shows where to repeat"
                },
                "answer": "B",
                "explanation": "Ledger lines are short extra lines added above or below the staff to accommodate notes outside its normal range."
            },
            {
                "id": 6,
                "question": "What is the note on the first ledger line below the treble clef staff?",
                "options": {"A": "B", "B": "C", "C": "D", "D": "A"},
                "answer": "B",
                "explanation": "Middle C sits on the first ledger line below the treble clef staff."
            },
            {
                "id": 7,
                "question": "How many semitones are in one octave?",
                "options": {"A": "8", "B": "10", "C": "12", "D": "7"},
                "answer": "C",
                "explanation": "An octave consists of 12 semitones (half steps), covering all the notes in Western music before the pattern repeats."
            },
            {
                "id": 8,
                "question": "What is the musical term for the distance between two pitches?",
                "options": {"A": "Interval", "B": "Chord", "C": "Scale", "D": "Arpeggio"},
                "answer": "A",
                "explanation": "An interval is the distance in pitch between two notes, measured in steps or semitones."
            },
            {
                "id": 9,
                "question": "What does a sharp (♯) do to a note?",
                "options": {
                    "A": "Lowers it by one semitone",
                    "B": "Raises it by one semitone",
                    "C": "Raises it by one tone",
                    "D": "Returns it to its natural pitch"
                },
                "answer": "B",
                "explanation": "A sharp raises the pitch of a note by one semitone (half step)."
            },
            {
                "id": 10,
                "question": "What does a flat (♭) do to a note?",
                "options": {
                    "A": "Raises it by one semitone",
                    "B": "Returns it to its natural pitch",
                    "C": "Lowers it by one semitone",
                    "D": "Lowers it by one tone"
                },
                "answer": "C",
                "explanation": "A flat lowers the pitch of a note by one semitone (half step)."
            },
            # ── Rhythm & Time ──────────────────────────────────────────────
            {
                "id": 11,
                "question": "How many beats does a semibreve (whole note) receive in 4/4 time?",
                "options": {"A": "1", "B": "2", "C": "3", "D": "4"},
                "answer": "D",
                "explanation": "A semibreve (whole note) lasts for 4 beats, filling a complete bar in 4/4 time."
            },
            {
                "id": 12,
                "question": "How many beats does a minim (half note) receive in 4/4 time?",
                "options": {"A": "1", "B": "2", "C": "3", "D": "4"},
                "answer": "B",
                "explanation": "A minim (half note) lasts for 2 beats — exactly half the value of a semibreve."
            },
            {
                "id": 13,
                "question": "How many crotchets (quarter notes) equal one semibreve (whole note)?",
                "options": {"A": "2", "B": "3", "C": "4", "D": "8"},
                "answer": "C",
                "explanation": "Four crotchets equal one semibreve: semibreve (4) ÷ crotchet (1) = 4."
            },
            {
                "id": 14,
                "question": "What does the top number of a time signature tell you?",
                "options": {
                    "A": "The tempo of the piece",
                    "B": "The type of note that gets one beat",
                    "C": "The number of beats in each bar",
                    "D": "The key of the piece"
                },
                "answer": "C",
                "explanation": "The top number of a time signature tells you how many beats are in each bar."
            },
            {
                "id": 15,
                "question": "What does the bottom number of a time signature tell you?",
                "options": {
                    "A": "The number of bars in the piece",
                    "B": "The type of note that represents one beat",
                    "C": "The tempo in BPM",
                    "D": "The number of beats per bar"
                },
                "answer": "B",
                "explanation": "The bottom number indicates the note value that equals one beat. '4' means a quarter note (crotchet) gets one beat."
            },
            {
                "id": 16,
                "question": "In 3/4 time, how many crotchet (quarter note) beats are there per bar?",
                "options": {"A": "2", "B": "3", "C": "4", "D": "6"},
                "answer": "B",
                "explanation": "In 3/4 time the top number is 3, meaning 3 crotchet beats per bar. This is the time signature of a waltz."
            },
            {
                "id": 17,
                "question": "What is the value of a dotted minim (dotted half note) in beats?",
                "options": {"A": "2", "B": "2.5", "C": "3", "D": "4"},
                "answer": "C",
                "explanation": "A dot adds half the note's value. Minim = 2 beats; half of 2 = 1; so dotted minim = 3 beats."
            },
            {
                "id": 18,
                "question": "How many quavers (eighth notes) equal one crotchet (quarter note)?",
                "options": {"A": "2", "B": "3", "C": "4", "D": "8"},
                "answer": "A",
                "explanation": "A quaver is worth half a crotchet, so two quavers equal one crotchet."
            },
            {
                "id": 19,
                "question": "What is a rest in music?",
                "options": {
                    "A": "A gradual slowing of tempo",
                    "B": "A symbol indicating silence for a specific duration",
                    "C": "A repeat sign",
                    "D": "A type of ornament"
                },
                "answer": "B",
                "explanation": "A rest is a symbol that indicates a period of silence. Every note value has a corresponding rest of the same duration."
            },
            {
                "id": 20,
                "question": "What is a bar (measure) in music?",
                "options": {
                    "A": "A tempo marking",
                    "B": "A segment of time defined by the time signature, separated by bar lines",
                    "C": "A type of scale",
                    "D": "A dynamic marking"
                },
                "answer": "B",
                "explanation": "A bar (or measure) is a segment of music containing a fixed number of beats as defined by the time signature, bounded by vertical bar lines."
            },
            # ── Scales & Keys ──────────────────────────────────────────────
            {
                "id": 21,
                "question": "How many notes are in a major scale?",
                "options": {"A": "5", "B": "6", "C": "7", "D": "8"},
                "answer": "C",
                "explanation": "A major scale has 7 distinct notes (plus the octave repetition of the first note), following the pattern T-T-S-T-T-T-S."
            },
            {
                "id": 22,
                "question": "What pattern of tones (T) and semitones (S) forms a major scale?",
                "options": {
                    "A": "T-T-T-S-T-T-S",
                    "B": "T-S-T-T-S-T-T",
                    "C": "T-T-S-T-T-T-S",
                    "D": "S-T-T-T-S-T-T"
                },
                "answer": "C",
                "explanation": "The major scale always follows: Tone-Tone-Semitone-Tone-Tone-Tone-Semitone (T-T-S-T-T-T-S)."
            },
            {
                "id": 23,
                "question": "The key of C major uses which set of notes?",
                "options": {
                    "A": "C D E F G A B — all white keys, no sharps or flats",
                    "B": "C D E♭ F G A B",
                    "C": "C D E F♯ G A B",
                    "D": "C♯ D♯ F G♯ A♯ C"
                },
                "answer": "A",
                "explanation": "C major is unique — it uses only the 7 white keys on the piano with no sharps or flats."
            },
            {
                "id": 24,
                "question": "How many sharps are in the key of G major?",
                "options": {"A": "0", "B": "1", "C": "2", "D": "3"},
                "answer": "B",
                "explanation": "G major has one sharp: F♯. The key signature shows F♯ on the staff."
            },
            {
                "id": 25,
                "question": "What is a pentatonic scale?",
                "options": {
                    "A": "A scale with 4 notes",
                    "B": "A scale with 5 notes",
                    "C": "A scale with 6 notes",
                    "D": "A scale with 8 notes"
                },
                "answer": "B",
                "explanation": "Pentatonic means 'five tones'. The pentatonic scale has 5 notes per octave and is used widely in folk, blues, and pop music."
            },
            # ── Dynamics & Tempo ───────────────────────────────────────────
            {
                "id": 26,
                "question": "What does 'forte' (f) mean?",
                "options": {"A": "Soft", "B": "Very soft", "C": "Loud", "D": "Very loud"},
                "answer": "C",
                "explanation": "Forte (f) is an Italian term meaning loud. It is one of the most common dynamic markings in music."
            },
            {
                "id": 27,
                "question": "What does 'piano' (p) mean as a dynamic marking?",
                "options": {"A": "Loud", "B": "Very loud", "C": "Soft", "D": "Medium loud"},
                "answer": "C",
                "explanation": "Piano (p) is an Italian term meaning soft or quiet. This is why the instrument 'piano' (short for pianoforte) can play both soft and loud."
            },
            {
                "id": 28,
                "question": "What does 'mezzo-forte' (mf) mean?",
                "options": {"A": "Very loud", "B": "Medium loud", "C": "Medium soft", "D": "Very soft"},
                "answer": "B",
                "explanation": "Mezzo-forte (mf) means moderately loud — louder than mezzo-piano but softer than forte."
            },
            {
                "id": 29,
                "question": "What does 'allegro' indicate?",
                "options": {"A": "Slow and stately", "B": "At a walking pace", "C": "Fast and lively", "D": "Very slow"},
                "answer": "C",
                "explanation": "Allegro is an Italian tempo marking meaning fast and lively, typically around 120–168 BPM."
            },
            {
                "id": 30,
                "question": "What does 'andante' mean?",
                "options": {"A": "Very fast", "B": "At a walking pace (moderately slow)", "C": "Very slow", "D": "Lively and quick"},
                "answer": "B",
                "explanation": "Andante is an Italian term meaning 'at a walking pace' — a moderate, unhurried tempo, typically around 76–108 BPM."
            },
        ]

    # ── Return questions for the frontend (no answers exposed) ────────────────
    def get_questions_for_frontend(self, randomize=False):
        questions = self.questions.copy()
        if randomize:
            random.shuffle(questions)
        return [
            {
                "id":       q["id"],
                "question": q["question"],
                "options":  q["options"]
                # NOTE: 'answer' and 'explanation' are intentionally excluded
            }
            for q in questions
        ]

    # ── Performance feedback based on percentage ──────────────────────────────
    def get_performance_feedback(self, percentage):
        if percentage == 100:
            return "🏆 Perfect score! Outstanding work!"
        elif percentage >= 80:
            return "🌟 Excellent! You have a strong grasp of music theory."
        elif percentage >= 60:
            return "👍 Good effort! Review the topics you missed and try again."
        elif percentage >= 40:
            return "📖 Keep practising — you're making progress!"
        else:
            return "🎵 Keep going! Every musician starts somewhere."

    # ── Grade submitted answers and return results ────────────────────────────
    def evaluate_quiz(self, user_submissions):
        """
        user_submissions: dict of { question_id (str): chosen_key (str) }
        Returns a dict with score, percentage, performance message, and per-question detail.
        """
        # Build a lookup from question id to full question data
        question_map = {str(q["id"]): q for q in self.questions}

        score = 0
        detailed_results = []

        for q_id, chosen_key in user_submissions.items():
            q = question_map.get(str(q_id))
            if not q:
                continue

            is_correct = chosen_key == q["answer"]
            if is_correct:
                score += 1

            detailed_results.append({
                "question":       q["question"],
                "your_answer":    chosen_key,
                "correct_answer": q["answer"],
                "is_correct":     is_correct,
                "explanation":    q["explanation"]
            })

        total      = len(user_submissions)
        percentage = round((score / total) * 100) if total > 0 else 0

        return {
            "score":               score,
            "total":               total,
            "percentage":          percentage,
            "performance_message": self.get_performance_feedback(percentage),
            "detailed_results":    detailed_results
        }


# ── Instantiate quiz globally ─────────────────────────────────────────────────
quiz = MusicTheoryQuiz()


# ── Routes ────────────────────────────────────────────────────────────────────

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/quiz')
def quiz_page():
    questions_for_js = quiz.get_questions_for_frontend(randomize=True)
    return render_template('index.html', questions=json.dumps(questions_for_js))


@app.route('/coming-soon')
def coming_soon():
    return render_template('coming-soon.html')


@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    data             = request.get_json()
    user_submissions = data.get('answers', {})
    results          = quiz.evaluate_quiz(user_submissions)
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)