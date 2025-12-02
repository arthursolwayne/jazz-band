
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

# Bar 2: Everyone comes in
# Bass plays walking line with chromatic approaches
bass_notes = [
    # Bar 2: F -> G -> A -> Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=73, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),  # Bb
    # Bar 3: Bb -> C -> D -> Eb
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=75, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=4.125, end=4.5),  # Eb
    # Bar 4: Eb -> F -> G -> A
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=73, start=5.625, end=6.0),  # A
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4, F7 -> Bb7 -> Eb7 -> A7
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.875),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=95, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.375),
    # Bar 4: Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=95, pitch=77, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),
    # Bar 4: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=95, pitch=73, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=81, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif in F, chromatic approach to Bb, then resolve to F
sax_notes = [
    # Bar 2: Start with motif - F, G#, Bb
    pretty_midi.Note(velocity=105, pitch=71, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=105, pitch=73, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=105, pitch=74, start=1.875, end=2.0),
    # Bar 3: Rest, let the others fill
    # Bar 4: Come back with resolution - F, G, A, Bb
    pretty_midi.Note(velocity=105, pitch=71, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=105, pitch=72, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=105, pitch=73, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=105, pitch=74, start=5.0625, end=5.25),
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_shorter_intro.mid')
