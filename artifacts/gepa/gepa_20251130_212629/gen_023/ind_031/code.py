
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

# Kick on 1 and 3, snare on 2 and 4
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    
    # Hihat on every eighth, with slight timing variations
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=60, pitch=42, start=1.875, end=2.0625),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=63, start=2.625, end=3.0), # D#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on bar 2
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625), # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif - start on D, play a triplet with a rest between notes
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0), # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5), # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=63, start=4.125, end=4.5), # D#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125), # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25), # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5), # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0), # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25), # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=63, start=5.625, end=6.0), # D#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625), # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif with a rest at the end, leaving it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75), # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5), # D
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=80, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625),
    
    # Hihat on every eighth, with slight timing variations
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=60, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=60, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=60, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=60, pitch=42, start=5.8125, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
