
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Set tempo and time signature
BPM = 160
TIME_SIGNATURE = (4, 4)
NOTE_DURATION = 0.375  # seconds per beat at 160 BPM
BAR_DURATION = 1.5     # seconds per bar

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=BPM)
midi.time_signature_changes = [pretty_midi.TimeSignatureChange(time=0, numerator=4, denominator=4)]

# Define instruments
drums = Instrument(program=Program.DRUMS, is_drum=True)
bass = Instrument(program=Program.BASS, name="Bass")
piano = Instrument(program=Program.PIANO, name="Piano")
sax = Instrument(program=Program.SAXOPHONE, name="Tenor Sax")

# Add to MIDI
midi.instruments = [drums, bass, piano, sax]

# -------------------------------
# 1. DRUMS (Little Ray)
# -------------------------------
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2-4: Same, but with slight dynamic variation and ghost notes

# Bar 1
drums.notes.append(Note(36, 100, 0, NOTE_DURATION))  # Kick on 1
drums.notes.append(Note(38, 100, NOTE_DURATION, NOTE_DURATION))  # Snare on 2
drums.notes.append(Note(42, 80, 0, NOTE_DURATION))    # Hihat on 1
drums.notes.append(Note(42, 80, NOTE_DURATION / 2, NOTE_DURATION))  # Hihat on 1.5
drums.notes.append(Note(42, 80, NOTE_DURATION, NOTE_DURATION))    # Hihat on 2
drums.notes.append(Note(42, 80, 1.5, NOTE_DURATION))    # Hihat on 3
drums.notes.append(Note(42, 80, 2, NOTE_DURATION))     # Hihat on 3.5
drums.notes.append(Note(42, 80, 2.5, NOTE_DURATION))   # Hihat on 4

# Bar 2 (Kick on 1 and 3)
drums.notes.append(Note(36, 100, 1.5, NOTE_DURATION))
drums.notes.append(Note(38, 100, 2, NOTE_DURATION))
drums.notes.append(Note(42, 70, 1.5, NOTE_DURATION))
drums.notes.append(Note(42, 70, 2, NOTE_DURATION))
drums.notes.append(Note(42, 70, 2.5, NOTE_DURATION))
drums.notes.append(Note(42, 70, 3, NOTE_DURATION))
drums.notes.append(Note(42, 70, 3.5, NOTE_DURATION))
drums.notes.append(Note(42, 70, 4, NOTE_DURATION))

# Bar 3
drums.notes.append(Note(36, 100, 3, NOTE_DURATION))
drums.notes.append(Note(38, 100, 3.5, NOTE_DURATION))
drums.notes.append(Note(42, 80, 3, NOTE_DURATION))
drums.notes.append(Note(42, 80, 3.5, NOTE_DURATION))
drums.notes.append(Note(42, 80, 4, NOTE_DURATION))
drums.notes.append(Note(42, 80, 4.5, NOTE_DURATION))
drums.notes.append(Note(42, 80, 5, NOTE_DURATION))
drums.notes.append(Note(42, 80, 5.5, NOTE_DURATION))

# Bar 4
drums.notes.append(Note(36, 100, 4.5, NOTE_DURATION))
drums.notes.append(Note(38, 100, 5, NOTE_DURATION))
drums.notes.append(Note(42, 70, 4.5, NOTE_DURATION))
drums.notes.append(Note(42, 70, 5, NOTE_DURATION))
drums.notes.append(Note(42, 70, 5.5, NOTE_DURATION))
drums.notes.append(Note(42, 70, 6, NOTE_DURATION))
drums.notes.append(Note(42, 70, 6.5, NOTE_DURATION))
drums.notes.append(Note(42, 70, 7, NOTE_DURATION))

# -------------------------------
# 2. BASS (Marcus)
# -------------------------------
# Bar 1: Dm7 walking line: D - C - Bb - A - G - F - E - D
# Use chromatic approaches

bass_notes = [62, 60, 59, 57, 55, 53, 52, 62]
for i, pitch in enumerate(bass_notes):
    start = i * NOTE_DURATION
    bass.notes.append(Note(pitch, 100, start, NOTE_DURATION))

# Bar 2: D - C - Bb - A - G - F - E - D
for i, pitch in enumerate(bass_notes):
    start = (i + 4) * NOTE_DURATION
    bass.notes.append(Note(pitch, 100, start, NOTE_DURATION))

# Bar 3: D - C - Bb - A - G - F - E - D
for i, pitch in enumerate(bass_notes):
    start = (i + 8) * NOTE_DURATION
    bass.notes.append(Note(pitch, 100, start, NOTE_DURATION))

# Bar 4: D - C - Bb - A - G - F - E - D
for i, pitch in enumerate(bass_notes):
    start = (i + 12) * NOTE_DURATION
    bass.notes.append(Note(pitch, 100, start, NOTE_DURATION))

# -------------------------------
# 3. PIANO (Diane)
# -------------------------------
# Bars 2-4: 7th chords, comp on 2 and 4

# Dm7 (D, F, A, C)
chord_notes = [62, 64, 67, 69]
# Comp on 2 and 4 of each bar

def comp_chord(time):
    for p in chord_notes:
        piano.notes.append(Note(p, 100, time, NOTE_DURATION / 2))

# Bar 2, beat 2
comp_chord(2)
# Bar 2, beat 4
comp_chord(4)

# Bar 3, beat 2
comp_chord(6)
# Bar 3, beat 4
comp_chord(8)

# Bar 4, beat 2
comp_chord(10)
# Bar 4, beat 4
comp_chord(12)

# -------------------------------
# 4. SAX (You)
# -------------------------------
# Bar 1: Rest
# Bar 2: Start motif — searching, deliberate, with space

# Bar 2: Motif: D - Bb - D - C (searching, 4 notes over 2 beats)
sax_notes = [62, 59, 62, 60]
for i, pitch in enumerate(sax_notes):
    start = (i + 4) * NOTE_DURATION  # Start on beat 2 of bar 2
    sax.notes.append(Note(pitch, 110, start, NOTE_DURATION / 2))

# Bar 3: Answer — a bit more complete, still searching
# C - Bb - C - D
sax_notes = [60, 59, 60, 62]
for i, pitch in enumerate(sax_notes):
    start = (i + 6) * NOTE_DURATION  # Start on beat 2 of bar 3
    sax.notes.append(Note(pitch, 110, start, NOTE_DURATION / 2))

# Bar 4: Resolve forward — no resolution, just tension
# D - C - D - F
sax_notes = [62, 60, 62, 64]
for i, pitch in enumerate(sax_notes):
    start = (i + 8) * NOTE_DURATION  # Start on beat 2 of bar 4
    sax.notes.append(Note(pitch, 110, start, NOTE_DURATION / 2))

# Save the MIDI
midi.write("dante_cellar_intro.mid")

print("MIDI file 'dante_cellar_intro.mid' created.")
print("Play it — make Wayne lean forward.")
