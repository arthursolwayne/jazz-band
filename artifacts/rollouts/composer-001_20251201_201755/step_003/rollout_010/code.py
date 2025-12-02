
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
    # Hihat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # D (root)
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),  # F (fifth)
    pretty_midi.Note(velocity=90, pitch=37, start=2.25, end=2.625),  # Eb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # D (root)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=3.75, end=4.125),  # G (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # D
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=37, start=5.25, end=5.625),  # Eb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano (Diane) - open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s): Dmaj7
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D (D)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G (maj7)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # B (3rd)
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # F# (7th)
    # Bar 3 (3.0 - 4.5s): D7
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C# (dom7)
    # Bar 4 (4.5 - 6.0s): Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A (minor 7th)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # B (minor 3rd)
]
piano.notes.extend(piano_notes)

# Sax (Dante) - short motif, make it sing
sax_notes = [
    # Bar 2 (1.5 - 3.0s): Start the motif
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.875),  # G (Dmaj7 5th)
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),  # G (end of bar)
    # Bar 3 (3.0 - 4.5s): Wait, then resolve
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),  # D (resolve)
    # Bar 4 (4.5 - 6.0s): Repeat motif and finish
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),  # G (finish)
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
