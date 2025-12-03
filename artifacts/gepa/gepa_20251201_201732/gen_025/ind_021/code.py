
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
drums.notes.extend(drum_notes)

# Bar 2: Everyone joins in (1.5 - 3.0s)
# Bass: walking line in F (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=79, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=80, start=1.875, end=2.25),  # F#2
    pretty_midi.Note(velocity=80, pitch=81, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=83, start=2.625, end=3.0),   # A2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=84, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=82, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=86, start=1.5, end=1.875),  # E
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=90, pitch=81, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=83, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=85, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=82, start=2.25, end=2.625),  # F
    # Bar 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=90, pitch=82, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=90, pitch=86, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=90, pitch=85, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=90, pitch=83, start=2.625, end=3.0),   # Bb
]
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: motif starts on F (79), moves to A (84), resolves on C (82)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=84, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=82, start=1.75, end=1.875),
    # Bar 3: silence (leave it hanging)
    pretty_midi.Note(velocity=0, pitch=79, start=2.25, end=2.625),
    # Bar 4: return with resolution
    pretty_midi.Note(velocity=100, pitch=79, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=84, start=2.75, end=2.875),
    pretty_midi.Note(velocity=100, pitch=82, start=2.875, end=3.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
