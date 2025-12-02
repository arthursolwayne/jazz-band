
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

# Bars 2-4 (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (Dm7)
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25), # F2
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # Eb2
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # D2
    # Bar 3 (G7)
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=58, start=3.375, end=3.75), # B2
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.125), # A2
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),  # G2
    # Bar 4 (Cm7)
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # C2
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25), # Eb2
    pretty_midi.Note(velocity=90, pitch=49, start=5.25, end=5.625), # D2
    pretty_midi.Note(velocity=90, pitch=48, start=5.625, end=6.0),  # C2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # F5
    # Bar 3: G7
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # C5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # B4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.5),  # F5
    # Bar 4: Cm7
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.0),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # B4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # E4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),   # G4
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.25),  # F4
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # E4
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),   # G4
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25),  # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
