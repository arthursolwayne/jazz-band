
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    # D (2nd fret low E) at 1.5s
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    
    # C# (1st fret low E) at 1.875s
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),
    
    # E (4th fret low E) at 2.25s
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),
    
    # F (5th fret low E) at 2.625s
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # D7 on 2 (1.875s)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # C
    
    # G7 on 4 (2.625s)
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=78, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=80, start=2.625, end=3.0),  # F#
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif - short, singable, starts at 1.5s
sax_notes = [
    # D (1.5s)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),
    
    # F# (1.6875s)
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875),
    
    # A (1.875s)
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.0625),
    
    # D (2.0625s)
    pretty_midi.Note(velocity=110, pitch=62, start=2.0625, end=2.25)
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3 (3.0 - 4.5s)

# Drums: same pattern
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
    drums.notes.append(note)

# Bass: continue walking line
bass_notes = [
    # F (5th fret low E) at 3.0s
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),
    
    # E (4th fret low E) at 3.375s
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),
    
    # G (6th fret low E) at 3.75s
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
    
    # A (7th fret low E) at 4.125s
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: comp on 2 and 4
piano_notes = [
    # E7 on 2 (3.375s)
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # G#
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # D
    
    # A7 on 4 (4.125s)
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=4.125, end=4.5),  # C#
    pretty_midi.Note(velocity=100, pitch=79, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=100, pitch=81, start=4.125, end=4.5),  # G
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: repeat motif with variation (start at 3.0s)
sax_notes = [
    # D (3.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),
    
    # F# (3.1875s)
    pretty_midi.Note(velocity=110, pitch=67, start=3.1875, end=3.375),
    
    # A (3.375s)
    pretty_midi.Note(velocity=110, pitch=72, start=3.375, end=3.5625),
    
    # D (3.5625s)
    pretty_midi.Note(velocity=110, pitch=62, start=3.5625, end=3.75)
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4 (4.5 - 6.0s)

# Drums: same pattern
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
    drums.notes.append(note)

# Bass: finish walking line
bass_notes = [
    # B (8th fret low E) at 4.5s
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    
    # C (9th fret low E) at 4.875s
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),
    
    # D (10th fret low E) at 5.25s
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),
    
    # F# (12th fret low E) at 5.625s
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: comp on 2 and 4
piano_notes = [
    # F#7 on 2 (4.875s)
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25),  # D
    
    # G7 on 4 (5.625s)
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),  # B
    pretty_midi.Note(velocity=100, pitch=78, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=80, start=5.625, end=6.0),  # F#
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: finish motif, return to start
sax_notes = [
    # D (4.5s)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),
    
    # F# (4.6875s)
    pretty_midi.Note(velocity=110, pitch=67, start=4.6875, end=4.875),
    
    # A (4.875s)
    pretty_midi.Note(velocity=110, pitch=72, start=4.875, end=5.0625),
    
    # D (5.0625s)
    pretty_midi.Note(velocity=110, pitch=62, start=5.0625, end=5.25)
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("intro_wayne.mid")
