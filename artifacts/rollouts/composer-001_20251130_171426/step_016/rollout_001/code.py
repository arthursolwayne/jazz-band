
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax takes the melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # F# (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=48, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=90, pitch=47, start=2.0, end=2.25),  # D#
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.5),  # C#
    pretty_midi.Note(velocity=90, pitch=46, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=48, start=2.75, end=3.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (7th chord on Dm7)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=1.75, end=2.0),  # D
    # Bar 2, beat 4 (7th chord on G7)
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.75, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=2.75, end=3.0),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax continues the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # F# (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=48, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=90, pitch=47, start=3.5, end=3.75),  # D#
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.0),  # C#
    pretty_midi.Note(velocity=90, pitch=46, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=48, start=4.25, end=4.5),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3, beat 2 (7th chord on Dm7)
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5),  # D
    # Bar 3, beat 4 (7th chord on G7)
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.25, end=4.5),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.25, end=4.5),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax finishes the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # F# (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=48, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=90, pitch=47, start=5.0, end=5.25),  # D#
    pretty_midi.Note(velocity=90, pitch=45, start=5.25, end=5.5),  # C#
    pretty_midi.Note(velocity=90, pitch=46, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=48, start=5.75, end=6.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, beat 2 (7th chord on Dm7)
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.75, end=5.0),  # D
    # Bar 4, beat 4 (7th chord on G7)
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=5.75, end=6.0),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=5.75, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=5.75, end=6.0),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Drums in bar 3 and 4
# Bar 3
for i in range(3):
    drum_start = 3.0 + i * 0.375
    pretty_midi.Note(velocity=100, pitch=42, start=drum_start, end=drum_start + 0.375)
    if i % 2 == 0:
        pretty_midi.Note(velocity=100, pitch=36, start=drum_start, end=drum_start + 0.375)
    else:
        pretty_midi.Note(velocity=100, pitch=38, start=drum_start, end=drum_start + 0.375)

# Bar 4
for i in range(3):
    drum_start = 4.5 + i * 0.375
    pretty_midi.Note(velocity=100, pitch=42, start=drum_start, end=drum_start + 0.375)
    if i % 2 == 0:
        pretty_midi.Note(velocity=100, pitch=36, start=drum_start, end=drum_start + 0.375)
    else:
        pretty_midi.Note(velocity=100, pitch=38, start=drum_start, end=drum_start + 0.375)

# Add all instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
