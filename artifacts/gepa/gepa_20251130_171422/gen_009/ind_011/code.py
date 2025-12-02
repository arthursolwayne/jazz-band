
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)  # 160 BPM

# Create instruments
drums = Instrument(program=Program.DRUMS, is_drum=True)
bass = Instrument(program=Program.BASS_GUITAR)
piano = Instrument(program=Program.ELECTRIC_PIANO_1)
sax = Instrument(program=Program.TENOR_SAX)

pm.instruments = [drums, bass, piano, sax]

# Time per bar (seconds) = 60 / 160 * 4
bar_duration = 60.0 / 160 * 4  # 1.5 seconds per bar
note_duration = 0.375  # One beat in 4/4 at 160 BPM is 0.375 seconds
half_note = note_duration * 2
quarter_note = note_duration
eighth_note = note_duration / 2

# ---------------------------
# Bar 1: Little Ray (Drums) — 4/4, 4 beats. Hi-hat on every 8th, kick on 1 and 3, snare on 2 and 4
# ---------------------------

# Kick on 1 and 3
drums.notes.append(Note(36, 60, 0, note_duration))  # Kick on 1
drums.notes.append(Note(36, 60, 2 * note_duration, note_duration))  # Kick on 3

# Snare on 2 and 4
drums.notes.append(Note(38, 60, 1 * note_duration, note_duration))  # Snare on 2
drums.notes.append(Note(38, 60, 3 * note_duration, note_duration))  # Snare on 4

# Hi-hat on every 8th
for i in range(8):
    drums.notes.append(Note(42, 60, i * eighth_note, eighth_note * 0.25))  # 25% duration for hi-hat

# ---------------------------
# Bar 2: Everyone in — Melody on sax, chords on piano, walking bass
# ---------------------------

# Sax tenor: Short motif — starts on B (F7 chord)
# Motif: B -> G -> A -> B (to end the phrase)
sax.notes.append(Note(71, 100, 1.5, 0.375))  # B (1st beat)
sax.notes.append(Note(67, 100, 1.875, 0.375))  # G (2nd beat)
sax.notes.append(Note(69, 100, 2.25, 0.375))   # A (3rd beat)
sax.notes.append(Note(71, 100, 2.625, 0.375))  # B (4th beat)

# Piano: 7th chords, comp on 2 and 4 in F7
# F7 = F A C E♭
# Chord on 2 (beat 2) and 4 (beat 4)
# F7 on beat 2 (start at 1.875)
# F7 on beat 4 (start at 2.625)
# Each chord: 1/4 note duration
piano.notes.append(Note(65, 100, 1.875, 0.375))  # F
piano.notes.append(Note(69, 100, 1.875, 0.375))  # A
piano.notes.append(Note(72, 100, 1.875, 0.375))  # C
piano.notes.append(Note(64, 100, 1.875, 0.375))  # E♭

piano.notes.append(Note(65, 100, 2.625, 0.375))  # F
piano.notes.append(Note(69, 100, 2.625, 0.375))  # A
piano.notes.append(Note(72, 100, 2.625, 0.375))  # C
piano.notes.append(Note(64, 100, 2.625, 0.375))  # E♭

# Bass: Walking line in F7 — chromatic approach
# F (65) -> G♭ (66) -> G (67) -> A♭ (68) -> A (69)
bass.notes.append(Note(65, 60, 1.5, 0.375))  # F
bass.notes.append(Note(66, 60, 1.875, 0.375))  # G♭
bass.notes.append(Note(67, 60, 2.25, 0.375))   # G
bass.notes.append(Note(68, 60, 2.625, 0.375))  # A♭

# ---------------------------
# Write to file
# ---------------------------

pm.write('dante_intro.mid')
print("MIDI file generated: 'dante_intro.mid'")
