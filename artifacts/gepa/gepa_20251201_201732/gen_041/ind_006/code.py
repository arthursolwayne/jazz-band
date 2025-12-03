
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F (F2, A2, C3, D3)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=76, start=1.875, end=2.25),  # A2
    pretty_midi.Note(velocity=80, pitch=79, start=2.25, end=2.625),  # C3
    pretty_midi.Note(velocity=80, pitch=80, start=2.625, end=3.0),   # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),
    pretty_midi.Note(velocity=95, pitch=76, start=1.5, end=2.25),
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=2.25),
    pretty_midi.Note(velocity=85, pitch=81, start=1.5, end=2.25),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),
    pretty_midi.Note(velocity=95, pitch=71, start=2.25, end=3.0),
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=3.0),
    pretty_midi.Note(velocity=85, pitch=74, start=2.25, end=3.0),
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.75),
    pretty_midi.Note(velocity=95, pitch=81, start=3.0, end=3.75),
    pretty_midi.Note(velocity=90, pitch=82, start=3.0, end=3.75),
    pretty_midi.Note(velocity=85, pitch=72, start=3.0, end=3.75),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif (F, A, Bb)
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=76, start=1.875, end=2.125), # A
    pretty_midi.Note(velocity=110, pitch=77, start=2.125, end=2.5),  # Bb
    # Bar 3: Leave it hanging (no note)
    # Bar 4: Return to finish it (F, A, Bb)
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=76, start=3.375, end=3.625), # A
    pretty_midi.Note(velocity=110, pitch=77, start=3.625, end=4.0),  # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
