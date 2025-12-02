
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Sax enters with a short motif (1.5 - 3.0s)
sax_notes = [
    # Start with a whisper: Fm7 = F, Ab, Bb, D
    pretty_midi.Note(velocity=85, pitch=64, start=1.5, end=1.75),    # F
    pretty_midi.Note(velocity=85, pitch=61, start=1.75, end=2.0),   # Ab
    pretty_midi.Note(velocity=85, pitch=62, start=2.0, end=2.25),   # Bb
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.5),   # D
    # Leave it hanging
    pretty_midi.Note(velocity=85, pitch=64, start=2.5, end=2.75),   # F
    pretty_midi.Note(velocity=85, pitch=61, start=2.75, end=3.0),   # Ab
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 2: Bass enters with walking line (1.5 - 3.0s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),    # F
    pretty_midi.Note(velocity=80, pitch=43, start=1.75, end=2.0),    # Eb
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),    # G
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.5),    # F
    pretty_midi.Note(velocity=80, pitch=46, start=2.5, end=2.75),    # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=2.75, end=3.0),    # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Bar 2: Piano enters with comping on 2 and 4 (1.5 - 3.0s)
piano_notes = [
    # 7th chords: Fm7 = F, Ab, Bb, D
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),    # F
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=2.0),    # Ab
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0),    # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),    # D
    # 2nd bar
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=3.0),    # F
    pretty_midi.Note(velocity=80, pitch=61, start=2.75, end=3.0),    # Ab
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=3.0),    # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),    # D
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Sax continues with a cry (3.0 - 4.5s)
sax_notes = [
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.25),    # A
    pretty_midi.Note(velocity=95, pitch=66, start=3.25, end=3.5),    # G
    pretty_midi.Note(velocity=95, pitch=67, start=3.5, end=3.75),    # Ab
    pretty_midi.Note(velocity=95, pitch=72, start=3.75, end=4.0),    # C
    pretty_midi.Note(velocity=95, pitch=64, start=4.0, end=4.25),    # F
    pretty_midi.Note(velocity=95, pitch=61, start=4.25, end=4.5),    # Ab
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Bass continues with walking line (3.0 - 4.5s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.25),    # Bb
    pretty_midi.Note(velocity=80, pitch=46, start=3.25, end=3.5),    # Ab
    pretty_midi.Note(velocity=80, pitch=49, start=3.5, end=3.75),    # C
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.0),    # F
    pretty_midi.Note(velocity=80, pitch=47, start=4.0, end=4.25),    # G
    pretty_midi.Note(velocity=80, pitch=45, start=4.25, end=4.5),    # F
]

for note in bass_notes:
    bass.notes.append(note)

# Bar 3: Piano continues with comping on 2 and 4 (3.0 - 4.5s)
piano_notes = [
    # 7th chords: Fm7 = F, Ab, Bb, D
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),    # F
    pretty_midi.Note(velocity=80, pitch=61, start=3.25, end=3.5),    # Ab
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),    # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5),    # D
    # 2nd bar
    pretty_midi.Note(velocity=80, pitch=64, start=4.25, end=4.5),    # F
    pretty_midi.Note(velocity=80, pitch=61, start=4.25, end=4.5),    # Ab
    pretty_midi.Note(velocity=80, pitch=62, start=4.25, end=4.5),    # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=4.25, end=4.5),    # D
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Sax finishes (4.5 - 6.0s)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=100, pitch=61, start=4.75, end=5.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),   # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),   # A
    pretty_midi.Note(velocity=100, pitch=66, start=5.75, end=6.0),   # G
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Bass finishes with walking line (4.5 - 6.0s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.75),    # F
    pretty_midi.Note(velocity=80, pitch=43, start=4.75, end=5.0),    # Eb
    pretty_midi.Note(velocity=80, pitch=47, start=5.0, end=5.25),    # G
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.5),    # F
    pretty_midi.Note(velocity=80, pitch=46, start=5.5, end=5.75),    # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=5.75, end=6.0),    # Bb
]

for note in bass_notes:
    bass.notes.append(note)

# Bar 4: Piano finishes with comping on 2 and 4 (4.5 - 6.0s)
piano_notes = [
    # 7th chords: Fm7 = F, Ab, Bb, D
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),    # F
    pretty_midi.Note(velocity=80, pitch=61, start=4.75, end=5.0),    # Ab
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0),    # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=5.0),    # D
    # 2nd bar
    pretty_midi.Note(velocity=80, pitch=64, start=5.75, end=6.0),    # F
    pretty_midi.Note(velocity=80, pitch=61, start=5.75, end=6.0),    # Ab
    pretty_midi.Note(velocity=80, pitch=62, start=5.75, end=6.0),    # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=5.75, end=6.0),    # D
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Drums continue (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')
