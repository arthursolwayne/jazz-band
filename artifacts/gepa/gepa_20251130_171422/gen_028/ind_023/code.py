
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to D minor (key signature: 1 flat)
pm.key_signature = pretty_midi.KeySignature(key=pretty_midi.KEY_D_MINOR)

# Create instruments
bass_program = Program(33, 0)  # Electric Bass
piano_program = Program(0, 0)  # Acoustic Piano
drums_program = Program(10, 0)  # Drums
sax_program = Program(62, 0)  # Tenor Saxophone

# Create instruments and add to the MIDI file
bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
drums = Instrument(program=drums_program)
sax = Instrument(program=sax_program)

pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)
pm.instruments.append(sax)

# Define the beat duration in seconds (160 BPM = 60/160 = 0.375 sec per beat)
beat = 0.375

# Define note durations and timing
note_quarter = beat
note_eighth = beat / 2
note_sixteenth = beat / 4

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Slight dynamic variation in hihat and snare

# Bar 1: 0.0 to 1.5 seconds

# Kick on 1 (0.0)
drums.notes.append(Note(36, 80, 0.0, note_quarter))
# Kick on 3 (1.5 - 0.0 = 1.5, 1.5 - 0.75 = 0.75)
drums.notes.append(Note(36, 80, 1.5 - 0.75, note_quarter))

# Snare on 2 (0.75)
drums.notes.append(Note(38, 85, 0.75, note_quarter))
# Snare on 4 (1.5)
drums.notes.append(Note(38, 85, 1.5, note_quarter))

# Hihat on every eighth
hihat_velocity = [85, 80, 85, 80, 85, 80, 85, 80]
hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]
for i in range(8):
    drums.notes.append(Note(42, hihat_velocity[i], hihat_times[i], note_sixteenth))

# Bar 2: All instruments join
# Time starts at 1.5 seconds

# Bass line: walking line with chromatic approaches
# Dm7: D, F, A, C
# Bass notes: D, F, Eb, G, A, Bb, B, C
bass_notes = [
    (0.0, 62),  # D
    (0.375, 65),  # F
    (0.75, 63),  # Eb
    (1.125, 67),  # G
    (1.5, 69),  # A
    (1.875, 67),  # Bb
    (2.25, 71),  # B
    (2.625, 72)  # C
]
for time, pitch in bass_notes:
    bass.notes.append(Note(pitch, 90, time + 1.5, note_sixteenth))

# Piano comp: 7th chords on 2 and 4
# Dm7: D, F, A, C
# Left hand: root (D), 7th (C), 5th (A)
piano_notes = [
    (0.75, 62),  # D
    (0.75, 67),  # A
    (0.75, 72),  # C
    (1.5, 62),  # D
    (1.5, 67),  # A
    (1.5, 72),  # C
]
for time, pitch in piano_notes:
    piano.notes.append(Note(pitch, 95, time + 1.5, note_quarter))

# Drums: same pattern, slightly louder
# Kick on 1 and 3
drums.notes.append(Note(36, 85, 1.5, note_quarter))
drums.notes.append(Note(36, 85, 2.25, note_quarter))
# Snare on 2 and 4
drums.notes.append(Note(38, 90, 1.875, note_quarter))
drums.notes.append(Note(38, 90, 2.625, note_quarter))
# Hihat: same pattern
for i in range(8):
    drums.notes.append(Note(42, hihat_velocity[i], hihat_times[i] + 1.5, note_sixteenth))

# Saxophone motif: Dmi7, concise, emotional
# Dmi7: D, F, A, C
# Motif: D - F - A - D (chromatic approach to A)
# D (D), F (F), A (A), D (D), rest, then D (D), F (F), A (A), D (D)
sax_notes = [
    (0.0, 62),  # D
    (0.375, 65),  # F
    (0.75, 69),  # A
    (1.125, 62),  # D
    (1.5, 62),  # Rest
    (1.875, 62),  # D
    (2.25, 65),  # F
    (2.625, 69),  # A
    (3.0, 62)  # D
]
for time, pitch in sax_notes:
    sax.notes.append(Note(pitch, 100, time + 1.5, note_sixteenth))

# Bar 4: Repeat of bar 2, but with slight variation in piano and sax
# Piano: same chords, but a bit more aggressive
piano_notes_bar4 = [
    (0.75, 62),
    (0.75, 67),
    (0.75, 72),
    (1.5, 62),
    (1.5, 67),
    (1.5, 72)
]
for time, pitch in piano_notes_bar4:
    piano.notes.append(Note(pitch, 100, time + 3.0, note_quarter))

# Saxophone: same motif, but with a slight variation in rhythm
sax_notes_bar4 = [
    (0.0, 62),
    (0.375, 65),
    (0.75, 69),
    (1.5, 62),
    (1.875, 62),
    (2.25, 65),
    (2.625, 69),
    (3.0, 62)
]
for time, pitch in sax_notes_bar4:
    sax.notes.append(Note(pitch, 100, time + 3.0, note_sixteenth))

# Save the MIDI file
pm.write("dante_intro.mid")
