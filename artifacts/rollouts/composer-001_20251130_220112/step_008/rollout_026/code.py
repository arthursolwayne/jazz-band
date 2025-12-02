
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
    # Hi-hat on every eighth
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

# Bar 2: Everyone in. Sax takes melody
# F7 chord: F A C E
# Sax motif: F - G - Bb - F (half note, quarter, eighth, eighth)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=3.0),  # F7 (half note)
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.75),  # G (quarter)
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),  # Bb (eighth)
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),  # F (eighth)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F minor
# F Eb D C Bb A G F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=80, pitch=59, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=57, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5),   # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Comp on 2 and 4 with 7th chords
# F7 on 2, Bb7 on 4
# F7 = F A C E
# Bb7 = Bb D F Ab
piano_notes = [
    # F7 on 2 (bar 2, beat 2)
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # E
    # Bb7 on 4 (bar 2, beat 4)
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375),  # Ab
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Continue pattern
# Sax repeats motif an octave higher
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=83, start=3.0, end=4.5),   # F7 (half note)
    pretty_midi.Note(velocity=110, pitch=84, start=4.5, end=5.25),  # G (quarter)
    pretty_midi.Note(velocity=110, pitch=81, start=5.25, end=5.625),  # Bb (eighth)
    pretty_midi.Note(velocity=110, pitch=83, start=5.625, end=6.0),  # F (eighth)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass continues walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=57, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),   # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Comp on 2 and 4 with 7th chords
# F7 on 2 (bar 3, beat 2)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # E
    # Bb7 on 4 (bar 3, beat 4)
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.875),  # Ab
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Repeat pattern
# Sax repeats motif an octave higher
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=83, start=4.5, end=6.0),   # F7 (half note)
    pretty_midi.Note(velocity=110, pitch=84, start=6.0, end=6.75),  # G (quarter)
    pretty_midi.Note(velocity=110, pitch=81, start=6.75, end=7.125),  # Bb (eighth)
    pretty_midi.Note(velocity=110, pitch=83, start=7.125, end=7.5),  # F (eighth)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass continues walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0),   # C
    pretty_midi.Note(velocity=80, pitch=59, start=6.0, end=6.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=57, start=6.375, end=6.75),  # A
    pretty_midi.Note(velocity=80, pitch=55, start=6.75, end=7.125),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=7.125, end=7.5),   # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Comp on 2 and 4 with 7th chords
# F7 on 2 (bar 4, beat 2)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # E
    # Bb7 on 4 (bar 4, beat 4)
    pretty_midi.Note(velocity=90, pitch=59, start=6.0, end=6.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=6.0, end=6.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=6.0, end=6.375),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=6.0, end=6.375),  # Ab
]

for note in piano_notes:
    piano.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')
