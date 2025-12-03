
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Define tempo and time signature
tempo = 160
time_signature = (4, 4)

# Define the key: F minor
key = 'Fm'

# Create instruments
bass_program = Program(33)  # Acoustic Bass
piano_program = Program(0)  # Acoustic Grand Piano
drums_program = Program(128)  # Drums
sax_program = Program(64)  # Tenor Saxophone

# Create instruments
bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
drums = Instrument(program=drums_program)
sax = Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# TIME: 0.0 to 6.0 seconds (4 bars at 160 BPM)
# Each beat = 0.375 seconds (60 / 160 = 0.375)
# Each bar = 1.5 seconds
# Bar 1: Drums only
# Bar 2-4: Everyone in

# -----------------------------
# BAR 1 (0.0 to 1.5 seconds): Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Drums: 8th notes on hihat, kicks on 1 and 3, snares on 2 and 4
# Note durations: 0.1875s per 8th note

# Hihat: every 8th note
for i in range(8):
    time = i * 0.1875
    hihat = Note(velocity=64, pitch=42, start=time, end=time + 0.1875)
    drums.notes.append(hihat)

# Kick on 1 and 3
kick1 = Note(velocity=100, pitch=36, start=0.0, end=0.1875)
kick3 = Note(velocity=100, pitch=36, start=0.75, end=0.9375)
drums.notes.append(kick1)
drums.notes.append(kick3)

# Snare on 2 and 4
snare2 = Note(velocity=90, pitch=38, start=0.375, end=0.5625)
snare4 = Note(velocity=90, pitch=38, start=1.125, end=1.3125)
drums.notes.append(snare2)
drums.notes.append(snare4)

# -----------------------------
# BAR 2 (1.5 to 3.0 seconds): Bass walks, piano opens, sax enters

# BASS: Root and fifth with chromatic approach
# Bar 2: Fm7 -> Dm7
# Root: F (48), 5th: C (60)
# Chromatic approach: E (64) before F

bass_note1 = Note(velocity=70, pitch=64, start=1.5, end=1.6875)  # E
bass_note2 = Note(velocity=70, pitch=48, start=1.6875, end=1.875)  # F
bass_note3 = Note(velocity=70, pitch=60, start=1.875, end=2.0625)  # C
bass_note4 = Note(velocity=70, pitch=48, start=2.0625, end=2.25)  # F
bass.notes.append(bass_note1)
bass.notes.append(bass_note2)
bass.notes.append(bass_note3)
bass.notes.append(bass_note4)

# PIANO: Open voicings, different chords each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 2: Play F, Ab, C, Eb as a spread voicing

piano_note1 = Note(velocity=80, pitch=48, start=1.5, end=2.0)
piano_note2 = Note(velocity=80, pitch=50, start=1.5, end=2.0)
piano_note3 = Note(velocity=80, pitch=60, start=1.5, end=2.0)
piano_note4 = Note(velocity=80, pitch=53, start=1.5, end=2.0)
piano.notes.append(piano_note1)
piano.notes.append(piano_note2)
piano.notes.append(piano_note3)
piano.notes.append(piano_note4)

# SAX: Motif — a question, not a statement
# Tenor sax: F (66), Ab (68), C (72), rest
# Play F, Ab, C, then rest — a whisper

sax_note1 = Note(velocity=100, pitch=66, start=1.5, end=1.875)
sax_note2 = Note(velocity=100, pitch=68, start=1.875, end=2.25)
sax_note3 = Note(velocity=100, pitch=72, start=2.25, end=2.625)
sax.notes.append(sax_note1)
sax.notes.append(sax_note2)
sax.notes.append(sax_note3)

# -----------------------------
# BAR 3 (3.0 to 4.5 seconds): Bass walks, piano opens, sax continues

# BASS: Dm7 -> Am7
# Root: D (50), 5th: A (65)
# Chromatic approach: C# (63) before D

bass_note5 = Note(velocity=70, pitch=63, start=3.0, end=3.1875)  # C#
bass_note6 = Note(velocity=70, pitch=50, start=3.1875, end=3.375)  # D
bass_note7 = Note(velocity=70, pitch=65, start=3.375, end=3.5625)  # A
bass_note8 = Note(velocity=70, pitch=50, start=3.5625, end=3.75)  # D
bass.notes.append(bass_note5)
bass.notes.append(bass_note6)
bass.notes.append(bass_note7)
bass.notes.append(bass_note8)

# PIANO: Dm7 (D, F, A, C)
# Play D, F, A, C as a spread voicing

piano_note5 = Note(velocity=80, pitch=50, start=3.0, end=3.5)
piano_note6 = Note(velocity=80, pitch=52, start=3.0, end=3.5)
piano_note7 = Note(velocity=80, pitch=65, start=3.0, end=3.5)
piano_note8 = Note(velocity=80, pitch=60, start=3.0, end=3.5)
piano.notes.append(piano_note5)
piano.notes.append(piano_note6)
piano.notes.append(piano_note7)
piano.notes.append(piano_note8)

# SAX: Motif continues — rest then F again

sax_note4 = Note(velocity=100, pitch=66, start=3.5, end=3.875)
sax.notes.append(sax_note4)

# -----------------------------
# BAR 4 (4.5 to 6.0 seconds): Bass walks, piano opens, sax resolves

# BASS: Am7 -> Fm7
# Root: A (69), 5th: E (64)
# Chromatic approach: G (67) before A

bass_note9 = Note(velocity=70, pitch=67, start=4.5, end=4.6875)  # G
bass_note10 = Note(velocity=70, pitch=69, start=4.6875, end=4.875)  # A
bass_note11 = Note(velocity=70, pitch=64, start=4.875, end=5.0625)  # E
bass_note12 = Note(velocity=70, pitch=69, start=5.0625, end=5.25)  # A
bass.notes.append(bass_note9)
bass.notes.append(bass_note10)
bass.notes.append(bass_note11)
bass.notes.append(bass_note12)

# PIANO: Am7 (A, C, E, G)
# Play A, C, E, G as a spread voicing

piano_note9 = Note(velocity=80, pitch=69, start=4.5, end=5.0)
piano_note10 = Note(velocity=80, pitch=60, start=4.5, end=5.0)
piano_note11 = Note(velocity=80, pitch=64, start=4.5, end=5.0)
piano_note12 = Note(velocity=80, pitch=67, start=4.5, end=5.0)
piano.notes.append(piano_note9)
piano.notes.append(piano_note10)
piano.notes.append(piano_note11)
piano.notes.append(piano_note12)

# SAX: Finish the motif — F again, then end on a rest

sax_note5 = Note(velocity=100, pitch=66, start=5.0, end=5.375)
sax.notes.append(sax_note5)

# Output the MIDI file
pm.write("dante_intro.mid")
