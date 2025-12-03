
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (38) -> F2 (41) -> A2 (45) -> C3 (48) with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),   # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.875),   # chromatic approach
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),  # chromatic approach
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625),  # chromatic approach
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0),   # C3
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),   # chromatic approach
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F#dim7)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # E
    # Bar 3: G7 (Bdim7)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),  # A
    # Bar 4: Cm7 (Ebdim7)
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),   # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Dm7 (F#dim7) -> G7 (Bdim7) -> Cm7 (Ebdim7)
# Motif: D - F# - A - C (complete in bar 4)
sax_notes = [
    # Bar 2: D (62)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    # Bar 3: F# (66)
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.625),
    # Bar 4: A (69) and C (72)
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=2.875),
    pretty_midi.Note(velocity=110, pitch=72, start=2.875, end=3.0),
]
for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
