
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in D (D F# A C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25), # F#
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Diane - 7th chords on 2 and 4 (comping)
# D7 = D F# A C
# G7 = G B D F
# A7 = A C# E G
# Bm7 = B D F# A
piano_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # C

    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625), # F

    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # C#
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G

    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=81, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.125), # A

    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # G

    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=100, pitch=81, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=76, start=5.25, end=5.625), # F#
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.625), # A
]
for note in piano_notes:
    piano.notes.append(note)

# Dante - Tenor sax melody
# One short motif: D, F#, A, B (starts at 1.5s)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75), # F#
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875), # A
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0),  # B

    # Rest for a beat (2.0 - 2.5s)
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.75), # F#
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=2.875), # A
    pretty_midi.Note(velocity=110, pitch=71, start=2.875, end=3.0),  # B
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4

    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4

    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
