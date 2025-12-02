
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=0.0, end=0.375),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=56, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=90, pitch=57, start=1.75, end=1.875), # E
    pretty_midi.Note(velocity=90, pitch=59, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.125),  # G#
    pretty_midi.Note(velocity=90, pitch=62, start=2.125, end=2.25), # A#
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.375), # A#
    pretty_midi.Note(velocity=90, pitch=60, start=2.375, end=2.5),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),   # A
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.75),   # C#
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),   # F#
    pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=1.75),   # A
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),   # A
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),   # C#
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5),   # F#
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.5),   # A
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: sparse, expressive motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # A
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.125),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5),  # A
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=65, start=3.125, end=3.25), # B
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.375), # C#
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.5),  # D#
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.625),  # F#
    pretty_midi.Note(velocity=90, pitch=72, start=3.625, end=3.75), # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=3.875), # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.875, end=4.0),  # F#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.25),   # A
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),   # C#
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.25),   # F#
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.25),   # A
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0),   # A
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),   # C#
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0),   # F#
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.0),   # A
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: sparse, expressive motif (continue)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),   # C#
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.625),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0),  # C#
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bass: walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.625),  # D#
    pretty_midi.Note(velocity=90, pitch=71, start=4.625, end=4.75), # F#
    pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=4.875), # G
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=5.0, end=5.125),  # B
    pretty_midi.Note(velocity=90, pitch=77, start=5.125, end=5.25), # B#
    pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.375), # B#
    pretty_midi.Note(velocity=90, pitch=76, start=5.375, end=5.5),  # B
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.75),   # A
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),   # C#
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75),   # F#
    pretty_midi.Note(velocity=80, pitch=74, start=4.5, end=4.75),   # A
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5),   # A
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5),   # C#
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.5),   # F#
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.5),   # A
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: sparse, expressive motif (finish)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.125),  # C#
    pretty_midi.Note(velocity=100, pitch=74, start=5.375, end=5.5),  # A
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
