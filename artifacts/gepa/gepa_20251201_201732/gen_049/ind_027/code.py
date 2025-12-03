
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
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus - walking line with chromatic approaches, roots and fifths
bass_notes = [
    # Bar 2: D (D2, 38), chromatic approach to G
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),

    # Bar 3: G (G2, 43), chromatic approach to A
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5),

    # Bar 4: A (A2, 45), chromatic approach to D
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=46, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=47, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Diane - open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C#4

    # Bar 3: G7 (G, B, D, F#)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # F#4

    # Bar 4: A7 (A, C#, E, G#)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # C#4
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # G#4
]
piano.notes.extend(piano_notes)

# Sax: Dante - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (D4, 62) -> F# (F#4, 67) -> A (A4, 71) -> D (D4, 62)
# Start on 1.5s, leave it hanging, then resolve on 3.0s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.9),
    pretty_midi.Note(velocity=100, pitch=71, start=1.9, end=2.0),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25)
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
# Keep the same pattern but with slight velocity changes for dynamics
for note in drum_notes:
    note.velocity = 90 if note.pitch == 38 else 70 if note.pitch == 42 else 110

# Add the instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
