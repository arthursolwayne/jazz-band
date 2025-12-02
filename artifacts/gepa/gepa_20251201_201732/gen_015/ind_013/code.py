
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Time per bar at 160 BPM: 6 seconds for 4 bars (1.5 seconds per bar)
# Each beat = 0.375 seconds

bar_length = 1.5  # seconds per bar
beat_length = 0.375  # seconds per beat

# Create instruments
drums = Instrument(program=Program.DRUMS, is_drum=True)
bass = Instrument(program=Program.BASS_GUITAR, name="Marcus")
piano = Instrument(program=Program.ACOUSTIC_GRAND_PIANO, name="Diane")
sax = Instrument(program=Program.TENOR_SAX, name="Dante")

pm.instruments = [drums, bass, piano, sax]

# Drums: Little Ray
# Bar 1: Kick on 1 & 3, hihat on every eighth
# Bar 2-4: Same pattern, but with a fill at the end of bar 3

# Bar 1: Kick on 1 & 3, hihat on every eighth
for beat in [0, 2]:
    note = Note(velocity=100, pitch=36, start=beat * beat_length, end=beat * beat_length + 0.1)
    drums.notes.append(note)

# Hihat on every eighth
for i in range(8):
    note = Note(velocity=80, pitch=42, start=i * beat_length, end=i * beat_length + 0.05)
    drums.notes.append(note)

# Bar 2: Same as Bar 1
for beat in [0, 2]:
    note = Note(velocity=100, pitch=36, start=(bar_length + beat * beat_length), end=(bar_length + beat * beat_length + 0.1))
    drums.notes.append(note)

for i in range(8):
    note = Note(velocity=80, pitch=42, start=(bar_length + i * beat_length), end=(bar_length + i * beat_length + 0.05))
    drums.notes.append(note)

# Bar 3: Same pattern
for beat in [0, 2]:
    note = Note(velocity=100, pitch=36, start=(2 * bar_length + beat * beat_length), end=(2 * bar_length + beat * beat_length + 0.1))
    drums.notes.append(note)

for i in range(8):
    note = Note(velocity=80, pitch=42, start=(2 * bar_length + i * beat_length), end=(2 * bar_length + i * beat_length + 0.05))
    drums.notes.append(note)

# Bar 4: Same pattern, with a fill on the last beat
# Snare on 4 of 4th bar
note = Note(velocity=100, pitch=38, start=(3 * bar_length + 3 * beat_length), end=(3 * bar_length + 3 * beat_length + 0.1))
drums.notes.append(note)

# Hihat on every eighth
for i in range(8):
    note = Note(velocity=80, pitch=42, start=(3 * bar_length + i * beat_length), end=(3 * bar_length + i * beat_length + 0.05))
    drums.notes.append(note)

# Bass: Marcus (D2-G2, roots and fifths, chromatic approaches)
# Walking line in Dm (D-F-A-C)
# Bar 1: D2, F2, Ab2 (chromatic), A2
# Bar 2: C2, D2, F2, G2
# Bar 3: A2, Bb2 (chromatic), C2, D2
# Bar 4: F2, G2, A2, Bb2 (chromatic)

# Bar 1
note = Note(velocity=100, pitch=38, start=0, end=beat_length)
bass.notes.append(note)
note = Note(velocity=100, pitch=41, start=beat_length, end=2 * beat_length)
bass.notes.append(note)
note = Note(velocity=100, pitch=40, start=2 * beat_length, end=3 * beat_length)
bass.notes.append(note)
note = Note(velocity=100, pitch=43, start=3 * beat_length, end=bar_length)
bass.notes.append(note)

# Bar 2
note = Note(velocity=100, pitch=35, start=bar_length, end=bar_length + beat_length)
bass.notes.append(note)
note = Note(velocity=100, pitch=38, start=bar_length + beat_length, end=bar_length + 2 * beat_length)
bass.notes.append(note)
note = Note(velocity=100, pitch=41, start=bar_length + 2 * beat_length, end=bar_length + 3 * beat_length)
bass.notes.append(note)
note = Note(velocity=100, pitch=43, start=bar_length + 3 * beat_length, end=2 * bar_length)
bass.notes.append(note)

# Bar 3
note = Note(velocity=100, pitch=43, start=2 * bar_length, end=2 * bar_length + beat_length)
bass.notes.append(note)
note = Note(velocity=100, pitch=42, start=2 * bar_length + beat_length, end=2 * bar_length + 2 * beat_length)
bass.notes.append(note)
note = Note(velocity=100, pitch=35, start=2 * bar_length + 2 * beat_length, end=2 * bar_length + 3 * beat_length)
bass.notes.append(note)
note = Note(velocity=100, pitch=38, start=2 * bar_length + 3 * beat_length, end=3 * bar_length)
bass.notes.append(note)

