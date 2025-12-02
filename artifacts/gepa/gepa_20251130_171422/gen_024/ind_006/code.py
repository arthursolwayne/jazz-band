
import pretty_midi

# Initialize MIDI file with tempo and instruments
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Create a questioning, open rhythm
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=85, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=85, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: F (C#) - Bb - G - D (resolve to F on beat 4)
# F = 65, Bb = 62, G = 67, D = 62
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=3.0),  # F (resolve)
]

# Bass: Walking line in F minor, chromatic
# F - Gb - G - A (F minor scale)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=70, pitch=66, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=70, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=70, pitch=69, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=70, pitch=65, start=2.5, end=3.0),  # F (resolve)
]

# Piano: 7th chords on 2 and 4
# F7 (F, A, C, Eb) on beat 2
# G7 (G, B, D, F) on beat 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=2.5, end=2.75),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=2.5, end=2.75),  # F
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif, but with slight variation (Bb -> Ab)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.5),  # F (resolve)
]

# Bass: Walking line, chromatic again
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=70, pitch=66, start=3.25, end=3.5),  # Gb
    pretty_midi.Note(velocity=70, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=70, pitch=68, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=70, pitch=65, start=4.0, end=4.5),  # F (resolve)
]

# Piano: 7th chords again
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=80, pitch=65, start=4.0, end=4.25),  # F
]

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End with a rest, then a resolution — the question answered
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.0),  # F
]

# Bass: End with a downbeat on F
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=65, start=4.5, end=5.0),  # F
]

# Piano: Final chord on the last beat
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0),  # Eb
]

# Add notes to instruments
for note in sax_notes:
    sax.notes.append(note)

for note in bass_notes:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

# Add drum notes from earlier
for note in drum_notes:
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
