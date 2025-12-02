
import pretty_midi

midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, midi_time=0)]
midi.tempo_changes = [pretty_midi.TempoChange(tempo=120, time=0)]

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # snare on 4 (bar 2)
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),  # D#

    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),  # G

    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.625),  # A#
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0),  # B
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane, 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # Bb

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Bb

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante, short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),  # E

    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.5),  # E

    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: continue for bars 2-4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),     # hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # snare on 4

    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),     # hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # snare on 4

    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