# Bar 4
note = Note(velocity=100, pitch=41, start=3 * bar_length, end=3 * bar_length + beat_length)
bass.notes.append(note)
note = Note(velocity=100, pitch=43, start=3 * bar_length + beat_length, end=3 * bar_length + 2 * beat_length)
bass.notes.append(note)
note = Note(velocity=100, pitch=43, start=3 * bar_length + 2 * beat_length, end=3 * bar_length + 3 * beat_length)
bass.notes.append(note)
note = Note(velocity=100, pitch=42, start=3 * bar_length + 3 * beat_length, end=4 * bar_length)
bass.notes.append(note)

# Piano: Diane (open voicings, different chords each bar, comp on 2 and 4)
# Bar 1: Dm7 (D, F, A, C)
# Bar 2: F7 (F, A, C, Eb)
# Bar 3: A7 (A, C, E, G)
# Bar 4: C7 (C, E, G, Bb)

# Bar 1: Dm7 (D, F, A, C)
note = Note(velocity=90, pitch=62, start=0, end=beat_length)
piano.notes.append(note)
note = Note(velocity=90, pitch=65, start=0, end=beat_length)
piano.notes.append(note)
note = Note(velocity=90, pitch=67, start=0, end=beat_length)
piano.notes.append(note)
note = Note(velocity=90, pitch=69, start=0, end=beat_length)
piano.notes.append(note)

# Bar 2: F7 (F, A, C, Eb)
note = Note(velocity=90, pitch=65, start=bar_length, end=bar_length + beat_length)
piano.notes.append(note)
note = Note(velocity=90, pitch=67, start=bar_length, end=bar_length + beat_length)
piano.notes.append(note)
note = Note(velocity=90, pitch=69, start=bar_length, end=bar_length + beat_length)
piano.notes.append(note)
note = Note(velocity=90, pitch=70, start=bar_length, end=bar_length + beat_length)
piano.notes.append(note)

# Bar 3: A7 (A, C, E, G)
note = Note(velocity=90, pitch=69, start=2 * bar_length, end=2 * bar_length + beat_length)
piano.notes.append(note)
note = Note(velocity=90, pitch=69, start=2 * bar_length, end=2 * bar_length + beat_length)
piano.notes.append(note)
note = Note(velocity=90, pitch=71, start=2 * bar_length, end=2 * bar_length + beat_length)
piano.notes.append(note)
note = Note(velocity=90, pitch=72, start=2 * bar_length, end=2 * bar_length + beat_length)
piano.notes.append(note)

# Bar 4: C7 (C, E, G, Bb)
note = Note(velocity=90, pitch=60, start=3 * bar_length, end=3 * bar_length + beat_length)
piano.notes.append(note)
note = Note(velocity=90, pitch=64, start=3 * bar_length, end=3 * bar_length + beat_length)
piano.notes.append(note)
note = Note(velocity=90, pitch=67, start=3 * bar_length, end=3 * bar_length + beat_length)
piano.notes.append(note)
note = Note(velocity=90, pitch=69, start=3 * bar_length, end=3 * bar_length + beat_length)
piano.notes.append(note)

# Sax: You (melodic motif, one idea, leave it hanging, come back)
# Bar 1: Start with motif
# Bar 2: Rest
# Bar 3: Rest
# Bar 4: End with resolution

# Bar 1: D (62), F (65), A (67), rest
note = Note(velocity=100, pitch=62, start=0, end=beat_length)
sax.notes.append(note)
note = Note(velocity=100, pitch=65, start=beat_length, end=2 * beat_length)
sax.notes.append(note)
note = Note(velocity=100, pitch=67, start=2 * beat_length, end=3 * beat_length)
sax.notes.append(note)

# Bar 2: Rest
# Bar 3: Rest

# Bar 4: End with resolution (F (65), A (67), C (69), rest)
note = Note(velocity=100, pitch=65, start=3 * bar_length, end=3 * bar_length + beat_length)
sax.notes.append(note)
note = Note(velocity=100, pitch=67, start=3 * bar_length + beat_length, end=3 * bar_length + 2 * beat_length)
sax.notes.append(note)
note = Note(velocity=100, pitch=69, start=3 * bar_length + 2 * beat_length, end=3 * bar_length + 3 * beat_length)
sax.notes.append(note)

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file created: dante_intro.mid")
