
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, roots and fifths with chromatic approaches
# Fm: F, Ab, D, C
# Bar 2: F -> Ab -> D -> C
# Bar 3: Ab -> Bb -> F -> Eb
# Bar 4: D -> F -> Ab -> G
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75),  # F2
    pretty_midi.Note(velocity=80, pitch=55, start=1.75, end=2.0),  # Ab2
    pretty_midi.Note(velocity=80, pitch=57, start=2.0, end=2.25),  # D2
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.5),  # C2

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=55, start=2.5, end=2.75),  # Ab2
    pretty_midi.Note(velocity=80, pitch=56, start=2.75, end=3.0),  # Bb2
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.25),  # F2
    pretty_midi.Note(velocity=80, pitch=51, start=3.25, end=3.5),  # Eb2

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=57, start=3.5, end=3.75),  # D2
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.0),  # F2
    pretty_midi.Note(velocity=80, pitch=55, start=4.0, end=4.25),  # Ab2
    pretty_midi.Note(velocity=80, pitch=54, start=4.25, end=4.5),  # G2

    # Bar 5
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.75),  # F2
    pretty_midi.Note(velocity=80, pitch=55, start=4.75, end=5.0),  # Ab2
    pretty_midi.Note(velocity=80, pitch=57, start=5.0, end=5.25),  # D2
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.5),  # C2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
# Bar 3: Ab7 (Ab, C, Eb, G)
# Bar 4: D7 (D, F#, A, C)
# Bar 5: Cm7 (C, Eb, G, Bb)
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=2.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0),  # D5

    # Bar 3: Ab7
    pretty_midi.Note(velocity=100, pitch=68, start=2.0, end=2.5),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.5),  # C5
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.5),  # Eb5
    pretty_midi.Note(velocity=100, pitch=79, start=2.0, end=2.5),  # G5

    # Bar 4: D7
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=3.0),  # C5

    # Bar 5: Cm7
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.5),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.5),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # Bb4
]

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: one short motif, start it, leave it hanging, finish it
# Motif: F, Ab, D, C
# Start on 1.5s, play F, Ab on 1.5-1.75, then leave it hanging until 3.0s, then D and C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.75),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # C4
]

for note in sax_notes:
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
# midi.write disabled
