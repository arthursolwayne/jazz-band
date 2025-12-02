
import pretty_midi

# Create a MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the instruments
sax = pretty_midi.Instrument(program=66)       # Alto Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Acoustic Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42, open hihat=46, ride=51

# === Bar 1: Drums only (0.0 - 1.5s) ===
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
    # Subtle syncopation on the hihat for tension
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.75)
]

for note in drum_notes:
    drums.notes.append(note)

# === Bar 2: Full quartet (1.5 - 3.0s) ===

# Sax: Start the motif - short, melodic, with space
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),     # D7 - F#
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=2.0),     # D7 - C#
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),     # D7 - F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),     # D7 - A
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),     # D7 - F#
    pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0),     # D7 - C#
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75),      # D7 - F#
    pretty_midi.Note(velocity=80, pitch=65, start=1.75, end=2.0),      # D7 - F#
    pretty_midi.Note(velocity=80, pitch=63, start=2.0, end=2.25),      # D7 - E
    pretty_midi.Note(velocity=80, pitch=66, start=2.25, end=2.5),      # D7 - G
    pretty_midi.Note(velocity=80, pitch=68, start=2.5, end=2.75),      # D7 - A
    pretty_midi.Note(velocity=80, pitch=66, start=2.75, end=3.0),      # D7 - G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4. Stay out of your way but keep it moving
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.75),      # D7 - F#
    pretty_midi.Note(velocity=85, pitch=72, start=1.5, end=1.75),      # D7 - C#
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=1.75),      # D7 - A
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=1.75),      # D7 - D
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.5),      # D7 - F#
    pretty_midi.Note(velocity=85, pitch=72, start=2.25, end=2.5),      # D7 - C#
    pretty_midi.Note(velocity=85, pitch=69, start=2.25, end=2.5),      # D7 - A
    pretty_midi.Note(velocity=85, pitch=64, start=2.25, end=2.5),      # D7 - D
]

for note in piano_notes:
    piano.notes.append(note)

# === Bar 3 and 4: Repeat of bar 2 (3.0 - 4.5s) ===
# Repeat sax and bass notes shifted by 1.5s
for note in sax_notes:
    note.start += 1.5
    note.end += 1.5
    sax.notes.append(note)

for note in bass_notes:
    note.start += 1.5
    note.end += 1.5
    bass.notes.append(note)

for note in piano_notes:
    note.start += 1.5
    note.end += 1.5
    piano.notes.append(note)

# === Bar 3: Add drum fill ===
# Snare fill on beat 3
pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5)
# Hi-hat fill
pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.6875)
pretty_midi.Note(velocity=90, pitch=42, start=3.6875, end=3.875)
pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0)
# Kick and snare on beat 4
pretty_midi.Note(velocity=100, pitch=36, start=3.875, end=4.0)
pretty_midi.Note(velocity=110, pitch=38, start=4.0, end=4.125)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_in_d.mid")
