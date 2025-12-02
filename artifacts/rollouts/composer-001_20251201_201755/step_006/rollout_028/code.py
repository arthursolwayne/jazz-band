
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
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # D2
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # A2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C#4
    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F4
    # Bar 4: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Ab4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
sax_notes = [
    # Bar 2: Start the motif on D4 (62)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.65),
    # Bar 3: Continue the motif on F#4 (67)
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.15),
    # Bar 4: Finish the motif on A4 (71)
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.65),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_shorter_intro.mid")
