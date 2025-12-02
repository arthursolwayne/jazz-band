
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
bar_length = 1.5  # seconds
notes_per_bar = 8  # 160 BPM, 4/4 time = 8 eighth notes per bar
note_duration = bar_length / notes_per_bar

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.0 + note_duration))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0 * note_duration, end=3.0 * note_duration + note_duration))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=2.0 * note_duration, end=2.0 * note_duration + note_duration))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=6.0 * note_duration, end=6.0 * note_duration + note_duration))

# Hi-hat on every eighth
for i in range(notes_per_bar):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i * note_duration, end=i * note_duration + note_duration))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (walking, chromatic)
bass_notes = [
    (1.5, 64, 100),  # F
    (1.75, 65, 100),  # F#
    (2.0, 65, 100),   # F#
    (2.25, 64, 100),  # F
    (2.5, 62, 100),   # D
    (2.75, 63, 100),  # D#
    (3.0, 63, 100),   # D#
    (3.25, 62, 100),  # D
    (3.5, 60, 100),   # Bb
    (3.75, 61, 100),  # B
    (4.0, 61, 100),   # B
    (4.25, 60, 100),  # Bb
    (4.5, 58, 100),   # G
    (4.75, 59, 100),  # G#
    (5.0, 59, 100),   # G#
    (5.25, 58, 100),  # G
    (5.5, 57, 100),   # F
    (5.75, 58, 100),  # F#
    (6.0, 58, 100),   # F#
]

for start, pitch, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + note_duration))

# Piano: 7th chords on beats 2 and 4
# Bar 2: Bb7 (Fm key)
piano.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.0 + note_duration))  # Bb
piano.notes.append(pretty_midi.Note(velocity=110, pitch=73, start=2.0, end=2.0 + note_duration))  # D
piano.notes.append(pretty_midi.Note(velocity=110, pitch=74, start=2.0, end=2.0 + note_duration))  # Eb
piano.notes.append(pretty_midi.Note(velocity=110, pitch=78, start=2.0, end=2.0 + note_duration))  # G

# Bar 3: C7
piano.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=4.0, end=4.0 + note_duration))  # C
piano.notes.append(pretty_midi.Note(velocity=110, pitch=74, start=4.0, end=4.0 + note_duration))  # Eb
piano.notes.append(pretty_midi.Note(velocity=110, pitch=75, start=4.0, end=4.0 + note_duration))  # E
piano.notes.append(pretty_midi.Note(velocity=110, pitch=79, start=4.0, end=4.0 + note_duration))  # G

# Bar 4: Ab7
piano.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=6.0, end=6.0 + note_duration))  # Ab
piano.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=6.0, end=6.0 + note_duration))  # C
piano.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=6.0, end=6.0 + note_duration))  # C#
piano.notes.append(pretty_midi.Note(velocity=110, pitch=76, start=6.0, end=6.0 + note_duration))  # E

# Saxophone: Melody (Bar 2-4)
# Start on F, move to G, Bb, then end on D (a question)
sax_notes = [
    (1.5, 64, 100),  # F
    (1.75, 66, 100),  # G
    (2.0, 62, 100),  # Bb
    (2.25, 64, 100),  # F
    (2.5, 66, 100),  # G
    (2.75, 62, 100),  # Bb
    (3.0, 64, 100),  # F
    (3.25, 66, 100),  # G
    (3.5, 62, 100),  # Bb
    (3.75, 64, 100),  # F
    (4.0, 66, 100),  # G
    (4.25, 62, 100),  # Bb
    (4.5, 65, 100),  # C
    (4.75, 62, 100),  # Bb
    (5.0, 64, 100),  # F
    (5.25, 66, 100),  # G
    (5.5, 61, 100),  # D
    (5.75, 61, 100),  # D
    (6.0, 61, 100),  # D
]

for start, pitch, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + note_duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
