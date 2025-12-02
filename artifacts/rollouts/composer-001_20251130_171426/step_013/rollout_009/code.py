
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-Hat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line, chromatic approaches, D minor
# Dmin7: D F A C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0), # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.5), # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875), # B
    pretty_midi.Note(velocity=80, pitch=73, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.625), # C#
    pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=6.0), # D
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4 (Dmin7, G7, Cm7, F7)
# Dmin7: D F A C
# G7: G B D F
# Cm7: C Eb G Bb
# F7: F A C Eb
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=85, pitch=65, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=85, pitch=72, start=1.5, end=1.875), # C
    # Bar 3
    pretty_midi.Note(velocity=85, pitch=71, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=85, pitch=74, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=85, pitch=76, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=85, pitch=77, start=2.25, end=2.625), # F
    # Bar 4
    pretty_midi.Note(velocity=85, pitch=60, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=85, pitch=63, start=3.0, end=3.375), # Eb
    pretty_midi.Note(velocity=85, pitch=71, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=85, pitch=74, start=3.0, end=3.375), # Bb
    # Bar 5
    pretty_midi.Note(velocity=85, pitch=65, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=85, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=85, pitch=72, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=85, pitch=76, start=3.75, end=4.125), # Eb
    # Bar 6
    pretty_midi.Note(velocity=85, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=85, pitch=65, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=85, pitch=72, start=4.5, end=4.875), # C
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor saxophone. One motif, make it sing.

# Dmin7: D F A C
# Motif: D -> F -> A -> C -> D (chromatic up to A, then resolve)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625), # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875), # E
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.125, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5), # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625), # D
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
